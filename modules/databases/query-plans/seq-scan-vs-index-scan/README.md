# Seq Scan Vs Index Scan

> Track: `databases` | Topic: `query-plans`

## Concept

Query optimizers choose between reading the whole table and probing an index. A sequential scan is often fine for broad reads, but once a query is selective and ordered on indexed columns, an index scan usually wins.

## Key Points

- A sequential scan reads every row whether most rows match or not.
- An index scan pays lookup overhead but can skip most of the table.
- Good plans depend on both filtering and sort order.
- `EXPLAIN QUERY PLAN` shows when the planner switches from scan to indexed search.

## Minimal Code Mental Model

```python
plan = explain_recent_workspace_events(conn, workspace_id=7)
flags = plan_flags(plan)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_events_table(conn: sqlite3.Connection) -> None:
def seed_events(conn: sqlite3.Connection, rows: list[tuple[int, str, str]]) -> None:
def add_workspace_created_index(conn: sqlite3.Connection) -> None:
def explain_recent_workspace_events(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 3,
) -> list[str]:
def plan_flags(plan_details: list[str]) -> dict[str, bool]:
```

## Run tests

```bash
pytest modules/databases/query-plans/seq-scan-vs-index-scan/python -q
```
