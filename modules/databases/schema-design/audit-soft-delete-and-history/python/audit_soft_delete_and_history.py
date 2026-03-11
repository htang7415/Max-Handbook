"""audit_soft_delete_and_history - current-state rows plus explicit lifecycle audit history."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_audit_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            deleted_at TEXT
        );

        CREATE TABLE document_audit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            action TEXT NOT NULL,
            title TEXT NOT NULL,
            deleted_at TEXT,
            occurred_at TEXT NOT NULL
        );
        """
    )


def insert_document(conn: sqlite3.Connection, title: str, occurred_at: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (title)
        VALUES (?)
        """,
        (title,),
    )
    document_id = int(cursor.lastrowid)
    conn.execute(
        """
        INSERT INTO document_audit (document_id, action, title, deleted_at, occurred_at)
        VALUES (?, 'created', ?, NULL, ?)
        """,
        (document_id, title, occurred_at),
    )
    return document_id


def soft_delete_document(conn: sqlite3.Connection, document_id: int, deleted_at: str) -> None:
    row = conn.execute(
        """
        SELECT title
        FROM documents
        WHERE id = ?
        """,
        (document_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"missing document {document_id}")
    title = str(row[0])
    conn.execute(
        """
        UPDATE documents
        SET deleted_at = ?
        WHERE id = ?
        """,
        (deleted_at, document_id),
    )
    conn.execute(
        """
        INSERT INTO document_audit (document_id, action, title, deleted_at, occurred_at)
        VALUES (?, 'soft-deleted', ?, ?, ?)
        """,
        (document_id, title, deleted_at, deleted_at),
    )


def restore_document(conn: sqlite3.Connection, document_id: int, restored_at: str) -> None:
    row = conn.execute(
        """
        SELECT title
        FROM documents
        WHERE id = ?
        """,
        (document_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"missing document {document_id}")
    title = str(row[0])
    conn.execute(
        """
        UPDATE documents
        SET deleted_at = NULL
        WHERE id = ?
        """,
        (document_id,),
    )
    conn.execute(
        """
        INSERT INTO document_audit (document_id, action, title, deleted_at, occurred_at)
        VALUES (?, 'restored', ?, NULL, ?)
        """,
        (document_id, title, restored_at),
    )


def live_documents(conn: sqlite3.Connection) -> list[tuple[int, str]]:
    rows = conn.execute(
        """
        SELECT id, title
        FROM documents
        WHERE deleted_at IS NULL
        ORDER BY id
        """
    ).fetchall()
    return [(int(document_id), str(title)) for document_id, title in rows]


def audit_history(conn: sqlite3.Connection, document_id: int) -> list[tuple[str, str, str | None]]:
    rows = conn.execute(
        """
        SELECT action, occurred_at, deleted_at
        FROM document_audit
        WHERE document_id = ?
        ORDER BY id
        """,
        (document_id,),
    ).fetchall()
    return [
        (
            str(action),
            str(occurred_at),
            None if deleted_at is None else str(deleted_at),
        )
        for action, occurred_at, deleted_at in rows
    ]
