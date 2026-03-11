# Exactly Once Claims Vs Reality

> Track: `databases` | Topic: `streaming`

## Concept

“Exactly once” is usually an end-to-end property, not a magic transport promise. If a sink applies duplicate deliveries twice, the business result is still wrong even if the broker has strong semantics in the middle.

## Key Points

- Duplicate delivery is normal in retry-heavy distributed systems.
- A non-idempotent sink can still double charge or double count.
- End-to-end safety often needs stable event IDs and sink-side deduplication.
- Marketing language around exactly once is less important than the actual source-to-sink contract.

## Minimal Code Mental Model

```python
events = [
    delivered_event("e1", "acct-1", 10),
    delivered_event("e1", "acct-1", 10),
]
summary = delivery_summary(events)
```

## Function

```python
def delivered_event(event_id: str, key: str, amount: int) -> dict[str, object]:
def duplicate_event_ids(events: list[dict[str, object]]) -> list[str]:
def non_idempotent_sink_totals(events: list[dict[str, object]]) -> dict[str, int]:
def idempotent_sink_totals(events: list[dict[str, object]]) -> dict[str, int]:
def end_to_end_safe(events: list[dict[str, object]], sink_idempotent: bool) -> bool:
```

## Run tests

```bash
pytest modules/databases/streaming/exactly-once-claims-vs-reality/python -q
```
