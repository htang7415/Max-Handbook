# TD Control Methods

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to compare the main temporal-difference control targets used in value-based RL:
Q-learning, SARSA, Expected SARSA, Double Q-learning, and target-network updates.

## First Principles

- TD control learns action values from one-step targets instead of waiting for full returns.
- The main difference between methods is which next-step value they bootstrap from.
- Q-learning is off-policy because it bootstraps from the greedy next action.
- SARSA is on-policy because it bootstraps from the action the policy actually takes.
- Double Q-learning separates action selection from action evaluation to reduce overestimation.
- Target networks slow down moving targets in deep value-based RL.

## Core Math

General TD update:

$$
Q \leftarrow Q + \alpha (y - Q)
$$

Q-learning target:

$$
y = r + \gamma \max_{a'} Q(s', a')
$$

SARSA target:

$$
y = r + \gamma Q(s', a')
$$

Expected SARSA target:

$$
y = r + \gamma \sum_a \pi(a \mid s') Q(s', a)
$$

## Minimal Code Mental Model

```python
target = q_learning_target(reward, gamma, next_q_values, done)
error = td_error(value=q_sa, target=target)
q_sa = td_update(value=q_sa, target=target, alpha=0.1)
target_net = soft_target_update(target_net, online_net, tau=0.01)
```

## Function

```python
def bootstrap_target(reward: float, gamma: float, next_value: float, done: bool = False) -> float:
def q_learning_target(reward: float, gamma: float, next_q_values: list[float], done: bool = False) -> float:
def sarsa_target(reward: float, gamma: float, next_q: float, done: bool = False) -> float:
def expected_sarsa_target(reward: float, gamma: float, next_action_probs: list[float], next_q_values: list[float], done: bool = False) -> float:
def double_q_target(reward: float, gamma: float, selector_values: list[float], evaluator_values: list[float], done: bool = False) -> float:
def td_error(value: float, target: float) -> float:
def td_update(value: float, target: float, alpha: float) -> float:
def soft_target_update(target_values: list[float], online_values: list[float], tau: float) -> list[float]:
def soft_update_gap(target_values: list[float], online_values: list[float], tau: float) -> float:
```

## When To Use What

- Use Q-learning as the default greedy TD-control baseline.
- Use SARSA when the on-policy next action is part of the learning target.
- Use Expected SARSA when you want the target to average over a policy instead of sampling one action.
- Use Double Q-learning when overestimation bias matters.
- Use soft target updates when deep value functions make greedy targets too unstable.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/td-control-methods/python -q
```
