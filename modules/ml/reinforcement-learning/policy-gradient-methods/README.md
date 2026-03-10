# Policy Gradient Methods

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to learn the main policy-gradient path in one place:
REINFORCE, generalized advantage estimation, and PPO clipping.

## First Principles

- Policy-gradient methods optimize the policy directly instead of learning only a greedy Q target.
- REINFORCE is the simplest score-function update: push up log-probability when return is high.
- Advantage estimates reduce variance by centering updates around how much better an action was than expected.
- PPO keeps policy updates conservative by clipping the probability ratio.

## Core Math

REINFORCE update shape:

$$
\nabla_\theta J = \mathbb{E}\left[R \nabla_\theta \log \pi_\theta(a \mid s)\right]
$$

GAE recursion:

$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
$$

$$
A_t^{\mathrm{GAE}} = \delta_t + \gamma \lambda A_{t+1}^{\mathrm{GAE}}
$$

PPO clipped term:

$$
\min\left(r_t A_t, \mathrm{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t\right)
$$

## Minimal Code Mental Model

```python
advantages = generalized_advantages(rewards, values, gamma=0.99, lam=0.95)
ratio = new_prob / old_prob
objective = ppo_objective_term(ratio, advantages[t], eps=0.2)
step = reinforce_update(grad_logp, reward=advantages[t], lr=1.0e-4)
```

## Function

```python
def reinforce_update(grad_logp: float, reward: float, lr: float) -> float:
def clip_ratio(ratio: float, eps: float) -> float:
def ppo_objective_term(ratio: float, advantage: float, eps: float) -> float:
def generalized_advantages(rewards: list[float], values: list[float], gamma: float, lam: float, next_value: float = 0.0) -> list[float]:
```

## When To Use What

- Use REINFORCE to understand the simplest policy-gradient estimator.
- Use GAE when policy-gradient updates are too noisy.
- Use PPO when you want a practical clipped objective for stable on-policy updates.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/policy-gradient-methods/python -q
```
