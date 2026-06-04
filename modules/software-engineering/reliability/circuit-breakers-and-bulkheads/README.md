# Circuit Breakers And Bulkheads

> Track: `software-engineering` | Topic: `reliability`

## Concept

Circuit breakers stop traffic to a failing dependency, and bulkheads keep one overloaded path from consuming all capacity needed by others.

## Use When

| Situation | Pattern |
| --- | --- |
| A dependency repeatedly times out or fails | Circuit breaker |
| A dependency may recover but needs controlled traffic | Half-open probes |
| One work class can starve another | Bulkhead isolation |

## First Principles

- A circuit should open after repeated failures, not after one noisy event.
- Half-open probes let a dependency earn traffic back carefully.
- Bulkheads reserve capacity for independent work instead of sharing one overloaded pool.

## Workflow

1. Count consecutive failures or failure rate by dependency.
2. Open the circuit when the threshold is crossed.
3. Allow only limited probes after the cooldown.
4. Isolate capacity for important work classes.

## Minimal Code Mental Model

```python
state = circuit_state(consecutive_failures=5, failure_threshold=4, cooldown_complete=False)
allowed = allow_dependency_call(state, probe_budget=1)
isolated = bulkhead_available(active_work=7, capacity=6)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Opening after one noisy failure | Unnecessary outage amplification |
| No half-open state | Dependency recovery is either ignored or flooded |
| One shared worker pool | Low-priority work can exhaust critical capacity |

## Function

```python
def circuit_state(consecutive_failures: int, failure_threshold: int, cooldown_complete: bool) -> str:
def allow_dependency_call(state: str, probe_budget: int = 0) -> bool:
def bulkhead_available(active_work: int, capacity: int) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/circuit-breakers-and-bulkheads/python -q
```
