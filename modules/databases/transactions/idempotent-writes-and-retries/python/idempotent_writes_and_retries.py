"""idempotent_writes_and_retries - safe retryable writes keyed by request identity."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.isolation_level = None
    return conn


def create_idempotent_payment_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_key TEXT NOT NULL UNIQUE,
            user_id TEXT NOT NULL,
            amount_cents INTEGER NOT NULL
        )
        """
    )


def process_payment(
    conn: sqlite3.Connection,
    request_key: str,
    user_id: str,
    amount_cents: int,
    fail_before_commit: bool = False,
) -> tuple[int, bool]:
    existing = conn.execute(
        """
        SELECT id
        FROM payments
        WHERE request_key = ?
        """,
        (request_key,),
    ).fetchone()
    if existing is not None:
        return int(existing[0]), False

    conn.execute("BEGIN")
    try:
        cursor = conn.execute(
            """
            INSERT INTO payments (request_key, user_id, amount_cents)
            VALUES (?, ?, ?)
            """,
            (request_key, user_id, amount_cents),
        )
        payment_id = int(cursor.lastrowid)
        if fail_before_commit:
            raise RuntimeError("simulated timeout before commit")
        conn.execute("COMMIT")
        return payment_id, True
    except Exception:
        conn.execute("ROLLBACK")
        raise


def payment_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str, int]]:
    rows = conn.execute(
        """
        SELECT id, request_key, user_id, amount_cents
        FROM payments
        ORDER BY id
        """
    ).fetchall()
    return [(payment_id, request_key, user_id, amount_cents) for payment_id, request_key, user_id, amount_cents in rows]
