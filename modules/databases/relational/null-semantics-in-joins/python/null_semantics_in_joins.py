"""null_semantics_in_joins - nullable join keys disappear under inner joins."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_demo_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            assignee_id INTEGER
        );
        """
    )


def seed_users(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
    conn.executemany(
        "INSERT INTO users (id, name) VALUES (?, ?)",
        rows,
    )


def seed_tickets(conn: sqlite3.Connection, rows: list[tuple[str, int | None]]) -> None:
    conn.executemany(
        """
        INSERT INTO tickets (title, assignee_id)
        VALUES (?, ?)
        """,
        rows,
    )


def inner_join_ticket_assignees(conn: sqlite3.Connection) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT t.title, u.name
        FROM tickets AS t
        JOIN users AS u ON u.id = t.assignee_id
        ORDER BY t.id
        """
    ).fetchall()
    return [(str(title), str(name)) for title, name in rows]


def left_join_ticket_assignees(conn: sqlite3.Connection) -> list[tuple[str, str | None]]:
    rows = conn.execute(
        """
        SELECT t.title, u.name
        FROM tickets AS t
        LEFT JOIN users AS u ON u.id = t.assignee_id
        ORDER BY t.id
        """
    ).fetchall()
    return [
        (str(title), None if name is None else str(name))
        for title, name in rows
    ]


def unassigned_tickets(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        """
        SELECT t.title
        FROM tickets AS t
        LEFT JOIN users AS u ON u.id = t.assignee_id
        WHERE u.id IS NULL
        ORDER BY t.id
        """
    ).fetchall()
    return [str(title) for (title,) in rows]
