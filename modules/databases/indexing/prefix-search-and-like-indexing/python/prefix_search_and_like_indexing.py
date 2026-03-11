"""prefix_search_and_like_indexing - prefix LIKE can use a B-tree range scan."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA case_sensitive_like = ON")
    return conn


def create_users_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
    )


def seed_names(conn: sqlite3.Connection, names: list[str]) -> None:
    conn.executemany(
        """
        INSERT INTO users (name)
        VALUES (?)
        """,
        [(name,) for name in names],
    )


def add_name_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_users_name
        ON users (name)
        """
    )


def like_prefix_plan(conn: sqlite3.Connection, prefix: str) -> list[str]:
    rows = conn.execute(
        """
        EXPLAIN QUERY PLAN
        SELECT name
        FROM users
        WHERE name LIKE ?
        ORDER BY name
        """,
        (f"{prefix}%",),
    ).fetchall()
    return [detail for _, _, _, detail in rows]


def matching_names(conn: sqlite3.Connection, prefix: str) -> list[str]:
    rows = conn.execute(
        """
        SELECT name
        FROM users
        WHERE name LIKE ?
        ORDER BY name
        """,
        (f"{prefix}%",),
    ).fetchall()
    return [str(name) for (name,) in rows]


def plan_flags(plan_details: list[str]) -> dict[str, bool]:
    joined = " | ".join(plan_details)
    return {
        "full_scan": "SCAN users" in joined,
        "uses_index": "idx_users_name" in joined,
        "temp_sort": "USE TEMP B-TREE FOR ORDER BY" in joined,
    }
