# Overload Duration Share

> Track: `ml` | Topic: `mlops`

## Concept

Overload duration share measures the fraction of observations spent above an overload threshold.

## Math

$$
\mathrm{OverloadDurationShare} = \frac{\sum_{i=1}^{N} \mathbf{1}[x_i > \tau]}{N}
$$

- $x_i$ -- observed load or utilization at time step $i$
- $\tau$ -- overload threshold

## Key Points

- This metric captures the time share of overload, not the overload magnitude.
- It complements overload margin and capacity-breach rate.
- This module returns a single share in `[0, 1]`.

## Function

```python
def overload_duration_share(observations: list[float], threshold: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/overload-duration-share/python -q
```
