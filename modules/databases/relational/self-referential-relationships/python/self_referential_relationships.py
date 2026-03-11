"""self_referential_relationships - adjacency-list hierarchies inside one table."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_employee_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            manager_id INTEGER,
            FOREIGN KEY (manager_id) REFERENCES employees(id)
        )
        """
    )


def insert_employee(
    conn: sqlite3.Connection,
    name: str,
    manager_id: int | None = None,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO employees (name, manager_id)
        VALUES (?, ?)
        """,
        (name, manager_id),
    )
    return int(cursor.lastrowid)


def direct_reports(conn: sqlite3.Connection, manager_id: int) -> list[str]:
    rows = conn.execute(
        """
        SELECT name
        FROM employees
        WHERE manager_id = ?
        ORDER BY id
        """,
        (manager_id,),
    ).fetchall()
    return [str(name) for (name,) in rows]


def management_chain(conn: sqlite3.Connection, employee_id: int) -> list[str]:
    chain: list[str] = []
    current_id = employee_id
    while True:
        row = conn.execute(
            """
            SELECT manager.id, manager.name
            FROM employees AS e
            LEFT JOIN employees AS manager
              ON manager.id = e.manager_id
            WHERE e.id = ?
            """,
            (current_id,),
        ).fetchone()
        if row is None:
            raise ValueError(f"missing employee {employee_id}")
        manager_id, manager_name = row
        if manager_id is None:
            return chain
        chain.append(str(manager_name))
        current_id = int(manager_id)
