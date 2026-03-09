# TD(lambda) Returns

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

TD(lambda) blends one-step bootstrapping with longer-horizon returns, trading variance against bias.

## Math

$$
G_t^\lambda = r_{t+1} + \gamma \left((1-\lambda)V(s_{t+1}) + \lambda G_{t+1}^\lambda \right)
$$

- $G_t^\lambda$ -- lambda-return at time $t$
- $r_{t+1}$ -- next reward
- $V(s_{t+1})$ -- bootstrap value of the next state
- $\gamma$ -- discount factor
- $\lambda$ -- return-mixing parameter

## Key Points

- `lambda = 0` reduces to one-step TD targets.
- `lambda = 1` reduces to Monte Carlo style returns over the observed horizon.
- This module computes lambda-returns, which pair naturally with eligibility traces.

## Function

```python
def td_lambda_returns(
    rewards: list[float],
    next_state_values: list[float],
    gamma: float,
    lam: float,
    terminal_value: float = 0.0,
) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/td-lambda/python -q
```
