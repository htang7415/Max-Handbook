# Reward, Return, Discount

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Return is the discounted sum of rewards.

## Math
$$G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}$$

- $G_t$ -- return at step t
- $\gamma$ -- discount factor
- $r_{t+k}$ -- reward observed $k$ steps after time $t$
- $G$ -- return
- $t$ -- timestep or iteration
- $k$ -- future-step offset in the discounted sum
- $r$ -- reward

## Function

```python
def discounted_return(rewards: list[float], gamma: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/return-discount/python -q
```
