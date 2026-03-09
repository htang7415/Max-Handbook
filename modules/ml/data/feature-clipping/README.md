# Feature Clipping

> Track: `ml` | Topic: `data`

## Concept

Feature clipping caps numeric features to a fixed interval so rare extreme values cannot dominate downstream models.

## Math

$$
\tilde{x}_i = \min(\max(x_i, L), U)
$$

- $x_i$ -- original feature value
- $L$ -- lower bound
- $U$ -- upper bound

## Key Points

- Clipping is a simple robustification step before linear models or trees.
- It is different from scaling because it changes only outliers beyond the bounds.
- This module applies the same numeric bounds to a list of values.

## Function

```python
def clip_features(values: list[float], min_value: float, max_value: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/data/feature-clipping/python -q
```
