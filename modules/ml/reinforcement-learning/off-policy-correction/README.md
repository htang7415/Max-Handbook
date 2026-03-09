# Off-Policy Correction

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Off-policy correction reweights or normalizes samples collected under one policy so they better estimate behavior under another policy.

## Math

$$
w_i = \frac{\pi(a_i \mid s_i)}{b(a_i \mid s_i)}
$$

$$
\hat{\mu}_{\mathrm{WIS}} = \frac{\sum_i w_i r_i}{\sum_i w_i}
$$

- $\pi(a_i \mid s_i)$ -- target-policy probability
- $b(a_i \mid s_i)$ -- behavior-policy probability
- $r_i$ -- observed reward

## Key Points

- Ordinary importance sampling can have very high variance.
- Weighted importance sampling normalizes the weights to reduce instability.
- This module isolates the normalized correction step, not a full offline RL algorithm.

## Function

```python
def weighted_importance_sampling_estimate(
    rewards: list[float],
    target_probs: list[float],
    behavior_probs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/off-policy-correction/python -q
```
