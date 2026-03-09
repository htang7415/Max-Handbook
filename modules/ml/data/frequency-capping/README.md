# Frequency Capping

> Track: `ml` | Topic: `data`

## Concept

Frequency capping clips very common sparse-feature counts so a single repeated token or event does not dominate a linear model.

## Math

$$
\tilde{c}_i = \min(c_i, C)
$$

- $c_i$ -- original count for feature $i$
- $C$ -- maximum retained count

## Key Points

- Count capping is a simple alternative to log transforms for sparse counts.
- It preserves presence information while reducing the impact of extreme repetition.
- This module applies a fixed cap to a feature-count mapping.

## Function

```python
def cap_frequencies(feature_counts: dict[str, int], max_count: int) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/ml/data/frequency-capping/python -q
```
