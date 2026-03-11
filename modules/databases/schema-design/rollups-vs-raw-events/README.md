# Rollups Vs Raw Events

> Track: `databases` | Topic: `schema-design`

## Concept

Raw event tables preserve full detail. Rollup tables pre-aggregate hot query paths. Good systems often keep both because they solve different problems.

## Key Points

- Raw events are the source of truth for audits, backfills, and new analyses.
- Rollups trade freshness and flexibility for cheaper reads.
- Rebuild or incremental maintenance is the real cost of rollups.
- This pattern is common in analytics tables, dashboards, and agent usage reporting.

## Minimal Code Mental Model

```python
insert_event(conn, 1, "2026-03-01T10:00", 5)
rebuild_hourly_rollups(conn)
total = rollup_total(conn, 1, "2026-03-01T10:00")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_rollup_schema(conn: sqlite3.Connection) -> None:
def insert_event(conn: sqlite3.Connection, workspace_id: int, hour_bucket: str, amount: int) -> int:
def rebuild_hourly_rollups(conn: sqlite3.Connection) -> None:
def raw_total(conn: sqlite3.Connection, workspace_id: int, hour_bucket: str) -> int:
def rollup_total(conn: sqlite3.Connection, workspace_id: int, hour_bucket: str) -> int:
def row_counts(conn: sqlite3.Connection) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/schema-design/rollups-vs-raw-events/python -q
```
