"""sessionization_basics - split events into sessions with a gap threshold."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_event_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            occurred_minute INTEGER NOT NULL
        )
        """
    )


def insert_event(
    conn: sqlite3.Connection,
    user_id: str,
    occurred_minute: int,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO events (user_id, occurred_minute)
        VALUES (?, ?)
        """,
        (user_id, occurred_minute),
    )
    return int(cursor.lastrowid)


def sessionized_events(
    conn: sqlite3.Connection,
    gap_minutes: int,
) -> list[tuple[str, int, int]]:
    rows = conn.execute(
        """
        WITH ordered AS (
            SELECT
                user_id,
                occurred_minute,
                CASE
                    WHEN LAG(occurred_minute) OVER (
                        PARTITION BY user_id
                        ORDER BY occurred_minute, id
                    ) IS NULL THEN 1
                    WHEN occurred_minute - LAG(occurred_minute) OVER (
                        PARTITION BY user_id
                        ORDER BY occurred_minute, id
                    ) > ? THEN 1
                    ELSE 0
                END AS new_session
            FROM events
        ),
        labeled AS (
            SELECT
                user_id,
                occurred_minute,
                SUM(new_session) OVER (
                    PARTITION BY user_id
                    ORDER BY occurred_minute
                    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                ) AS session_id
            FROM ordered
        )
        SELECT user_id, occurred_minute, session_id
        FROM labeled
        ORDER BY user_id, occurred_minute
        """,
        (gap_minutes,),
    ).fetchall()
    return [(user_id, int(occurred_minute), int(session_id)) for user_id, occurred_minute, session_id in rows]


def session_counts(
    conn: sqlite3.Connection,
    gap_minutes: int,
) -> list[tuple[str, int]]:
    rows = conn.execute(
        """
        WITH ordered AS (
            SELECT
                user_id,
                occurred_minute,
                CASE
                    WHEN LAG(occurred_minute) OVER (
                        PARTITION BY user_id
                        ORDER BY occurred_minute, id
                    ) IS NULL THEN 1
                    WHEN occurred_minute - LAG(occurred_minute) OVER (
                        PARTITION BY user_id
                        ORDER BY occurred_minute, id
                    ) > ? THEN 1
                    ELSE 0
                END AS new_session
            FROM events
        )
        SELECT user_id, SUM(new_session) AS session_count
        FROM ordered
        GROUP BY user_id
        ORDER BY user_id
        """,
        (gap_minutes,),
    ).fetchall()
    return [(user_id, int(session_count)) for user_id, session_count in rows]
