# Value Normalization

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Value normalization rescales critic targets so the value head does not have to chase unstable reward magnitudes directly.

## Math

$$
\tilde{V}_i = \frac{V_i - \mu_V}{\sigma_V + \epsilon}
$$

- $V_i$ -- raw value target
- $\mu_V$ -- batch mean of value targets
- $\sigma_V$ -- batch standard deviation
- $\epsilon$ -- numerical stabilizer

## Key Points

- This is similar in spirit to advantage normalization but targets the critic scale.
- Returning the normalization statistics makes later denormalization possible.
- The module focuses on a batch transformation, not running-stat tracking across training.

## Function

```python
def normalize_value_targets(values: list[float], eps: float = 1.0e-8) -> tuple[list[float], float, float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/value-normalization/python -q
```
