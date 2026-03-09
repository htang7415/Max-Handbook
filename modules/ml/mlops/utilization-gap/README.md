# Utilization Gap

> Track: `ml` | Topic: `mlops`

## Concept

Utilization gap measures how far observed utilization sits above or below a target level.

## Math

$$
g_i = u_i - t
$$

$$
\bar{g} = \frac{1}{N} \sum_{i=1}^{N} g_i
$$

- $u_i$ -- observed utilization at time step $i$
- $t$ -- target utilization

## Key Points

- Positive gaps indicate overload relative to the target.
- Negative gaps indicate unused headroom relative to the target.
- This module returns per-observation gaps and the mean gap.

## Function

```python
def utilization_gap(utilizations: list[float], target: float) -> tuple[list[float], float]:
```

## Run tests

```bash
pytest modules/ml/mlops/utilization-gap/python -q
```
