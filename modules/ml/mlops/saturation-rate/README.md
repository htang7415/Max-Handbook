# Saturation Rate

> Track: `ml` | Topic: `mlops`

## Concept

Saturation rate measures how often a system runs at or above a configured full-capacity utilization threshold.

## Math

$$
\mathrm{SaturationRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[u_i \ge \tau]}{N}
$$

- $u_i$ -- observed utilization at time step $i$
- $\tau$ -- saturation threshold

## Key Points

- Saturation rate is a coarse overload signal for serving systems.
- It complements queue and latency metrics by focusing on capacity pressure.
- This module returns both the saturated count and the fraction.

## Function

```python
def saturation_rate(utilizations: list[float], threshold: float = 1.0) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/saturation-rate/python -q
```
