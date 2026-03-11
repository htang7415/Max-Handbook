# Expression Index Basics

> Track: `databases` | Topic: `indexing`

## Concept

If your query always applies a function like `lower(email)` or `date(created_at)`, a plain index on the raw column may not help. An expression index stores the transformed value so those function-shaped predicates can use an access path too.

## Key Points

- Function-wrapped predicates often break normal index usage.
- Expression indexes materialize the transformed lookup key.
- The indexed expression must match the query shape closely.
- They are useful for normalized lookups like case-insensitive search.

## Minimal Code Mental Model

```python
add_lower_email_index(conn)
plan = explain_lookup_by_lower_email(conn, "ada@example.com")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_users_table(conn: sqlite3.Connection) -> None:
def seed_users(conn: sqlite3.Connection, rows: list[tuple[str, str]]) -> None:
def add_lower_email_index(conn: sqlite3.Connection) -> None:
def explain_lookup_by_lower_email(conn: sqlite3.Connection, email: str) -> list[str]:
def matching_names(conn: sqlite3.Connection, email: str) -> list[str]:
def plan_flags(plan_details: list[str]) -> dict[str, bool]:
```

## Run tests

```bash
pytest modules/databases/indexing/expression-index-basics/python -q
```
