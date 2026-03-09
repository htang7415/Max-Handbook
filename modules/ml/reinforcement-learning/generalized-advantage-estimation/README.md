# Generalized Advantage Estimation

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Generalized advantage estimation (GAE) smooths policy-gradient advantages by mixing one-step TD residuals across multiple future steps.

## Math

$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
$$

$$
A_t^{\mathrm{GAE}(\gamma,\lambda)} = \delta_t + \gamma \lambda A_{t+1}^{\mathrm{GAE}(\gamma,\lambda)}
$$

- $\delta_t$ -- TD residual at time $t$
- $V(s_t)$ -- critic value estimate
- $\gamma$ -- discount factor
- $\lambda$ -- bias-variance trade-off parameter

## Key Points

- `lambda = 0` gives raw one-step TD residuals.
- Larger `lambda` carries more long-horizon credit backward.
- GAE is a standard variance-reduction tool in PPO-style training.

## Function

```python
def generalized_advantages(
    rewards: list[float],
    values: list[float],
    gamma: float,
    lam: float,
    next_value: float = 0.0,
) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/generalized-advantage-estimation/python -q
```
