# Bootstrap Target

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Bootstrap targets combine an immediate reward with a discounted estimate of future value from the next state.

## Math

$$
y = r + \gamma (1 - d) V(s')
$$

- $r$ -- immediate reward
- $\gamma$ -- discount factor
- $d$ -- terminal indicator, 1 if the episode ended
- $V(s')$ -- next-state value estimate

## Key Points

- This is the basic one-step target behind many temporal-difference methods.
- Terminal transitions should not bootstrap from the next value.
- This module computes one scalar target.

## Function

```python
def bootstrap_target(reward: float, gamma: float, next_value: float, done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/bootstrap-target/python -q
```
