# Cancellation, Deadlines, And Timeouts

> Track: `software-engineering` | Topic: `concurrency`

## Concept

Concurrent work should stop when cancellation is requested or when the remaining deadline budget is too small to finish safely.

## Key Points

- Deadlines are easier to compose than independent timeout guesses.
- New work should not start when the remaining budget is already gone.
- Cancellation should be explicit and observable, not hidden as a generic failure.

## Minimal Code Mental Model

```python
remaining = remaining_budget_ms(total_deadline_ms=1200, elapsed_ms=300)
start = can_start_step(remaining_budget_ms=900, step_timeout_ms=400, cleanup_reserve_ms=100)
state = execution_state(cancel_requested=False, remaining_budget_ms=900)
```

## Function

```python
def remaining_budget_ms(total_deadline_ms: int, elapsed_ms: int) -> int:
def can_start_step(remaining_budget_ms: int, step_timeout_ms: int, cleanup_reserve_ms: int = 0) -> bool:
def execution_state(cancel_requested: bool, remaining_budget_ms: int) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/concurrency/cancellation-deadlines-and-timeouts/python -q
```
