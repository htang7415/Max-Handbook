"""seq_scan_vs_index_scan - show the plan shift from full scan to indexed lookup."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_events_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            kind TEXT NOT NULL
        )
        """
    )


def seed_events(conn: sqlite3.Connection, rows: list[tuple[int, str, str]]) -> None:
    conn.executemany(
        """
        INSERT INTO events (workspace_id, created_at, kind)
        VALUES (?, ?, ?)
        """,
        rows,
    )


def add_workspace_created_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_events_workspace_created
        ON events (workspace_id, created_at DESC)
        """
    )


def explain_recent_workspace_events(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 3,
) -> list[str]:
    rows = conn.execute(
        """
        EXPLAIN QUERY PLAN
        SELECT id, created_at
        FROM events
        WHERE workspace_id = ?
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (workspace_id, limit),
    ).fetchall()
    return [detail for _, _, _, detail in rows]


def plan_flags(plan_details: list[str]) -> dict[str, bool]:
    joined = " | ".join(plan_details)
    return {
        "full_scan": "SCAN events" in joined,
        "uses_index": "idx_events_workspace_created" in joined,
        "temp_sort": "USE TEMP B-TREE FOR ORDER BY" in joined,
    }
