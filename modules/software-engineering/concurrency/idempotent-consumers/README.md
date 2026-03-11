# Idempotent Consumers

> Track: `software-engineering` | Topic: `concurrency`

## Concept

An idempotent consumer can receive the same message more than once without applying the side effect more than once.

## Key Points

- Duplicate delivery is normal in queue-backed systems.
- Deduplication keys should bind the consumer identity to the message identity.
- Processing decisions should happen before the side effect runs.

## Minimal Code Mental Model

```python
key = dedupe_key("msg_1", "invoice-writer")
allowed = should_process_message("msg_1", seen_keys=set(), consumer_name="invoice-writer")
seen = mark_processed("msg_1", seen_keys=set(), consumer_name="invoice-writer")
```

## Function

```python
def dedupe_key(message_id: str, consumer_name: str) -> str:
def should_process_message(message_id: str, seen_keys: set[str], consumer_name: str) -> bool:
def mark_processed(message_id: str, seen_keys: set[str], consumer_name: str) -> set[str]:
```

## Run tests

```bash
pytest modules/software-engineering/concurrency/idempotent-consumers/python -q
```
