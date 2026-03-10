# Reinforcement Learning

Reinforcement learning is about choosing actions that improve long-run reward, not just immediate reward.

## Purpose

Use this page to learn the main RL ideas in the right order:
- environment and return
- value estimation and bootstrapping
- exploration
- value-based vs policy-based updates
- RL for LLMs only after the basics make sense

## First Principles

- `Return` is the discounted sum of future rewards.
- `Value estimation` asks how good a state or action is.
- `Bootstrapping` uses current estimates to update future estimates.
- `Exploration` trades short-term reward for better information.
- `Policy methods` optimize action probabilities directly; `value methods` optimize targets such as Q-values.

## Core Math

- Return:
  $$
  G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}
  $$
- Bellman target:
  $$
  Q(s,a) \leftarrow r + \gamma \max_{a'} Q(s', a')
  $$
- TD error:
  $$
  \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
  $$
- Policy gradient shape:
  $$
  \nabla J(\theta) = \mathbb{E}\left[\nabla \log \pi_\theta(a \mid s) A(s,a)\right]
  $$

## Minimal Code Mental Model

```python
action = policy(state)
next_state, reward, done = env.step(action)
replay.add(state, action, reward, next_state, done)
update_value_or_policy(replay.sample())
```

## Canonical Modules

- Foundations: `mdp`, `exploration-exploitation`
- Bandits and exploration: `bandit-exploration-methods`
- Return estimation: `return-estimation-methods`
- Value-based RL: `td-control-methods`
- Policy-based RL: `policy-gradient-methods`, `policy-optimization-utilities`
- Planning: `monte-carlo-tree-search`
- Off-policy ideas: `off-policy-estimation-methods`

## Supporting Guides

- RL-for-LLM guide (`docs/ml/reinforcement-learning/rl-for-llm`)
- Transition indicators guide (`docs/ml/reinforcement-learning/transition-indicators`)

## When To Use What

- Start with bandits when there is no state transition structure.
- Use value-based RL when bootstrapped action values are the main learning object.
- Use policy gradients or PPO when the policy itself is the main object and action spaces are harder to optimize with pure Q-learning.
- Use Monte Carlo or n-step prediction when you want the connection between returns and bootstrapping to be explicit.
- Use `transition-indicators` when you need the simplest done-mask logic for TD targets or batched RL code.
- Use RL-for-LLM only after MDPs, returns, bootstrapping, and policy gradients are already clear.
