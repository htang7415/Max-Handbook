# Reward Clipping

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Reward clipping limits extreme rewards to a fixed range so updates are less sensitive to scale spikes.

## Math

$$
\mathrm{clip}(r) = \min(r_{\max}, \max(r_{\min}, r))
$$

- $r$ -- raw reward
- $r_{\min}, r_{\max}$ -- clipping bounds

## Key Points

- Clipping can stabilize value learning when reward magnitudes vary widely.
- It changes the optimization problem, so it is a trade-off rather than a free win.
- The module clips a list of rewards with shared bounds.

## Function

```python
def clip_rewards(rewards: list[float], min_reward: float = -1.0, max_reward: float = 1.0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/reward-clipping/python -q
```
