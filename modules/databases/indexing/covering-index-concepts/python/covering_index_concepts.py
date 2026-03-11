"""covering_index_concepts - compare index-assisted and index-only reads."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_documents_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )


def seed_documents(
    conn: sqlite3.Connection,
    rows: list[tuple[int, str, str]],
) -> None:
    conn.executemany(
        """
        INSERT INTO documents (workspace_id, title, created_at)
        VALUES (?, ?, ?)
        """,
        rows,
    )


def add_non_covering_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_documents_workspace_created
        ON documents (workspace_id, created_at DESC)
        """
    )


def add_covering_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_documents_workspace_created_title
        ON documents (workspace_id, created_at DESC, title)
        """
    )


def query_plan(conn: sqlite3.Connection, workspace_id: int) -> list[str]:
    rows = conn.execute(
        """
        EXPLAIN QUERY PLAN
        SELECT title, created_at
        FROM documents
        WHERE workspace_id = ?
        ORDER BY created_at DESC
        """,
        (workspace_id,),
    ).fetchall()
    return [detail for _, _, _, detail in rows]


def plan_summary(plan_details: list[str]) -> dict[str, bool]:
    joined = " | ".join(plan_details)
    return {
        "uses_index": "USING INDEX" in joined or "USING COVERING INDEX" in joined,
        "uses_covering_index": "USING COVERING INDEX" in joined,
        "temp_sort": "USE TEMP B-TREE FOR ORDER BY" in joined,
    }


def query_rows(conn: sqlite3.Connection, workspace_id: int) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT title, created_at
        FROM documents
        WHERE workspace_id = ?
        ORDER BY created_at DESC
        """,
        (workspace_id,),
    ).fetchall()
    return [(title, created_at) for title, created_at in rows]
