# Cancellation, Deadlines, And Timeouts

> Track: `software-engineering` | Topic: `concurrency`

## Concept

Concurrent work should stop when cancellation is requested or when the remaining deadline budget is too small to finish safely.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Multi-step request | Work must fit inside one caller deadline | Each step is independent and fire-and-forget |
| Background worker | Cancellation or shutdown can interrupt work | Work cannot be safely stopped |
| Dependency call | Cleanup needs reserved time after timeout | There is no cleanup or external side effect |

## First Principles

- Deadlines are easier to compose than independent timeout guesses.
- New work should not start when the remaining budget is already gone.
- Cancellation should be explicit and observable, not hidden as a generic failure.

## Workflow

1. Track total deadline and elapsed time.
2. Compute remaining budget before each step.
3. Reserve cleanup time when needed.
4. Start a step only if it fits inside the remaining budget.
5. Report `cancelled`, `timed_out`, or `running` explicitly.

## Minimal Code Mental Model

```python
remaining = remaining_budget_ms(total_deadline_ms=1200, elapsed_ms=300)
start = can_start_step(remaining_budget_ms=900, step_timeout_ms=400, cleanup_reserve_ms=100)
state = execution_state(cancel_requested=False, remaining_budget_ms=900)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Negative time values | Budget math becomes invalid | Functions reject negative inputs |
| Step starts without cleanup reserve | Timeout leaves partial side effects | `can_start_step` includes cleanup reserve |
| Cancellation hidden as generic failure | Operators cannot distinguish user cancel from timeout | `execution_state` returns explicit state |

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
