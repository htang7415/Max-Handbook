# Request SLA Compliance

> Track: `ml` | Topic: `mlops`

## Concept

Request-level SLA compliance measures what fraction of requests finish within a latency target.

## Math

$$\mathrm{compliance} = \frac{\#\{t_i \le \tau\}}{N}$$

- $t_i$ -- latency of request $i$
- $\tau$ -- SLA threshold
- $N$ -- total number of requests

## Key Points

- SLA compliance is easier to reason about than raw average latency alone.
- A small number of slow tail requests can break an otherwise fast service.
- This module focuses on a single threshold, not multi-SLO dashboards.

## Function

```python
def request_sla_compliance(
    latencies_ms: list[float],
    sla_ms: float,
) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/request-sla/python -q
```
