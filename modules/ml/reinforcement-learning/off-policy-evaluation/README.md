# Off-Policy Evaluation

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Off-policy evaluation estimates how a target policy would perform using data collected by a different behavior policy.

## Math

$$
\hat{\mu}_{IS} = \frac{1}{n} \sum_{i=1}^{n} r_i \frac{\pi(a_i \mid s_i)}{b(a_i \mid s_i)}
$$

$$
\hat{\mu}_{WIS} = \frac{\sum_i r_i \frac{\pi(a_i \mid s_i)}{b(a_i \mid s_i)}}{\sum_i \frac{\pi(a_i \mid s_i)}{b(a_i \mid s_i)}}
$$

- $\pi(a_i \mid s_i)$ -- target-policy probability
- $b(a_i \mid s_i)$ -- behavior-policy probability
- $r_i$ -- observed reward

## Key Points

- Ordinary importance sampling is unbiased but can have very high variance.
- Weighted importance sampling trades some bias for lower variance.
- This module returns both estimates side by side.

## Function

```python
def off_policy_estimates(
    rewards: list[float],
    target_probs: list[float],
    behavior_probs: list[float],
) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/off-policy-evaluation/python -q
```
