# Batch Fill Rate

> Track: `ml` | Topic: `mlops`

## Concept

Batch fill rate measures how full serving batches are relative to their configured maximum size.

## Math

$$
\mathrm{fill\_rate} = \frac{\mathrm{avg\_batch\_size}}{\mathrm{max\_batch\_size}}
$$

- $\mathrm{avg\_batch\_size}$ -- average number of requests per batch
- $\mathrm{max\_batch\_size}$ -- configured batch capacity

## Key Points

- Higher fill rate means the system is using batching capacity more efficiently.
- Low fill rate can indicate fragmentation or underutilization.
- This complements latency and queue metrics in serving systems.

## Function

```python
def batch_fill_rate(batch_sizes: list[int], max_batch_size: int) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/batch-fill-rate/python -q
```
