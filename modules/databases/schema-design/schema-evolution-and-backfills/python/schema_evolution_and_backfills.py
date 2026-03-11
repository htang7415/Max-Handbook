"""schema_evolution_and_backfills - additive column rollout plus backfill."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_job_table_v1(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_name TEXT NOT NULL,
            job_type TEXT NOT NULL
        )
        """
    )


def evolve_to_v2_add_priority(conn: sqlite3.Connection) -> None:
    conn.execute("ALTER TABLE jobs ADD COLUMN priority TEXT")


def insert_job_v1(conn: sqlite3.Connection, job_name: str, job_type: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO jobs (job_name, job_type)
        VALUES (?, ?)
        """,
        (job_name, job_type),
    )
    return int(cursor.lastrowid)


def insert_job_v2(
    conn: sqlite3.Connection,
    job_name: str,
    job_type: str,
    priority: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO jobs (job_name, job_type, priority)
        VALUES (?, ?, ?)
        """,
        (job_name, job_type, priority),
    )
    return int(cursor.lastrowid)


def backfill_priority(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        UPDATE jobs
        SET priority = CASE
            WHEN job_type = 'incident' THEN 'high'
            ELSE 'normal'
        END
        WHERE priority IS NULL
        """
    )


def job_rows(conn: sqlite3.Connection) -> list[tuple[str, str, str | None]]:
    rows = conn.execute(
        """
        SELECT job_name, job_type, priority
        FROM jobs
        ORDER BY id
        """
    ).fetchall()
    return [
        (str(job_name), str(job_type), None if priority is None else str(priority))
        for job_name, job_type, priority in rows
    ]


def null_priority_count(conn: sqlite3.Connection) -> int:
    row = conn.execute(
        """
        SELECT COUNT(*)
        FROM jobs
        WHERE priority IS NULL
        """
    ).fetchone()
    assert row is not None
    return int(row[0])
