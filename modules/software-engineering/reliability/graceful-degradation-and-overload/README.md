# Graceful Degradation And Overload

> Track: `software-engineering` | Topic: `reliability`

## Concept

Graceful degradation keeps core behavior alive when load is too high by shedding optional work before the whole service collapses.

## Key Points

- Overload is a normal operating condition, not just a rare incident.
- Capacity needs both a safe zone and a hard limit.
- Optional features should be disabled before core requests are dropped.

## Minimal Code Mental Model

```python
state = capacity_state(current_rps=850, safe_rps=700, hard_rps=900)
shed = requests_to_shed(current_rps=950, hard_rps=900)
actions = degradation_actions("overloaded", ["personalization", "analytics"])
```

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
