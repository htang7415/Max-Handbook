# Capacity Breach Rate

> Track: `ml` | Topic: `mlops`

## Concept

Capacity breach rate measures how often observed load rises above a hard capacity limit.

## Math

$$
\mathrm{CapacityBreachRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[x_i > C]}{N}
$$

- $x_i$ -- observed load or utilization at time step $i$
- $C$ -- hard capacity limit

## Key Points

- This metric highlights direct capacity violations rather than soft saturation.
- It complements queue and utilization metrics in serving systems.
- This module returns both the breach count and the breach fraction.

## Function

```python
def capacity_breach_rate(observations: list[float], capacity: float) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/capacity-breach-rate/python -q
```
