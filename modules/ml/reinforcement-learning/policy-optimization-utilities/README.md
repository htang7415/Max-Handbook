# Policy Optimization Utilities

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to learn the small but important utilities around PPO-style policy optimization:
entropy terms, batch normalization, reward scaling, and reward clipping.

## First Principles

- Policy entropy measures how uncertain the action distribution is.
- Entropy bonus turns that uncertainty into an optimization term that encourages exploration.
- Advantage normalization stabilizes policy updates by standardizing the batch scale.
- Value-target normalization helps critics deal with unstable reward magnitudes.
- Reward scale and reward clipping are simple ways to reason about or control target magnitude.

## Core Math

Policy entropy:

$$
H(\pi) = -\sum_a \pi(a)\log \pi(a)
$$

Entropy bonus:

$$
\mathcal{B} = \beta H(\pi)
$$

Advantage normalization:

$$
\tilde{A}_i = \frac{A_i - \mu_A}{\sigma_A + \epsilon}
$$

## Minimal Code Mental Model

```python
entropy = policy_entropy(probs)
bonus = entropy_bonus(probs, coefficient=0.01)
advantages = normalize_advantages(raw_advantages)
clipped_rewards = clip_rewards(rewards, -1.0, 1.0)
```

## Function

```python
def policy_entropy(probabilities: list[float]) -> float:
def entropy_bonus(probabilities: list[float], coefficient: float) -> float:
def normalize_advantages(advantages: list[float], eps: float = 1.0e-8) -> list[float]:
def normalize_value_targets(values: list[float], eps: float = 1.0e-8) -> tuple[list[float], float, float]:
def reward_scale(rewards: list[float]) -> float:
def clip_rewards(rewards: list[float], min_reward: float = -1.0, max_reward: float = 1.0) -> list[float]:
```

## When To Use What

- Use policy entropy to inspect how exploratory a policy still is.
- Use entropy bonus when you want exploration pressure inside the objective.
- Use advantage normalization in PPO-style batched updates.
- Use value normalization when critic targets vary too much in scale.
- Use reward scale as a diagnostic and reward clipping as a deliberate stabilization trade-off.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/policy-optimization-utilities/python -q
```
