# CDC Vs Application Events

> Track: `databases` | Topic: `streaming`

## Concept

CDC events describe row-level data changes after commit, while application events describe business meaning the application chose to publish.

## Key Points

- CDC is good for replication and downstream state sync.
- Application events are good for workflows like notifications or billing triggers.
- CDC can reconstruct table state, but it may miss business intent.
- Application events can express intent, but they may not contain enough data to rebuild every table exactly.

## Minimal Code Mental Model

```python
events = [
    cdc_event("orders", "insert", "o1", {"status": "placed"}),
    application_event("order.created", "o1", {"customer_id": "c1"}),
]
row = latest_row_from_cdc(events, "orders", "o1")
names = application_event_names(events)
```

## Function

```python
def cdc_event(table: str, op: str, row_id: str, after: dict[str, object] | None) -> dict[str, object]:
def application_event(name: str, aggregate_id: str, payload: dict[str, object]) -> dict[str, object]:
def latest_row_from_cdc(
    events: list[dict[str, object]],
    table: str,
    row_id: str,
) -> dict[str, object] | None:
def application_event_names(events: list[dict[str, object]]) -> list[str]:
def event_kinds(events: list[dict[str, object]]) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/streaming/cdc-vs-application-events/python -q
```
