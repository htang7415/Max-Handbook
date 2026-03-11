"""entity_vs_event_tables - current-state entities plus append-only events."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_entity_event_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE job_state (
            run_id TEXT PRIMARY KEY,
            status TEXT NOT NULL
        );

        CREATE TABLE job_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id TEXT NOT NULL,
            status TEXT NOT NULL,
            occurred_at TEXT NOT NULL
        );
        """
    )


def upsert_job_state(conn: sqlite3.Connection, run_id: str, status: str) -> None:
    conn.execute(
        """
        INSERT INTO job_state (run_id, status)
        VALUES (?, ?)
        ON CONFLICT(run_id) DO UPDATE SET status = excluded.status
        """,
        (run_id, status),
    )


def append_job_event(
    conn: sqlite3.Connection,
    run_id: str,
    status: str,
    occurred_at: str,
) -> None:
    conn.execute(
        """
        INSERT INTO job_events (run_id, status, occurred_at)
        VALUES (?, ?, ?)
        """,
        (run_id, status, occurred_at),
    )


def current_state_from_entity_table(conn: sqlite3.Connection) -> dict[str, str]:
    rows = conn.execute(
        """
        SELECT run_id, status
        FROM job_state
        ORDER BY run_id
        """
    ).fetchall()
    return {run_id: status for run_id, status in rows}


def current_state_from_event_table(conn: sqlite3.Connection) -> dict[str, str]:
    rows = conn.execute(
        """
        WITH ranked AS (
            SELECT
                run_id,
                status,
                ROW_NUMBER() OVER (
                    PARTITION BY run_id
                    ORDER BY occurred_at DESC, id DESC
                ) AS rn
            FROM job_events
        )
        SELECT run_id, status
        FROM ranked
        WHERE rn = 1
        ORDER BY run_id
        """
    ).fetchall()
    return {run_id: status for run_id, status in rows}
