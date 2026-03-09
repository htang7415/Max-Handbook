# Queue Age Percentiles

> Track: `ml` | Topic: `mlops`

## Concept

Queue age percentiles summarize how long requests have been waiting in the queue, with p50 and p95 capturing typical and tail backlog.

## Math

For sorted queue ages $a_{(1)} \le \dots \le a_{(N)}$, this module uses linear interpolation for percentile $q$:

$$
\mathrm{Percentile}(q)
$$

at position $(N-1)q$ in the sorted list.

## Key Points

- Queue age is a backlog signal even before total latency is measured.
- p95 highlights tail waiting better than a simple mean.
- This module returns p50 and p95 from one batch of queue ages.

## Function

```python
def queue_age_percentiles(queue_ages: list[float]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/queue-age-percentiles/python -q
```
