# Overflow Spread

> Track: `ml` | Topic: `data`

## Concept

Overflow spread measures the distance between a lower and upper overflow quantile.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$:

$$
\mathrm{Spread} = Q_{q_h}(o) - Q_{q_l}(o)
$$

- $Q_{q_h}$ -- upper overflow quantile
- $Q_{q_l}$ -- lower overflow quantile

## Key Points

- This metric captures how dispersed overflow severity is across a batch.
- It complements mean overflow and overflow peak.
- This module uses linear interpolation for both quantiles.

## Function

```python
def overflow_spread(
    lengths: list[int],
    max_length: int,
    low_quantile: float = 0.5,
    high_quantile: float = 0.95,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-spread/python -q
```
