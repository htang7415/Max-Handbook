"""one_to_many_and_many_to_many - basic relationship table patterns."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_relationship_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            chunk_index INTEGER NOT NULL,
            text TEXT NOT NULL,
            FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
            UNIQUE (document_id, chunk_index)
        );

        CREATE TABLE tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );

        CREATE TABLE document_tags (
            document_id INTEGER NOT NULL,
            tag_id INTEGER NOT NULL,
            FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE,
            PRIMARY KEY (document_id, tag_id)
        );
        """
    )


def insert_document(conn: sqlite3.Connection, title: str) -> int:
    cursor = conn.execute(
        "INSERT INTO documents (title) VALUES (?)",
        (title,),
    )
    return int(cursor.lastrowid)


def insert_chunk(
    conn: sqlite3.Connection,
    document_id: int,
    chunk_index: int,
    text: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO chunks (document_id, chunk_index, text)
        VALUES (?, ?, ?)
        """,
        (document_id, chunk_index, text),
    )
    return int(cursor.lastrowid)


def insert_tag(conn: sqlite3.Connection, name: str) -> int:
    cursor = conn.execute(
        "INSERT INTO tags (name) VALUES (?)",
        (name,),
    )
    return int(cursor.lastrowid)


def link_document_tag(conn: sqlite3.Connection, document_id: int, tag_id: int) -> None:
    conn.execute(
        """
        INSERT INTO document_tags (document_id, tag_id)
        VALUES (?, ?)
        """,
        (document_id, tag_id),
    )


def document_chunk_counts(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    rows = conn.execute(
        """
        SELECT d.title, COUNT(c.id) AS chunk_count
        FROM documents AS d
        LEFT JOIN chunks AS c ON c.document_id = d.id
        GROUP BY d.id, d.title
        ORDER BY d.id
        """
    ).fetchall()
    return [(title, chunk_count) for title, chunk_count in rows]


def document_tag_names(conn: sqlite3.Connection, title: str) -> list[str]:
    rows = conn.execute(
        """
        SELECT t.name
        FROM documents AS d
        JOIN document_tags AS dt ON dt.document_id = d.id
        JOIN tags AS t ON t.id = dt.tag_id
        WHERE d.title = ?
        ORDER BY t.name
        """,
        (title,),
    ).fetchall()
    return [name for (name,) in rows]
