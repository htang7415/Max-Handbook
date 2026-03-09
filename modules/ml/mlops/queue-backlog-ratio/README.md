# Queue Backlog Ratio

> Track: `ml` | Topic: `mlops`

## Concept

Queue backlog ratio compares observed queue age to a service target so backlog can be interpreted in normalized units.

## Math

$$
\mathrm{BacklogRatio} = \frac{a}{t}
$$

- $a$ -- observed queue age
- $t$ -- queue-age or service target

## Key Points

- A ratio above 1 means requests are waiting longer than the target.
- Ratios make queue health easier to compare across systems with different SLAs.
- This module returns one ratio per observation plus the mean ratio.

## Function

```python
def queue_backlog_ratio(queue_ages: list[float], target_age: float) -> tuple[list[float], float]:
```

## Run tests

```bash
pytest modules/ml/mlops/queue-backlog-ratio/python -q
```
