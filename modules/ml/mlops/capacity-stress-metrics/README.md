# Capacity Stress Metrics

> Track: `ml` | Topic: `mlops`

## Concept

Capacity-stress metrics summarize whether a serving system is comfortably below
its limit, frequently breaching it, or concentrating failures in a severe tail.

## Math

- Breach rate:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[x_i > C]
  $$
- Overload margin:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\max(0, x_i - C)
  $$
- Pressure score:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[x_i > C]\left(1 + \frac{x_i - C}{C}\right)
  $$

- $x_i$ -- observed load
- $C$ -- capacity target

## Key Points

- Start with breach rate to know whether capacity is routinely violated.
- Headroom gap explains whether the system is comfortably below the ceiling even
  when there is no breach.
- Pressure and overload margin separate mild overflow from severe overflow.
- Bucket metrics are useful only after the simple summaries already say the
  system is under stress.

## Function

```python
def capacity_breach_rate(observations: list[float], capacity: float) -> tuple[int, float]:
def headroom_gap(observations: list[float], ceiling: float) -> tuple[list[float], float]:
def overload_margin(observations: list[float], capacity: float) -> float:
def pressure_score(observations: list[float], capacity: float) -> float:
def surge_pressure(observations: list[float], capacity: float) -> float:
def breach_bucket_share(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
def breach_bucket_entropy(observations: list[float], capacity: float, cutoffs: list[float]) -> float:
def breach_bucket_slope(observations: list[float], capacity: float, cutoffs: list[float]) -> float:
def breach_bucket_tail(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
    tail_buckets: int = 1,
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/capacity-stress-metrics/python -q
```
