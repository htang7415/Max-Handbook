"""funnel_conversion_basics - count ordered user progression through funnel stages."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_funnel_events_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE funnel_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            stage TEXT NOT NULL,
            occurred_at TEXT NOT NULL,
            UNIQUE (user_id, stage)
        )
        """
    )


def insert_funnel_event(
    conn: sqlite3.Connection,
    user_id: str,
    stage: str,
    occurred_at: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO funnel_events (user_id, stage, occurred_at)
        VALUES (?, ?, ?)
        """,
        (user_id, stage, occurred_at),
    )
    return int(cursor.lastrowid)


def stage_times_by_user(conn: sqlite3.Connection) -> dict[str, dict[str, str]]:
    rows = conn.execute(
        """
        SELECT user_id, stage, occurred_at
        FROM funnel_events
        ORDER BY user_id, occurred_at, id
        """
    ).fetchall()
    stage_times: dict[str, dict[str, str]] = {}
    for user_id, stage, occurred_at in rows:
        user_rows = stage_times.setdefault(str(user_id), {})
        user_rows[str(stage)] = str(occurred_at)
    return stage_times


def funnel_counts(conn: sqlite3.Connection, stages: list[str]) -> list[tuple[str, int]]:
    stage_times = stage_times_by_user(conn)
    valid_users: dict[str, str] = {}
    counts: list[tuple[str, int]] = []

    for index, stage in enumerate(stages):
        next_valid: dict[str, str] = {}
        for user_id, user_stage_times in stage_times.items():
            current_time = user_stage_times.get(stage)
            if current_time is None:
                continue
            if index == 0:
                next_valid[user_id] = current_time
                continue
            previous_time = valid_users.get(user_id)
            if previous_time is not None and current_time >= previous_time:
                next_valid[user_id] = current_time

        counts.append((stage, len(next_valid)))
        valid_users = next_valid
    return counts


def conversion_rates(conn: sqlite3.Connection, stages: list[str]) -> list[tuple[str, float]]:
    counts = funnel_counts(conn, stages)
    rates: list[tuple[str, float]] = []
    previous_count: int | None = None
    for stage, count in counts:
        if previous_count is None:
            rates.append((stage, 1.0 if count > 0 else 0.0))
        else:
            rates.append((stage, 0.0 if previous_count == 0 else count / previous_count))
        previous_count = count
    return rates
