import pytest

from idempotent_writes_and_retries import (
    create_connection,
    create_idempotent_payment_schema,
    payment_rows,
    process_payment,
)


def build_connection():
    conn = create_connection()
    create_idempotent_payment_schema(conn)
    return conn


def test_same_request_key_returns_existing_write_on_retry() -> None:
    conn = build_connection()
    payment_id, created = process_payment(conn, "req-1", "user-7", 5000)
    same_payment_id, created_again = process_payment(conn, "req-1", "user-7", 5000)

    assert (payment_id, created) == (1, True)
    assert (same_payment_id, created_again) == (1, False)
    assert payment_rows(conn) == [(1, "req-1", "user-7", 5000)]


def test_failed_attempt_rolls_back_cleanly_so_retry_creates_once() -> None:
    conn = build_connection()

    with pytest.raises(RuntimeError):
        process_payment(conn, "req-1", "user-7", 5000, fail_before_commit=True)

    payment_id, created = process_payment(conn, "req-1", "user-7", 5000)

    assert (payment_id, created) == (1, True)
    assert payment_rows(conn) == [(1, "req-1", "user-7", 5000)]


def test_different_request_keys_create_distinct_rows() -> None:
    conn = build_connection()
    process_payment(conn, "req-1", "user-7", 5000)
    process_payment(conn, "req-2", "user-7", 5000)

    assert payment_rows(conn) == [
        (1, "req-1", "user-7", 5000),
        (2, "req-2", "user-7", 5000),
    ]
