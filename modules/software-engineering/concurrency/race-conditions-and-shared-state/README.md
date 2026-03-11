# Race Conditions And Shared State

> Track: `software-engineering` | Topic: `concurrency`

## Concept

A race condition happens when concurrent work observes or writes shared state in an order the code did not intend.

## Key Points

- Shared mutable state is the main source of concurrency bugs.
- Version checks are a simple way to prevent lost updates.
- More writers without coordination usually means higher risk.

## Minimal Code Mental Model

```python
allowed = optimistic_write_allowed(current_version=4, expected_version=4)
value, version = apply_versioned_update(10, delta=5, current_version=4, expected_version=4)
risk = shared_state_risk(concurrent_writers=3, uses_coordination=False)
```

## Function

```python
def optimistic_write_allowed(current_version: int, expected_version: int) -> bool:
def apply_versioned_update(
    current_value: int,
    delta: int,
    current_version: int,
    expected_version: int,
) -> tuple[int, int]:
def shared_state_risk(concurrent_writers: int, uses_coordination: bool) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/concurrency/race-conditions-and-shared-state/python -q
```
