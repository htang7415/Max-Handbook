# Entropy Bonus

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Entropy bonus adds a scaled entropy term to the objective so policy updates keep some exploration pressure.

## Math

$$
\mathcal{B} = \beta H(\pi) = -\beta \sum_a \pi(a)\log \pi(a)
$$

- $\beta$ -- entropy regularization coefficient
- $\pi(a)$ -- action probability for action $a$

## Key Points

- Entropy bonus turns policy entropy into a directly weighted optimization term.
- Larger coefficients encourage more exploration.
- This module computes the bonus for one discrete policy.

## Function

```python
def entropy_bonus(probabilities: list[float], coefficient: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/entropy-bonus/python -q
```
