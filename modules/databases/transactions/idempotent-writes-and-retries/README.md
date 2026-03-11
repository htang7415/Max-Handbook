# Idempotent Writes And Retries

> Track: `databases` | Topic: `transactions`

## Concept

Idempotent writes let a client retry after uncertain failures without accidentally creating duplicate side effects.

## Key Points

- A stable request key turns repeated attempts into “same write” instead of “new write”.
- Retries are normal around timeouts and transient failures.
- The database needs a uniqueness rule or ledger keyed by the request identity.
- The return path should tell the caller whether a write was newly created or reused from an earlier attempt.

## Minimal Code Mental Model

```python
conn = create_connection()
create_idempotent_payment_schema(conn)
payment_id, created = process_payment(conn, "req-1", "user-7", 5000)
same_id, created_again = process_payment(conn, "req-1", "user-7", 5000)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_idempotent_payment_schema(conn: sqlite3.Connection) -> None:
def process_payment(
    conn: sqlite3.Connection,
    request_key: str,
    user_id: str,
    amount_cents: int,
    fail_before_commit: bool = False,
) -> tuple[int, bool]:
def payment_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str, int]]:
```

## Run tests

```bash
pytest modules/databases/transactions/idempotent-writes-and-retries/python -q
```
