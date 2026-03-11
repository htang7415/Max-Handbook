# Covering Index Concepts

> Track: `databases` | Topic: `indexing`

## Concept

A covering index contains every column the query needs, so the database can answer the query from the index alone without looking up the base table rows.

## Key Points

- A non-covering index can still help filtering and ordering, but it may need extra table lookups to fetch selected columns.
- Adding projected columns to the index can make the same query index-only.
- Covering indexes trade more storage for less read work on hot paths.
- `EXPLAIN QUERY PLAN` often exposes this with `USING COVERING INDEX`.

## Minimal Code Mental Model

```python
conn = create_connection()
create_documents_table(conn)
seed_documents(conn, rows)
add_non_covering_index(conn)
noncover = plan_summary(query_plan(conn, workspace_id=7))
add_covering_index(conn)
cover = plan_summary(query_plan(conn, workspace_id=7))
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_documents_table(conn: sqlite3.Connection) -> None:
def seed_documents(
    conn: sqlite3.Connection,
    rows: list[tuple[int, str, str]],
) -> None:
def add_non_covering_index(conn: sqlite3.Connection) -> None:
def add_covering_index(conn: sqlite3.Connection) -> None:
def query_plan(conn: sqlite3.Connection, workspace_id: int) -> list[str]:
def plan_summary(plan_details: list[str]) -> dict[str, bool]:
def query_rows(conn: sqlite3.Connection, workspace_id: int) -> list[tuple[str, str]]:
```

## Run tests

```bash
pytest modules/databases/indexing/covering-index-concepts/python -q
```
