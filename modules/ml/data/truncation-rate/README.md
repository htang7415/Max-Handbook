# Truncation Rate

> Track: `ml` | Topic: `data`

## Concept

Truncation rate measures how often examples exceed a hard length cap and therefore lose information during preprocessing.

## Math

$$
\mathrm{TruncationRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[l_i > L]}{N}
$$

- $l_i$ -- original length of example $i$
- $L$ -- maximum allowed length

## Key Points

- Truncation rate is a quick diagnostic for whether a token budget is too small.
- It complements token budgeting by tracking how often clipping happens.
- This module returns both the truncated count and the rate.

## Function

```python
def truncation_rate(lengths: list[int], max_length: int) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/data/truncation-rate/python -q
```
