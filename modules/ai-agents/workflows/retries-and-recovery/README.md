# Retries and Recovery

> Track: `ai-agents` | Topic: `workflows`

## Concept

Retries and recovery decide when a failed step should be tried again, how long to wait, and when to fall back to a simpler safe path.

## Key Points

- Retries are useful for transient failures, not for every error.
- Backoff prevents the agent from hammering the same failing dependency.
- Recovery should move to a known fallback instead of looping forever.

## Minimal Code Mental Model

```python
retry = should_retry(error_type="timeout", attempt=1, max_attempts=3)
delay = exponential_backoff_ms(base_delay_ms=200, attempt=2)
next_step = fallback_action("search")
```

## Function

```python
def should_retry(error_type: str, attempt: int, max_attempts: int) -> bool:
def exponential_backoff_ms(base_delay_ms: int, attempt: int) -> int:
def fallback_action(primary_action: str, fallback_map: dict[str, str] | None = None) -> str | None:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/retries-and-recovery/python -q
```
