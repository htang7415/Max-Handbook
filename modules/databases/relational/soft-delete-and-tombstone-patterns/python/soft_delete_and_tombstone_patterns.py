"""soft_delete_and_tombstone_patterns - compare keeping deleted rows to recording delete markers."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_delete_demo_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            deleted_at TEXT
        );

        CREATE TABLE document_tombstones (
            document_id INTEGER PRIMARY KEY,
            deleted_at TEXT NOT NULL,
            reason TEXT NOT NULL
        );
        """
    )


def insert_document(conn: sqlite3.Connection, title: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (title)
        VALUES (?)
        """,
        (title,),
    )
    return int(cursor.lastrowid)


def soft_delete_document(
    conn: sqlite3.Connection,
    document_id: int,
    deleted_at: str,
) -> None:
    conn.execute(
        """
        UPDATE documents
        SET deleted_at = ?
        WHERE id = ?
        """,
        (deleted_at, document_id),
    )


def hard_delete_with_tombstone(
    conn: sqlite3.Connection,
    document_id: int,
    deleted_at: str,
    reason: str,
) -> None:
    row = conn.execute(
        """
        SELECT id
        FROM documents
        WHERE id = ?
        """,
        (document_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"missing document {document_id}")

    conn.execute(
        """
        INSERT INTO document_tombstones (document_id, deleted_at, reason)
        VALUES (?, ?, ?)
        """,
        (document_id, deleted_at, reason),
    )
    conn.execute(
        """
        DELETE FROM documents
        WHERE id = ?
        """,
        (document_id,),
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
    return [(int(document_id), title) for document_id, title in rows]


def all_document_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str | None]]:
    rows = conn.execute(
        """
        SELECT id, title, deleted_at
        FROM documents
        ORDER BY id
        """
    ).fetchall()
    return [
        (int(document_id), title, None if deleted_at is None else str(deleted_at))
        for document_id, title, deleted_at in rows
    ]


def tombstone_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
    rows = conn.execute(
        """
        SELECT document_id, deleted_at, reason
        FROM document_tombstones
        ORDER BY document_id
        """
    ).fetchall()
    return [(int(document_id), deleted_at, reason) for document_id, deleted_at, reason in rows]
