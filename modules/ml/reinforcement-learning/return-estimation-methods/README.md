# Return Estimation Methods

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to learn the main ways RL estimates future reward:
discounted return, n-step return, Monte Carlo returns, n-step TD targets, and TD(lambda).

## First Principles

- A `return` is the future reward signal a learner tries to predict or optimize.
- Monte Carlo methods wait for more real rewards before estimating the target.
- TD methods bootstrap from a value estimate before the full episode is finished.
- n-step methods sit between one-step TD and full Monte Carlo returns.
- TD(lambda) mixes short and long horizons to trade bias against variance.

## Core Math

Discounted return:

$$
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}
$$

n-step return:

$$
G_t^{(n)} = \sum_{k=0}^{n-1} \gamma^k r_{t+k+1} + \gamma^n V_{\text{boot}}
$$

TD(lambda) return:

$$
G_t^\lambda = r_{t+1} + \gamma \left((1-\lambda)V(s_{t+1}) + \lambda G_{t+1}^\lambda \right)
$$

## Minimal Code Mental Model

```python
full = discounted_return(rewards, gamma=0.99)
target = n_step_return(rewards[:3], gamma=0.99, bootstrap_value=v_boot)
lambda_targets = td_lambda_returns(rewards, next_values, gamma=0.99, lam=0.95)
```

## Function

```python
def discounted_return(rewards: list[float], gamma: float) -> float:
def n_step_return(rewards: list[float], gamma: float, bootstrap_value: float = 0.0) -> float:
def n_step_td_target(rewards: list[float], bootstrap_value: float, gamma: float) -> float:
def td_lambda_returns(rewards: list[float], next_state_values: list[float], gamma: float, lam: float, terminal_value: float = 0.0) -> list[float]:
def first_visit_returns(states: list[str], rewards: list[float], gamma: float) -> dict[str, float]:
```

## When To Use What

- Use discounted return when you want the cleanest definition of future reward.
- Use n-step return when you want a short rollout plus one bootstrap value.
- Use first-visit Monte Carlo returns when you want pure episode-based targets.
- Use n-step TD targets when you want explicit control over the reward horizon.
- Use TD(lambda) when you want a smoother interpolation between TD and Monte Carlo.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/return-estimation-methods/python -q
```
