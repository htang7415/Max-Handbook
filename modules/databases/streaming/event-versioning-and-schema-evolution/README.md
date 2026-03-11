# Event Versioning And Schema Evolution

> Track: `databases` | Topic: `streaming`

## Concept

Event schemas change over time, but streams usually contain old and new versions at once. Consumers need a compatibility strategy so they can normalize multiple versions into one internal shape.

## Key Points

- Streams rarely switch all events to one schema version instantly.
- Consumers should normalize old and new payloads into one model.
- Additive evolution is safer than breaking field renames without translation.
- Version handling belongs in the consumer contract, not in wishful thinking.

## Minimal Code Mental Model

```python
normalized = normalize_order_event(event_v2)
```

## Function

```python
def order_event_v1(order_id: str, status: str) -> dict[str, object]:
def order_event_v2(order_id: str, status: str, workspace_id: int) -> dict[str, object]:
def normalize_order_event(event: dict[str, object]) -> dict[str, object]:
def normalized_stream(events: list[dict[str, object]]) -> list[dict[str, object]]:
```

## Run tests

```bash
pytest modules/databases/streaming/event-versioning-and-schema-evolution/python -q
```
