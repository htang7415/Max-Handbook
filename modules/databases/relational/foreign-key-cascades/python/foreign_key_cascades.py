"""foreign_key_cascades - delete owned child rows automatically with ON DELETE CASCADE."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_cascade_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE workspaces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            FOREIGN KEY (workspace_id) REFERENCES workspaces(id) ON DELETE CASCADE
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            body TEXT NOT NULL,
            FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE
        );
        """
    )


def insert_workspace(conn: sqlite3.Connection, name: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO workspaces (name)
        VALUES (?)
        """,
        (name,),
    )
    return int(cursor.lastrowid)


def insert_document(conn: sqlite3.Connection, workspace_id: int, title: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (workspace_id, title)
        VALUES (?, ?)
        """,
        (workspace_id, title),
    )
    return int(cursor.lastrowid)


def insert_chunk(conn: sqlite3.Connection, document_id: int, body: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO chunks (document_id, body)
        VALUES (?, ?)
        """,
        (document_id, body),
    )
    return int(cursor.lastrowid)


def delete_document(conn: sqlite3.Connection, document_id: int) -> None:
    conn.execute(
        """
        DELETE FROM documents
        WHERE id = ?
        """,
        (document_id,),
    )


def delete_workspace(conn: sqlite3.Connection, workspace_id: int) -> None:
    conn.execute(
        """
        DELETE FROM workspaces
        WHERE id = ?
        """,
        (workspace_id,),
    )


def row_counts(conn: sqlite3.Connection) -> dict[str, int]:
    tables = ["workspaces", "documents", "chunks"]
    counts: dict[str, int] = {}
    for table in tables:
        row = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
        assert row is not None
        counts[table] = int(row[0])
    return counts
