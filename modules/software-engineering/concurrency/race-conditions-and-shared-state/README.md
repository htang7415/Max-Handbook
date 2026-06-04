# Race Conditions And Shared State

> Track: `software-engineering` | Topic: `concurrency`

## Concept

A race condition happens when concurrent work observes or writes shared state in an order the code did not intend.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Shared write path | Multiple workers or requests can update the same value | State is immutable or single-owner |
| Optimistic update | You can compare an expected version before writing | The operation needs pessimistic locking or transactions |
| Risk review | Writer count and coordination are known | The state boundary is still unclear |

## First Principles

- Shared mutable state is the main source of concurrency bugs.
- Version checks are a simple way to prevent lost updates.
- More writers without coordination usually means higher risk.

## Workflow

1. Identify the shared value and its version.
2. Require the caller to send the version it observed.
3. Compare expected and current versions before writing.
4. Increment the version only after a successful write.
5. Classify risk from writer count and coordination.

## Minimal Code Mental Model

```python
allowed = optimistic_write_allowed(current_version=4, expected_version=4)
value, version = apply_versioned_update(10, delta=5, current_version=4, expected_version=4)
risk = shared_state_risk(concurrent_writers=3, uses_coordination=False)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Stale write | Later work overwrites newer state | `apply_versioned_update` rejects mismatched versions |
| Negative version | Invalid state enters the concurrency model | `optimistic_write_allowed` rejects negative versions |
| Uncoordinated writers | Risk rises as writers increase | `shared_state_risk` returns `high` without coordination |

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
