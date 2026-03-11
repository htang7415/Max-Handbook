# Worker Retry Semantics

> Track: `software-engineering` | Topic: `concurrency`

## Concept

Worker retry semantics decide whether a failed job should retry, move to a dead-letter queue, or stop immediately.

## Key Points

- Retry only transient failures.
- Max attempts should be explicit and small enough to audit.
- Terminal failures should stop consuming queue capacity quickly.

## Minimal Code Mental Model

```python
action = worker_retry_action("timeout", attempt=1, max_attempts=3)
delay = next_retry_delay_ms(base_delay_ms=200, attempt=2, max_delay_ms=1000)
ack = worker_ack_state(action)
```

## Function

```python
def worker_retry_action(error_type: str, attempt: int, max_attempts: int) -> str:
def next_retry_delay_ms(base_delay_ms: int, attempt: int, max_delay_ms: int) -> int:
def worker_ack_state(action: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/concurrency/worker-retry-semantics/python -q
```
