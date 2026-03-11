# Outbox And Materialized View Patterns

> Track: `databases` | Topic: `streaming`

## Concept

The outbox pattern makes writes publishable, and a materialized view makes those published events cheap to read. Together they form a common operational-to-read-model pipeline.

## Key Points

- Transactional state and outbound events should be written together so downstream projectors cannot miss changes.
- A projector turns ordered events into a query-friendly read model.
- When the same entity changes status, the read model must subtract the old state before adding the new one.
- A full rebuild from the event log should match the incrementally maintained view.

## Minimal Code Mental Model

```python
conn = create_connection()
create_pipeline_tables(conn)
write_order_status(conn, order_id="o1", workspace_id=7, status="placed")
write_order_status(conn, order_id="o1", workspace_id=7, status="completed")
while project_next_event(conn) is not None:
    pass
counts = workspace_status_totals(conn, 7)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_pipeline_tables(conn: sqlite3.Connection) -> None:
def write_order_status(
    conn: sqlite3.Connection,
    order_id: str,
    workspace_id: int,
    status: str,
    fail_before_outbox: bool = False,
) -> None:
def order_rows(conn: sqlite3.Connection) -> list[tuple[str, int, str]]:
def outbox_event_rows(
    conn: sqlite3.Connection,
) -> list[tuple[int, str, int, str, str | None]]:
def next_unprojected_event(
    conn: sqlite3.Connection,
) -> tuple[int, str, int, str] | None:
def project_next_event(conn: sqlite3.Connection) -> int | None:
def workspace_status_totals(
    conn: sqlite3.Connection,
    workspace_id: int,
) -> dict[str, int]:
def rebuild_workspace_status_view(
    events: list[tuple[str, int, str]],
) -> dict[int, dict[str, int]]:
```

## Run tests

```bash
pytest modules/databases/streaming/outbox-and-materialized-view-patterns/python -q
```
