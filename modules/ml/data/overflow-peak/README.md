# Overflow Peak

> Track: `ml` | Topic: `data`

## Concept

Overflow peak measures the maximum overflow amount beyond a hard length cap within a batch.

## Math

$$
\mathrm{OverflowPeak} = \max_i \max(0, l_i - L)
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length

## Key Points

- This metric highlights the single worst truncation case.
- It complements mean overflow and overflow quantiles.
- This module returns zero when nothing overflows.

## Function

```python
def overflow_peak(lengths: list[int], max_length: int) -> int:
```

## Run tests

```bash
pytest modules/ml/data/overflow-peak/python -q
```
