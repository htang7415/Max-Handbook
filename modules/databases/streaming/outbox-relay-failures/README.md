# Outbox Relay Failures

> Track: `databases` | Topic: `streaming`

## Concept

The outbox pattern makes database writes durable before relay, but the relay itself can still fail at awkward points. If it crashes after publishing an event but before marking it delivered, a retry can publish the same event again.

## Key Points

- Outbox solves “write plus event” atomicity inside the database.
- Relay crashes move the failure boundary to publish-versus-mark behavior.
- Duplicate publication is normal unless downstream consumers are idempotent.
- The practical guarantee is often “at least once from the relay, exactly once only with sink dedup.”

## Minimal Code Mental Model

```python
summary = relay_summary([1, 2], first_failure_event_id=1)
```

## Function

```python
def pending_ids(outbox_ids: list[int], marked_ids: set[int]) -> list[int]:
def duplicate_published_ids(published_ids: list[int]) -> list[int]:
def relay_once(
    outbox_ids: list[int],
    published_ids: list[int],
    marked_ids: set[int],
    fail_after_publish_event_id: int | None = None,
) -> None:
def relay_summary(
    outbox_ids: list[int],
    first_failure_event_id: int | None = None,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/streaming/outbox-relay-failures/python -q
```
