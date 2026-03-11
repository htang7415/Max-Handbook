# Canary Rollout And Rollback

> Track: `software-engineering` | Topic: `reliability`

## Concept

A canary rollout sends a small share of traffic to a new version, expands only when health stays acceptable, and rolls back quickly when it does not.

## Key Points

- Canary health should be compared against a baseline, not judged in isolation.
- Traffic steps should be explicit and easy to audit.
- A bad canary should go to zero fast instead of waiting for more evidence while users are hurt.

## Minimal Code Mental Model

```python
healthy = canary_healthy(baseline_error_rate=0.01, canary_error_rate=0.015, max_increase=0.01)
next_pct = next_canary_percentage(current_percentage=10, healthy=healthy)
decision = rollout_decision(current_percentage=10, healthy=healthy)
```

## Function

```python
def canary_healthy(baseline_error_rate: float, canary_error_rate: float, max_increase: float) -> bool:
def next_canary_percentage(current_percentage: int, healthy: bool) -> int:
def rollout_decision(current_percentage: int, healthy: bool) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/canary-rollout-and-rollback/python -q
```
