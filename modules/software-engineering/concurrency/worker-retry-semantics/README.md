# Worker Retry Semantics

> Track: `software-engineering` | Topic: `concurrency`

## Concept

Worker retry semantics decide whether a failed job should retry, move to a dead-letter queue, or stop immediately.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Background worker | Jobs can fail from transient or terminal causes | The task cannot be retried safely |
| Queue retry policy | Attempts and delays should be bounded | Failures are handled synchronously by the caller |
| Dead-letter handling | Repeated failures need investigation | The job has no durable message identity |

## First Principles

- Retry only transient failures.
- Max attempts should be explicit and small enough to audit.
- Terminal failures should stop consuming queue capacity quickly.

## Workflow

1. Classify the error as transient or terminal.
2. Compare current attempt with max attempts.
3. Retry transient failures while attempts remain.
4. Move exhausted retries to dead letter.
5. Acknowledge or requeue based on the chosen action.

## Minimal Code Mental Model

```python
action = worker_retry_action("timeout", attempt=1, max_attempts=3)
delay = next_retry_delay_ms(base_delay_ms=200, attempt=2, max_delay_ms=1000)
ack = worker_ack_state(action)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Terminal error retried | Queue capacity is wasted | `worker_retry_action` stops non-transient failures |
| Infinite retry | Bad jobs never leave the queue | Max attempts force dead-letter behavior |
| Unbounded retry delay | Recovery becomes unpredictable | `next_retry_delay_ms` applies capped backoff |

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
