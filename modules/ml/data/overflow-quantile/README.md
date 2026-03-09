# Overflow Quantile

> Track: `ml` | Topic: `data`

## Concept

Overflow quantile reports a configurable percentile of per-example overflow amounts beyond a hard length cap.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$, this module reports a quantile of $\{o_i\}$ using linear interpolation.

## Key Points

- This generalizes fixed overflow-tail summaries to any quantile.
- Including zero-overflow examples keeps the statistic tied to the full batch.
- This module is useful when different teams track different tail percentiles.

## Function

```python
def overflow_quantile(lengths: list[int], max_length: int, quantile: float) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-quantile/python -q
```
