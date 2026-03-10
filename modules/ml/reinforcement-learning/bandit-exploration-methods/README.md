# Bandit Exploration Methods

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to learn the core bandit exploration methods together:
incremental value estimation, epsilon-greedy selection, and UCB.

## First Principles

- A multi-armed bandit has actions and rewards, but no state transitions.
- The main question is how to trade off `exploration` and `exploitation`.
- You usually keep an estimate of each arm's reward and update it online.
- Epsilon-greedy explores randomly; UCB explores arms with high uncertainty.

## Core Math

Incremental mean update:

$$
Q_n = Q_{n-1} + \frac{R_n - Q_{n-1}}{n}
$$

Epsilon-greedy action probability:

$$
\pi(a) =
\begin{cases}
\frac{\epsilon}{K} + (1-\epsilon) & \text{if } a \text{ is greedy} \\
\frac{\epsilon}{K} & \text{otherwise}
\end{cases}
$$

UCB score:

$$
\mathrm{UCB}(a) = Q(a) + c \sqrt{\frac{\log t}{N(a)}}
$$

## Minimal Code Mental Model

```python
q[a] = incremental_mean(q[a], n[a], reward)
probs = epsilon_greedy_probs(q, epsilon=0.1)
scores = ucb_scores(q, total_steps=t, pull_counts=n, c=2.0)
```

## Function

```python
def incremental_mean(estimate: float, pull_count: int, reward: float) -> float:
def epsilon_greedy_probs(action_values: list[float], epsilon: float) -> list[float]:
def ucb_scores(action_values: list[float], total_steps: int, pull_counts: list[int], c: float = 1.0) -> list[float]:
```

## When To Use What

- Use the incremental mean update when rewards arrive one pull at a time.
- Use epsilon-greedy when you want the simplest exploration baseline.
- Use UCB when you want optimism to depend on how uncertain each arm still is.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/bandit-exploration-methods/python -q
```
