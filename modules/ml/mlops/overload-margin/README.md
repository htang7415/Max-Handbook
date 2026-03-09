# Overload Margin

> Track: `ml` | Topic: `mlops`

## Concept

Overload margin measures the average amount by which observed load exceeds a hard capacity, ignoring observations below the limit.

## Math

$$
\mathrm{OverloadMargin} = \frac{1}{N} \sum_{i=1}^{N} \max(0, x_i - C)
$$

- $x_i$ -- observed load or utilization at time step $i$
- $C$ -- hard capacity limit

## Key Points

- This metric captures overload severity, not just breach incidence.
- It complements capacity-breach rate and utilization-gap metrics.
- This module averages only the positive margin contribution per observation.

## Function

```python
def overload_margin(observations: list[float], capacity: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/overload-margin/python -q
```
