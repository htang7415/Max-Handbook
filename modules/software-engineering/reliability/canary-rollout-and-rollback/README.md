# Canary Rollout And Rollback

> Track: `software-engineering` | Topic: `reliability`

## Concept

A canary rollout sends a small share of traffic to a new version, expands only when health stays acceptable, and rolls back quickly when it does not.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Risky release | Production traffic may expose failures tests missed | The change can be fully validated offline |
| Progressive rollout | Traffic can move through explicit percentages | Traffic cannot be routed by version |
| Rollback gate | Health can be compared against a baseline | There is no reliable health signal |

## First Principles

- Canary health should be compared against a baseline, not judged in isolation.
- Traffic steps should be explicit and easy to audit.
- A bad canary should go to zero fast instead of waiting for more evidence while users are hurt.

## Workflow

1. Pick the current canary percentage from the allowed steps.
2. Compare canary error rate with baseline plus allowed increase.
3. Expand to the next step when healthy.
4. Roll back to zero when unhealthy.
5. Complete only when the healthy rollout reaches the final step.

## Minimal Code Mental Model

```python
healthy = canary_healthy(baseline_error_rate=0.01, canary_error_rate=0.015, max_increase=0.01)
next_pct = next_canary_percentage(current_percentage=10, healthy=healthy)
decision = rollout_decision(current_percentage=10, healthy=healthy)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Canary judged without baseline | Normal traffic noise looks like release health | `canary_healthy` compares against baseline plus threshold |
| Unknown rollout step | Operators cannot audit traffic movement | `next_canary_percentage` rejects unknown percentages |
| Slow rollback | Users stay on a bad version | Unhealthy canary returns `0` and `rollback` |

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
