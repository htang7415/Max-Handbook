# Robust Scaling

> Track: `ml` | Topic: `data`

## Concept

Robust scaling centers features by the median and scales them by the interquartile range, which makes it less sensitive to outliers than z-score normalization.

## Math

$$r_i = \frac{x_i - \mathrm{median}(x)}{\mathrm{IQR}(x)}$$

$$\mathrm{IQR}(x) = Q_{0.75}(x) - Q_{0.25}(x)$$

- $x_i$ -- original value
- $Q_{0.25}, Q_{0.75}$ -- first and third quartiles
- $\mathrm{IQR}$ -- interquartile range

## Key Points

- Robust scaling is often safer than z-scoring when heavy outliers exist.
- Median and IQR are more stable than mean and standard deviation under contamination.
- If the IQR is zero, the feature has no robust spread to scale by.

## Function

```python
def robust_scale(values: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/data/robust-scaling/python -q
```
