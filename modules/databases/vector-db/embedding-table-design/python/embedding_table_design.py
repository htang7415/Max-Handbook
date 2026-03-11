"""embedding_table_design - explicit chunk/model embedding rows with freshness metadata."""

from __future__ import annotations

import json
import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_embedding_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            doc_type TEXT NOT NULL,
            text TEXT NOT NULL
        );

        CREATE TABLE chunk_embeddings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chunk_id INTEGER NOT NULL,
            model_name TEXT NOT NULL,
            job_id TEXT NOT NULL,
            vector_json TEXT NOT NULL,
            FOREIGN KEY (chunk_id) REFERENCES chunks(id) ON DELETE CASCADE,
            UNIQUE (chunk_id, model_name, job_id)
        );
        """
    )


def insert_chunk(
    conn: sqlite3.Connection,
    workspace_id: int,
    doc_type: str,
    text: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO chunks (workspace_id, doc_type, text)
        VALUES (?, ?, ?)
        """,
        (workspace_id, doc_type, text),
    )
    return int(cursor.lastrowid)


def insert_embedding(
    conn: sqlite3.Connection,
    chunk_id: int,
    model_name: str,
    job_id: str,
    vector: list[float],
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO chunk_embeddings (chunk_id, model_name, job_id, vector_json)
        VALUES (?, ?, ?, ?)
        """,
        (chunk_id, model_name, job_id, json.dumps(vector)),
    )
    return int(cursor.lastrowid)


def embedding_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
    rows = conn.execute(
        """
        SELECT chunk_id, model_name, job_id
        FROM chunk_embeddings
        ORDER BY chunk_id, model_name, job_id
        """
    ).fetchall()
    return [(chunk_id, model_name, job_id) for chunk_id, model_name, job_id in rows]


def chunks_missing_model(conn: sqlite3.Connection, model_name: str) -> list[int]:
    rows = conn.execute(
        """
        SELECT c.id
        FROM chunks AS c
        LEFT JOIN chunk_embeddings AS ce
          ON ce.chunk_id = c.id
         AND ce.model_name = ?
        WHERE ce.id IS NULL
        ORDER BY c.id
        """,
        (model_name,),
    ).fetchall()
    return [chunk_id for (chunk_id,) in rows]
