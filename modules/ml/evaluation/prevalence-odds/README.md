# Prevalence Odds

> Track: `ml` | Topic: `evaluation`

## Concept

Prevalence odds expresses a binary positive rate in odds form instead of probability form.

## Math

$$
\mathrm{Odds} = \frac{p}{1 - p}
$$

- $p$ -- positive rate

## Key Points

- Odds become large when the positive class dominates.
- This is useful when switching between probability and log-odds views.
- This module computes odds from one binary label set.

## Function

```python
def prevalence_odds(labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/prevalence-odds/python -q
```
