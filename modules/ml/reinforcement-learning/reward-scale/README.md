# Reward Scale

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Reward scale summarizes the average absolute magnitude of rewards, which is a simple way to reason about critic target scale and clipping pressure.

## Math

$$
\mathrm{RewardScale} = \frac{1}{N} \sum_{i=1}^{N} |r_i|
$$

- $r_i$ -- reward on transition $i$

## Key Points

- Reward scale is a descriptive statistic, not a learning update.
- Large reward magnitudes often motivate normalization or clipping.
- This module uses the mean absolute reward.

## Function

```python
def reward_scale(rewards: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/reward-scale/python -q
```
