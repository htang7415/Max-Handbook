# Canary Rollout

> Track: `ml` | Topic: `mlops`

## Concept

Canary rollout gradually increases traffic to a new model while watching guardrail metrics like error rate or latency.

## Math

$$
\mathrm{next\_share} =
\begin{cases}
\min(1, s + \Delta) & \text{if metric is healthy} \\
\max(0, s - \Delta) & \text{if metric breaches threshold}
\end{cases}
$$

- $s$ -- current canary traffic share
- $\Delta$ -- rollout step size

## Key Points

- Rollouts should advance in bounded steps, not jump straight to 100%.
- Guardrails let the system roll back automatically when a canary degrades.
- This goes beyond a static split by modeling the staged progression itself.

## Function

```python
def next_canary_share(
    current_share: float,
    step: float,
    error_rate: float,
    threshold: float,
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/canary-rollout/python -q
```
