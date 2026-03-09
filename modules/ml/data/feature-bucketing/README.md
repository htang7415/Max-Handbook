# Feature Bucketing

> Track: `ml` | Topic: `data`

## Concept

Feature bucketing converts continuous values into discrete bins based on ordered boundaries.

## Math

$$
\mathrm{bucket}(x) = \min \{ i : x < b_i \}
$$

- $x$ -- numeric feature value
- $b_i$ -- bucket boundary

## Key Points

- Bucketing can make nonlinear thresholds easier for simple models to use.
- It is common in ranking, ads, and tabular preprocessing.
- This module returns bucket indices directly.

## Function

```python
def bucketize(values: list[float], boundaries: list[float]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/data/feature-bucketing/python -q
```
