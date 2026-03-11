# Serializable Retries

> Track: `databases` | Topic: `transactions`

## Concept

Serializable isolation can abort a transaction instead of letting an unsafe interleaving commit. Application code therefore needs a retry loop, not just one attempt.

## Key Points

- A serialization failure is often a normal concurrency outcome, not a fatal bug.
- The transaction body should be safe to retry from the beginning.
- Retry budgets and backoff matter when contention is heavy.
- Serializable safety is only practical if the application treats retry as part of the contract.

## Minimal Code Mental Model

```python
summary = run_serializable_retry_loop([True, True, False], max_retries=3)
```

## Function

```python
def run_serializable_retry_loop(
    conflicts: list[bool],
    max_retries: int,
) -> dict[str, int | bool]:
def should_backoff(conflicts: list[bool]) -> bool:
```

## Run tests

```bash
pytest modules/databases/transactions/serializable-retries/python -q
```
