# Off-Policy Estimation Methods

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to learn the core estimators for evaluating a target policy from data collected by a different behavior policy.

## First Principles

- Off-policy estimation asks: "How good is policy `pi` if the data came from policy `b`?"
- Importance sampling corrects the mismatch by reweighting each sample by `pi / b`.
- Ordinary importance sampling is unbiased but often high variance.
- Weighted importance sampling normalizes the weights to reduce instability.

## Core Math

Importance weight:

$$
w_i = \frac{\pi(a_i \mid s_i)}{b(a_i \mid s_i)}
$$

Ordinary importance sampling:

$$
\hat{\mu}_{IS} = \frac{1}{n}\sum_{i=1}^{n} r_i w_i
$$

Weighted importance sampling:

$$
\hat{\mu}_{WIS} = \frac{\sum_i r_i w_i}{\sum_i w_i}
$$

## Minimal Code Mental Model

```python
ordinary = importance_sampling_estimate(rewards, target_probs, behavior_probs)
weighted = weighted_importance_sampling_estimate(rewards, target_probs, behavior_probs)
ordinary, weighted = off_policy_estimates(rewards, target_probs, behavior_probs)
```

## Function

```python
def importance_sampling_estimate(rewards: list[float], target_probs: list[float], behavior_probs: list[float]) -> float:
def weighted_importance_sampling_estimate(rewards: list[float], target_probs: list[float], behavior_probs: list[float]) -> float:
def off_policy_estimates(rewards: list[float], target_probs: list[float], behavior_probs: list[float]) -> tuple[float, float]:
```

## When To Use What

- Use ordinary importance sampling when unbiasedness matters most.
- Use weighted importance sampling when variance is the practical bottleneck.
- Compare both side by side when you want a quick bias-versus-variance sanity check.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/off-policy-estimation-methods/python -q
```
