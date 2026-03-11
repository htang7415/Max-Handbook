# Flaky Test Reduction

> Track: `software-engineering` | Topic: `testing`

## Concept

Flaky tests fail intermittently because they depend on unstable time, network, ordering, or shared state instead of a controlled test environment.

## Key Points

- Time, randomness, network access, and shared state are the main flake sources.
- The best fix is usually to remove the unstable dependency, not to add retries.
- Quarantining a flaky test can reduce noise, but it does not solve the underlying bug.

## Minimal Code Mental Model

```python
risk = flake_risk(uses_time=True, uses_network=False, shared_state=True)
steps = stabilization_steps(uses_time=True, uses_network=True, shared_state=False)
quarantine = should_quarantine(failure_rate=0.2, critical_path=False)
```

## Function

```python
def flake_risk(uses_time: bool, uses_network: bool, shared_state: bool) -> str:
def stabilization_steps(uses_time: bool, uses_network: bool, shared_state: bool) -> list[str]:
def should_quarantine(failure_rate: float, critical_path: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/testing/flaky-test-reduction/python -q
```
