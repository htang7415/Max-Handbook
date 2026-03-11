"""normalization_vs_denormalization - compare source-of-truth joins to copied read rows."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_normalization_demo_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE orders_normalized (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_code TEXT NOT NULL UNIQUE,
            FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
        );

        CREATE TABLE orders_denormalized (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            customer_name TEXT NOT NULL,
            order_code TEXT NOT NULL UNIQUE
        );
        """
    )


def insert_customer(conn: sqlite3.Connection, name: str) -> int:
    cursor = conn.execute("INSERT INTO customers (name) VALUES (?)", (name,))
    return int(cursor.lastrowid)


def insert_order_rows(
    conn: sqlite3.Connection,
    customer_id: int,
    order_codes: list[str],
) -> None:
    row = conn.execute(
        "SELECT name FROM customers WHERE id = ?",
        (customer_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"missing customer {customer_id}")
    customer_name = row[0]
    conn.executemany(
        "INSERT INTO orders_normalized (customer_id, order_code) VALUES (?, ?)",
        [(customer_id, code) for code in order_codes],
    )
    conn.executemany(
        """
        INSERT INTO orders_denormalized (customer_id, customer_name, order_code)
        VALUES (?, ?, ?)
        """,
        [(customer_id, customer_name, code) for code in order_codes],
    )


def normalized_order_feed(conn: sqlite3.Connection) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT c.name, o.order_code
        FROM orders_normalized AS o
        JOIN customers AS c ON c.id = o.customer_id
        ORDER BY o.id
        """
    ).fetchall()
    return [(customer_name, order_code) for customer_name, order_code in rows]


def denormalized_order_feed(conn: sqlite3.Connection) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT customer_name, order_code
        FROM orders_denormalized
        ORDER BY id
        """
    ).fetchall()
    return [(customer_name, order_code) for customer_name, order_code in rows]


def rename_customer(conn: sqlite3.Connection, customer_id: int, new_name: str) -> tuple[int, int]:
    normalized_updates = conn.execute(
        "UPDATE customers SET name = ? WHERE id = ?",
        (new_name, customer_id),
    ).rowcount
    denormalized_updates = conn.execute(
        """
        UPDATE orders_denormalized
        SET customer_name = ?
        WHERE customer_id = ?
        """,
        (new_name, customer_id),
    ).rowcount
    return normalized_updates, denormalized_updates
