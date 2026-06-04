# Flaky Test Reduction

> Track: `software-engineering` | Topic: `testing`

## Concept

Flaky tests fail intermittently because they depend on unstable time, network, ordering, or shared state instead of a controlled test environment.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Intermittent test failure | The same test passes and fails without code changes | The failure is deterministic and reproducible |
| Test stabilization | Time, network, or shared state appears in the test | The test is already hermetic |
| Quarantine decision | Noise is blocking work but the path is not critical | The test protects a critical path |

## First Principles

- Time, randomness, network access, and shared state are the main flake sources.
- The best fix is usually to remove the unstable dependency, not to add retries.
- Quarantining a flaky test can reduce noise, but it does not solve the underlying bug.

## Workflow

1. Identify uncontrolled dependencies in the test.
2. Estimate flake risk from time, network, and shared state.
3. Replace unstable dependencies with controlled fakes.
4. Quarantine only noncritical high-noise tests.
5. Fix the underlying dependency before restoring trust.

## Minimal Code Mental Model

```python
risk = flake_risk(uses_time=True, uses_network=False, shared_state=True)
steps = stabilization_steps(uses_time=True, uses_network=True, shared_state=False)
quarantine = should_quarantine(failure_rate=0.2, critical_path=False)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Hidden time dependency | Test fails near clock or timeout boundaries | `stabilization_steps` recommends clock injection |
| Network dependency | CI fails from external service behavior | `stabilization_steps` recommends a stub |
| Critical test quarantined | Real regression loses protection | `should_quarantine` blocks quarantine on critical paths |

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
