# Null Semantics In Joins

> Track: `databases` | Topic: `relational`

## Concept

`NULL` does not behave like a normal value in SQL joins. A nullable foreign key does not match anything under `=`, so inner joins drop those rows and left joins are often required to preserve them.

## Key Points

- `NULL = anything` is not true, including `NULL = NULL`.
- Inner joins silently remove rows whose join key is `NULL`.
- Left joins preserve those rows and surface `NULL` on the missing side.
- Filtering for missing relationships usually needs `IS NULL`, not `= NULL`.

## Minimal Code Mental Model

```python
rows = left_join_ticket_assignees(conn)
missing = unassigned_tickets(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_demo_tables(conn: sqlite3.Connection) -> None:
def seed_users(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
def seed_tickets(conn: sqlite3.Connection, rows: list[tuple[str, int | None]]) -> None:
def inner_join_ticket_assignees(conn: sqlite3.Connection) -> list[tuple[str, str]]:
def left_join_ticket_assignees(conn: sqlite3.Connection) -> list[tuple[str, str | None]]:
def unassigned_tickets(conn: sqlite3.Connection) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/relational/null-semantics-in-joins/python -q
```
