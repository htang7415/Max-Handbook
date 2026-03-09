# Overflow Count

> Track: `ml` | Topic: `data`

## Concept

Overflow count measures how many total units exceed a hard length budget across a batch of examples.

## Math

$$
\mathrm{OverflowCount} = \sum_{i=1}^{N} \max(0, l_i - L)
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length

## Key Points

- Overflow count tracks total lost budget, not just whether truncation happened.
- It complements truncation rate when you need severity rather than incidence.
- This module sums overflow beyond one fixed cap.

## Function

```python
def overflow_count(lengths: list[int], max_length: int) -> int:
```

## Run tests

```bash
pytest modules/ml/data/overflow-count/python -q
```
