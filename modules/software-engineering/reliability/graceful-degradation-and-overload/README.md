# Graceful Degradation And Overload

> Track: `software-engineering` | Topic: `reliability`

## Concept

Graceful degradation keeps core behavior alive when load is too high by shedding optional work before the whole service collapses.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Overload planning | Current load can exceed safe or hard capacity | Capacity is effectively unlimited for the path |
| Feature shedding | Optional work can be disabled before core work fails | All work is equally critical |
| Rate limiting | Excess requests should be bounded during overload | Dropping requests is less safe than queueing them |

## First Principles

- Overload is a normal operating condition, not just a rare incident.
- Capacity needs both a safe zone and a hard limit.
- Optional features should be disabled before core requests are dropped.

## Workflow

1. Define safe and hard request-per-second limits.
2. Classify the current state as healthy, degraded, or overloaded.
3. Disable optional features in degraded state.
4. Add rate limiting when overloaded.
5. Shed only the requests above hard capacity.

## Minimal Code Mental Model

```python
state = capacity_state(current_rps=850, safe_rps=700, hard_rps=900)
shed = requests_to_shed(current_rps=950, hard_rps=900)
actions = degradation_actions("overloaded", ["personalization", "analytics"])
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Invalid capacity range | State classification lies | `capacity_state` validates ordered capacity inputs |
| Optional features stay on | Core path collapses first | `degradation_actions` disables optional features |
| Unknown overload state | Operators cannot predict behavior | `degradation_actions` rejects unknown states |

## Function

```python
def capacity_state(current_rps: int, safe_rps: int, hard_rps: int) -> str:
def requests_to_shed(current_rps: int, hard_rps: int) -> int:
def degradation_actions(state: str, optional_features: list[str]) -> list[str]:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/graceful-degradation-and-overload/python -q
```
