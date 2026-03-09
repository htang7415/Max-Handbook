# Overflow Presence Rate

> Track: `ml` | Topic: `data`

## Concept

Overflow presence rate measures how often examples exceed a hard length budget at all.

## Math

$$
\mathrm{OverflowPresenceRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[l_i > L]}{N}
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length

## Key Points

- This metric captures incidence, not severity.
- It complements mean overflow and overflow count.
- This module returns both the count of overflowing examples and the rate.

## Function

```python
def overflow_presence_rate(lengths: list[int], max_length: int) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/data/overflow-presence-rate/python -q
```
