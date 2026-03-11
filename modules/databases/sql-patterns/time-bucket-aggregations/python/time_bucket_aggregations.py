"""time_bucket_aggregations - roll events into fixed time buckets for reporting."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_metric_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            occurred_at TEXT NOT NULL,
            amount INTEGER NOT NULL
        )
        """
    )


def insert_metric(
    conn: sqlite3.Connection,
    workspace_id: int,
    occurred_at: str,
    amount: int,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO metrics (workspace_id, occurred_at, amount)
        VALUES (?, ?, ?)
        """,
        (workspace_id, occurred_at, amount),
    )
    return int(cursor.lastrowid)


def totals_by_hour(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    rows = conn.execute(
        """
        SELECT substr(occurred_at, 1, 13) || ':00' AS bucket, SUM(amount) AS total_amount
        FROM metrics
        GROUP BY bucket
        ORDER BY bucket
        """
    ).fetchall()
    return [(bucket, int(total_amount)) for bucket, total_amount in rows]


def workspace_hour_totals(conn: sqlite3.Connection) -> list[tuple[int, str, int]]:
    rows = conn.execute(
        """
        SELECT
            workspace_id,
            substr(occurred_at, 1, 13) || ':00' AS bucket,
            SUM(amount) AS total_amount
        FROM metrics
        GROUP BY workspace_id, bucket
        ORDER BY workspace_id, bucket
        """
    ).fetchall()
    return [(int(workspace_id), bucket, int(total_amount)) for workspace_id, bucket, total_amount in rows]
