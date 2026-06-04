# Idempotent Consumers

> Track: `software-engineering` | Topic: `concurrency`

## Concept

An idempotent consumer can receive the same message more than once without applying the side effect more than once.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Queue consumer | The broker can deliver the same message more than once | The source guarantees exactly-once delivery end to end |
| External side effect | Duplicate writes, emails, or API calls would be harmful | Repeating the operation is harmless |
| Multi-consumer system | Different consumers process the same message ID independently | One global message ID should block all consumers |

## First Principles

- Duplicate delivery is normal in queue-backed systems.
- Deduplication keys should bind the consumer identity to the message identity.
- Processing decisions should happen before the side effect runs.

## Workflow

1. Build a dedupe key from message ID and consumer name.
2. Check the dedupe set before running side effects.
3. Process only if the dedupe key is unseen.
4. Mark the message processed after successful side effect.
5. Skip duplicates for the same consumer without blocking other consumers.

## Minimal Code Mental Model

```python
key = dedupe_key("msg_1", "invoice-writer")
allowed = should_process_message("msg_1", seen_keys=set(), consumer_name="invoice-writer")
seen = mark_processed("msg_1", seen_keys=set(), consumer_name="invoice-writer")
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Message ID only | One consumer blocks another unrelated consumer | `dedupe_key` includes consumer name |
| Side effect before dedupe check | Duplicate delivery repeats the write | `should_process_message` decides before processing |
| Blank identity | Dedupe key is ambiguous | Dedupe helpers validate message and consumer names |

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
