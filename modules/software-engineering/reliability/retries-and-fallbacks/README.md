# Retries And Fallbacks

> Track: `software-engineering` | Topic: `reliability`

## Concept

Retries are for transient failures on safe operations, and fallbacks are for keeping degraded service alive when retries are no longer worth the cost.

## Use When

| Situation | Response |
| --- | --- |
| A safe operation hits a transient error | Retry with a small budget |
| The primary path is too slow or unavailable | Use a simpler fallback |
| The operation may duplicate side effects | Avoid blind retries |

## First Principles

- Retries should prefer idempotent operations.
- Max attempts should be explicit and small.
- Fallback targets should be simpler or cheaper than the primary path.

## Workflow

1. Classify the error as transient, permanent, or unknown.
2. Retry only when the operation is safe or idempotent.
3. Cap attempts and delay growth.
4. Switch to a fallback before the retry budget harms users or dependencies.

## Minimal Code Mental Model

```python
action = retry_action("timeout", attempt=1, max_attempts=3, idempotent=True)
delay = retry_delay_ms(base_delay_ms=200, attempt=2, max_delay_ms=1000)
fallback = fallback_target("live-recommendations")
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Retrying non-idempotent writes | Duplicate side effects |
| Unlimited retries | Load amplification during an outage |
| Expensive fallback | Degraded mode fails under the same pressure |

## Function

```python
def retry_action(error_type: str, attempt: int, max_attempts: int, idempotent: bool) -> str:
def retry_delay_ms(base_delay_ms: int, attempt: int, max_delay_ms: int) -> int:
def fallback_target(primary_path: str, fallback_map: dict[str, str] | None = None) -> str | None:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/retries-and-fallbacks/python -q
```
