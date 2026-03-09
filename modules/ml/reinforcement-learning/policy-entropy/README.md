# Policy Entropy

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Policy entropy measures how spread out an action distribution is, which makes it a simple proxy for exploration pressure.

## Math

$$
H(\pi) = - \sum_a \pi(a) \log \pi(a)
$$

- $\pi(a)$ -- probability of taking action $a$

## Key Points

- Entropy is zero for a deterministic policy.
- Higher entropy means the policy is more exploratory.
- This module computes entropy from one discrete action distribution.

## Function

```python
def policy_entropy(probabilities: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/policy-entropy/python -q
```
