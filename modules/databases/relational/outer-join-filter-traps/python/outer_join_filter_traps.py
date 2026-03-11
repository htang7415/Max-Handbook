"""outer_join_filter_traps - right-side WHERE filters can erase outer-join rows."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_demo_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            status TEXT NOT NULL
        );
        """
    )


def seed_projects(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
    conn.executemany(
        "INSERT INTO projects (id, name) VALUES (?, ?)",
        rows,
    )


def seed_tasks(conn: sqlite3.Connection, rows: list[tuple[int, str, str]]) -> None:
    conn.executemany(
        """
        INSERT INTO tasks (project_id, title, status)
        VALUES (?, ?, ?)
        """,
        rows,
    )


def open_tasks_filter_in_where(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        """
        SELECT p.name
        FROM projects AS p
        LEFT JOIN tasks AS t
          ON t.project_id = p.id
        WHERE t.status = 'open'
        ORDER BY p.id
        """
    ).fetchall()
    return [str(name) for (name,) in rows]


def open_tasks_filter_in_on(conn: sqlite3.Connection) -> list[tuple[str, str | None]]:
    rows = conn.execute(
        """
        SELECT p.name, t.title
        FROM projects AS p
        LEFT JOIN tasks AS t
          ON t.project_id = p.id
         AND t.status = 'open'
        ORDER BY p.id, t.id
        """
    ).fetchall()
    return [
        (str(project_name), None if task_title is None else str(task_title))
        for project_name, task_title in rows
    ]


def projects_without_open_tasks(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        """
        SELECT p.name
        FROM projects AS p
        LEFT JOIN tasks AS t
          ON t.project_id = p.id
         AND t.status = 'open'
        WHERE t.id IS NULL
        ORDER BY p.id
        """
    ).fetchall()
    return [str(name) for (name,) in rows]
