# Q-Learning Target

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

The Q-learning target is the bootstrapped value used before applying the learning-rate update.

## Math

$$
\mathrm{target} = r + \gamma \max_a Q(s', a)
$$

- $r$ -- immediate reward
- $\gamma$ -- discount factor
- $Q(s', a)$ -- next-state action values

## Key Points

- This isolates the target from the full Q-update.
- The same target appears inside the standard Q-learning update rule.
- It pairs naturally with TD error and double-Q variants.

## Function

```python
def q_target(reward: float, gamma: float, next_q_values: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/q-target/python -q
```
