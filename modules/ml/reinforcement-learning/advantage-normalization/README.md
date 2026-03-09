# Advantage Normalization

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Advantage normalization rescales a batch of advantages to zero mean and unit variance before the policy update.

## Math

$$
\tilde{A}_i = \frac{A_i - \mu_A}{\sigma_A + \epsilon}
$$

- $A_i$ -- raw advantage
- $\mu_A$ -- batch mean advantage
- $\sigma_A$ -- batch standard deviation
- $\epsilon$ -- numerical stabilizer

## Key Points

- Normalization can reduce update-scale instability in PPO-style training.
- It does not change the ordering of the advantages.
- This module isolates the batch normalization step only.

## Function

```python
def normalize_advantages(advantages: list[float], eps: float = 1.0e-8) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/advantage-normalization/python -q
```
