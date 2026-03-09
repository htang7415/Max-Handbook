# Sequential Testing

> Track: `ml` | Topic: `mlops`

## Concept

Sequential testing adjusts the significance threshold when an experiment is checked multiple times before the final horizon.

## Math

$$
\alpha_t = \alpha \frac{t}{T}
$$

- $\alpha$ -- total significance budget
- $t$ -- current look index
- $T$ -- total planned looks
- $\alpha_t$ -- cumulative alpha spent by look $t$

## Key Points

- Repeated peeking inflates false positives if the threshold never changes.
- Alpha-spending ideas tighten early looks and spend more budget later.
- This module uses a simple linear spending rule as a minimal teaching example.

## Function

```python
def sequential_test_decision(
    p_value: float,
    alpha: float,
    look_index: int,
    total_looks: int,
) -> tuple[float, bool]:
```

## Run tests

```bash
pytest modules/ml/mlops/sequential-testing/python -q
```
