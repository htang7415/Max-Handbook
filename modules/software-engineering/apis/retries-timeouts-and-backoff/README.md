# Retries, Timeouts, And Backoff

> Track: `software-engineering` | Topic: `apis`

## Concept

Retries help with transient failures only when the request is safe to repeat and the caller enforces bounded timeouts and backoff.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Transient dependency failure | Status codes include timeout, rate limit, or 5xx errors | The operation is not safe to repeat |
| Mutating API call | The request has an idempotency key | The mutation has no duplicate guard |
| Deadline budgeting | A caller has a fixed end-to-end timeout | Each retry can wait indefinitely |

## First Principles

- Not every error should be retried.
- Mutating requests usually need idempotency before retries are safe.
- Backoff reduces pressure on a failing dependency.
- Timeout budgets should be explicit instead of growing with every retry.

## Workflow

1. Decide whether the method is retryable.
2. Require idempotency for retried POST requests.
3. Retry only retryable HTTP statuses.
4. Use capped exponential backoff between attempts.
5. Divide the total deadline into bounded per-attempt timeouts.

## Minimal Code Mental Model

```python
safe = retryable_request("POST", has_idempotency_key=True)
retry = should_retry_http(503, "POST", has_idempotency_key=True)
delay = capped_backoff_ms(base_delay_ms=200, attempt=3, max_delay_ms=1000)
attempt_timeout = per_attempt_timeout_ms(total_deadline_ms=1200, max_attempts=3)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Retrying unsafe mutation | Duplicate side effects | `retryable_request` rejects POST without idempotency |
| Retrying client errors | Load increases without recovery | `should_retry_http` retries only selected statuses |
| Unbounded wait | Retries exceed caller deadline | `per_attempt_timeout_ms` divides a fixed deadline |

## Function

```python
def retryable_request(method: str, has_idempotency_key: bool = False) -> bool:
def should_retry_http(status_code: int, method: str, has_idempotency_key: bool = False) -> bool:
def capped_backoff_ms(base_delay_ms: int, attempt: int, max_delay_ms: int) -> int:
def per_attempt_timeout_ms(total_deadline_ms: int, max_attempts: int) -> int:
```

## Run tests

```bash
pytest modules/software-engineering/apis/retries-timeouts-and-backoff/python -q
```
