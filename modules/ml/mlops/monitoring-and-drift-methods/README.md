# Monitoring and Drift Methods

> Track: `ml` | Topic: `mlops`

## Purpose

Use this module to learn the main ways production ML systems detect that inputs,
predictions, or raw data quality have shifted.

## First Principles

- Monitoring starts with a reference state and asks how far the live system moved away from it.
- Different failure classes need different summaries: missing-value checks, distribution drift, and output drift are not the same.
- PSI works on bucket proportions; KS drift works on empirical CDF shape.
- Prediction monitoring is often the fastest signal when labels arrive late.

## Core Math

PSI:

$$
\mathrm{PSI} = \sum_i (a_i - e_i)\log\frac{a_i}{e_i}
$$

KS drift:

$$
D_{KS} = \max_x \left| F_{ref}(x) - F_{cur}(x) \right|
$$

Mean prediction shift:

$$
\Delta \mu = |\mu_{\text{new}} - \mu_{\text{old}}|
$$

## From Math To Code

- Compare bucket proportions term by term before summing them into PSI.
- Treat KS drift as the largest gap between two empirical CDFs, not just a mean difference.
- Keep prediction shift separate from input drift because labels often arrive later.
- Start with the simplest health checks, like missing-rate, before moving to richer drift summaries.

## Minimal Code Mental Model

```python
terms = psi_terms(expected_bins, actual_bins)
population_shift = psi(expected_bins, actual_bins)
ks_score = ks_drift_score(reference, current)
prediction_shift = mean_shift(old_predictions, new_predictions)
null_fraction = missing_rate(values)
```

## Functions

```python
def psi_terms(expected: list[float], actual: list[float]) -> list[float]:
def psi(expected: list[float], actual: list[float]) -> float:
def ks_drift_score(reference: list[float], current: list[float]) -> float:
def drift_detected(reference: list[float], current: list[float], threshold: float = 0.2) -> bool:
def mean_shift(old: list[float], new: list[float]) -> float:
def missing_rate(values: list[float | None]) -> float:
```

## When To Use What

- Use PSI when data is already bucketed and you want a simple distribution-drift summary.
- Use KS drift when you want a shape-aware nonparametric comparison of continuous values.
- Use prediction mean shift when you need a lightweight online output monitor.
- Use missing-rate checks when upstream data quality is the primary operational risk.

## Run tests

```bash
pytest modules/ml/mlops/monitoring-and-drift-methods/python -q
```
