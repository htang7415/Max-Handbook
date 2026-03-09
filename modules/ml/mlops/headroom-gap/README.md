# Headroom Gap

> Track: `ml` | Topic: `mlops`

## Concept

Headroom gap measures how far observed load sits below or above a target ceiling.

## Math

$$
h_i = c - x_i
$$

$$
\bar{h} = \frac{1}{N} \sum_{i=1}^{N} h_i
$$

- $c$ -- target ceiling or capacity limit
- $x_i$ -- observed load at time step $i$

## Key Points

- Positive values mean spare headroom remains.
- Negative values mean the system is above the target ceiling.
- This module returns per-observation gaps and the mean gap.

## Function

```python
def headroom_gap(observations: list[float], ceiling: float) -> tuple[list[float], float]:
```

## Run tests

```bash
pytest modules/ml/mlops/headroom-gap/python -q
```
