# Drift Detection

> Track: `ml` | Topic: `mlops`

## Concept

Drift detection compares a reference distribution with a current distribution and asks whether the shape has moved enough to trigger investigation.

## Math

$$
D_{KS} = \max_x \left| F_{ref}(x) - F_{cur}(x) \right|
$$

- $F_{ref}$ -- empirical CDF of the reference sample
- $F_{cur}$ -- empirical CDF of the current sample
- $D_{KS}$ -- Kolmogorov-Smirnov drift score

## Key Points

- KS-style drift detection is nonparametric and shape-aware.
- It complements bucketed PSI by comparing empirical CDFs directly.
- This module exposes both the drift score and a thresholded alert.

## Function

```python
def ks_drift_score(reference: list[float], current: list[float]) -> float:
def drift_detected(reference: list[float], current: list[float], threshold: float = 0.2) -> bool:
```

## Run tests

```bash
pytest modules/ml/mlops/drift-detection/python -q
```
