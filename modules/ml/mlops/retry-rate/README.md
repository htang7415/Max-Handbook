# Retry Rate

> Track: `ml` | Topic: `mlops`

## Concept

Retry rate measures how often requests need at least one retry instead of succeeding on the first attempt.

## Math

$$
\mathrm{RetryRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[r_i > 0]}{N}
$$

- $r_i$ -- retry count for request $i$
- $N$ -- total number of requests

## Key Points

- A rising retry rate often signals flaky dependencies or overload.
- It is complementary to SLA and error-budget metrics.
- This module counts how many requests required at least one retry.

## Function

```python
def retry_rate(retry_counts: list[int]) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/retry-rate/python -q
```
