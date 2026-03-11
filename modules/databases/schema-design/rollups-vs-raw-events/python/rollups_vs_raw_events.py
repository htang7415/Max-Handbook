"""rollups_vs_raw_events - raw events preserve detail while rollups speed hot reads."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_rollup_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE raw_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            hour_bucket TEXT NOT NULL,
            amount INTEGER NOT NULL
        );

        CREATE TABLE hourly_rollups (
            workspace_id INTEGER NOT NULL,
            hour_bucket TEXT NOT NULL,
            total_amount INTEGER NOT NULL,
            PRIMARY KEY (workspace_id, hour_bucket)
        );
        """
    )


def insert_event(conn: sqlite3.Connection, workspace_id: int, hour_bucket: str, amount: int) -> int:
    cursor = conn.execute(
        """
        INSERT INTO raw_events (workspace_id, hour_bucket, amount)
        VALUES (?, ?, ?)
        """,
        (workspace_id, hour_bucket, amount),
    )
    return int(cursor.lastrowid)


def rebuild_hourly_rollups(conn: sqlite3.Connection) -> None:
    conn.execute("DELETE FROM hourly_rollups")
    conn.execute(
        """
        INSERT INTO hourly_rollups (workspace_id, hour_bucket, total_amount)
        SELECT workspace_id, hour_bucket, SUM(amount)
        FROM raw_events
        GROUP BY workspace_id, hour_bucket
        """
    )


def raw_total(conn: sqlite3.Connection, workspace_id: int, hour_bucket: str) -> int:
    row = conn.execute(
        """
        SELECT COALESCE(SUM(amount), 0)
        FROM raw_events
        WHERE workspace_id = ? AND hour_bucket = ?
        """,
        (workspace_id, hour_bucket),
    ).fetchone()
    assert row is not None
    return int(row[0])


def rollup_total(conn: sqlite3.Connection, workspace_id: int, hour_bucket: str) -> int:
    row = conn.execute(
        """
        SELECT COALESCE(total_amount, 0)
        FROM hourly_rollups
        WHERE workspace_id = ? AND hour_bucket = ?
        """,
        (workspace_id, hour_bucket),
    ).fetchone()
    return 0 if row is None else int(row[0])


def row_counts(conn: sqlite3.Connection) -> dict[str, int]:
    raw_count = conn.execute("SELECT COUNT(*) FROM raw_events").fetchone()
    rollup_count = conn.execute("SELECT COUNT(*) FROM hourly_rollups").fetchone()
    assert raw_count is not None and rollup_count is not None
    return {
        "raw_events": int(raw_count[0]),
        "hourly_rollups": int(rollup_count[0]),
    }
