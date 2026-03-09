# Soft Update Gap

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Soft update gap measures how much lag remains between online parameters and target parameters after a Polyak-style target-network update.

## Math

With target parameters $\theta^-$, online parameters $\theta$, and update rate $\tau$:

$$
\theta^-_{\text{new}} = (1 - \tau)\theta^- + \tau\theta
$$

This module reports the mean absolute post-update gap:

$$
\frac{1}{N} \sum_{i=1}^{N} \left| \theta_i - \theta^-_{\text{new}, i} \right|
$$

## Key Points

- Smaller $\tau$ leaves more lag in the target network.
- The remaining gap is one way to reason about target-network smoothness.
- This module is a metric; it does not return updated parameters.

## Function

```python
def soft_update_gap(target_values: list[float], online_values: list[float], tau: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/soft-update-gap/python -q
```
