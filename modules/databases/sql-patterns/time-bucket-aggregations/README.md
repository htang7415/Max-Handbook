# Time Bucket Aggregations

> Track: `databases` | Topic: `sql-patterns`

## Concept

Time-bucket aggregation groups events into fixed windows such as minutes, hours, or days. It is the basic shape behind dashboards, rate charts, and freshness reporting.

## Key Points

- Buckets turn raw event streams into regular reporting intervals.
- Grouping by a normalized timestamp is the core SQL pattern.
- Time buckets can be global or split by dimensions such as workspace or tenant.
- Fixed buckets are different from sessions or sliding windows; they do not depend on user behavior.

## Minimal Code Mental Model

```python
insert_metric(conn, 1, "2026-03-01T10:05:00", 5)
insert_metric(conn, 1, "2026-03-01T10:45:00", 7)
rows = totals_by_hour(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_metric_table(conn: sqlite3.Connection) -> None:
def insert_metric(conn: sqlite3.Connection, workspace_id: int, occurred_at: str, amount: int) -> int:
def totals_by_hour(conn: sqlite3.Connection) -> list[tuple[str, int]]:
def workspace_hour_totals(conn: sqlite3.Connection) -> list[tuple[int, str, int]]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/time-bucket-aggregations/python -q
```
