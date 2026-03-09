# Mean Overflow

> Track: `ml` | Topic: `data`

## Concept

Mean overflow measures the average amount by which examples exceed a hard length budget.

## Math

$$
\mathrm{MeanOverflow} = \frac{1}{N} \sum_{i=1}^{N} \max(0, l_i - L)
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length

## Key Points

- This metric complements overflow count by normalizing per example.
- It is useful when comparing batches of different sizes.
- This module counts zero overflow for examples within the limit.

## Function

```python
def mean_overflow(lengths: list[int], max_length: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/mean-overflow/python -q
```
