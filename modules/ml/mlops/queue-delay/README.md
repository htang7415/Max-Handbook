# Queue Delay

> Track: `ml` | Topic: `mlops`

## Concept

Queue delay measures how long a request waits after arrival before service actually starts.

## Math

$$
d_i = s_i - a_i
$$

$$
\bar{d} = \frac{1}{N} \sum_{i=1}^{N} d_i
$$

- $a_i$ -- enqueue or arrival time for request $i$
- $s_i$ -- service start time for request $i$

## Key Points

- Queue delay isolates waiting time from actual service time.
- It is a leading indicator for overload before total latency fully degrades.
- This module returns per-request delays and the mean queue delay.

## Function

```python
def queue_delay(enqueued_at: list[float], started_at: list[float]) -> tuple[list[float], float]:
```

## Run tests

```bash
pytest modules/ml/mlops/queue-delay/python -q
```
