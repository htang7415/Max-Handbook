# Overflow Tail

> Track: `ml` | Topic: `data`

## Concept

Overflow tail summarizes the upper end of overflow severity using a percentile of per-example overflow amounts.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$, this module reports a chosen upper-tail percentile of $\{o_i\}$.

## Key Points

- This complements mean overflow and overflow count by focusing on severe cases.
- Including zero-overflow examples keeps the percentile tied to batch composition.
- This module uses linear interpolation on sorted overflow amounts.

## Function

```python
def overflow_tail(lengths: list[int], max_length: int, quantile: float = 0.95) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-tail/python -q
```
