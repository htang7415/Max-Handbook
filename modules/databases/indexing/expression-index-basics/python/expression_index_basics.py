"""expression_index_basics - use an index on lower(email) for case-insensitive lookup."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_users_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )


def seed_users(conn: sqlite3.Connection, rows: list[tuple[str, str]]) -> None:
    conn.executemany(
        """
        INSERT INTO users (name, email)
        VALUES (?, ?)
        """,
        rows,
    )


def add_lower_email_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_users_lower_email
        ON users (lower(email))
        """
    )


def explain_lookup_by_lower_email(conn: sqlite3.Connection, email: str) -> list[str]:
    rows = conn.execute(
        """
        EXPLAIN QUERY PLAN
        SELECT name
        FROM users
        WHERE lower(email) = ?
        """,
        (email.lower(),),
    ).fetchall()
    return [detail for _, _, _, detail in rows]


def matching_names(conn: sqlite3.Connection, email: str) -> list[str]:
    rows = conn.execute(
        """
        SELECT name
        FROM users
        WHERE lower(email) = ?
        ORDER BY id
        """,
        (email.lower(),),
    ).fetchall()
    return [name for (name,) in rows]


def plan_flags(plan_details: list[str]) -> dict[str, bool]:
    joined = " | ".join(plan_details)
    return {
        "full_scan": "SCAN users" in joined,
        "uses_expression_index": "idx_users_lower_email" in joined,
    }
