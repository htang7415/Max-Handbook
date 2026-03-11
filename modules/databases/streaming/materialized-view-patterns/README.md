# Materialized View Patterns

> Track: `databases` | Topic: `streaming`

## Concept

A materialized view is a precomputed read model that is incrementally updated from an event stream instead of recalculated from scratch on every query.

## Key Points

- The event log is the source of truth, but the view is optimized for reads.
- When an entity changes status, the view usually removes the old aggregate contribution and adds the new one.
- Incremental maintenance should match a full rebuild from the same event stream.
- Materialized views are one of the main reasons streaming systems can serve low-latency dashboards.

## Minimal Code Mental Model

```python
view = empty_view()
apply_order_status_event(view, {"order_id": "o1", "workspace_id": 7, "status": "queued"})
apply_order_status_event(view, {"order_id": "o1", "workspace_id": 7, "status": "completed"})
counts = workspace_status_counts(view, 7)
```

## Function

```python
def empty_view() -> dict[str, object]:
def apply_order_status_event(
    view: dict[str, object],
    event: dict[str, object],
) -> None:
def rebuild_view(events: list[dict[str, object]]) -> dict[str, object]:
def workspace_status_counts(
    view: dict[str, object],
    workspace_id: int,
) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/streaming/materialized-view-patterns/python -q
```
