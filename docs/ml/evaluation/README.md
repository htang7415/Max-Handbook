# Metrics and Evaluation

Metrics only matter when they match the question you actually care about.

## Purpose

Use this page to choose the right evaluation frame:
- classification and ranking quality
- probability quality and uncertainty
- experiment validity
- regression or clustering quality when those are the task

## First Principles

- `Classification metrics` ask whether the predicted labels are useful.
- `Ranking metrics` ask whether the right items appear early enough.
- `Calibration metrics` ask whether predicted probabilities are trustworthy.
- `Uncertainty intervals` ask how much sampling noise surrounds an estimate.
- `Statistical tests` ask whether an observed difference is likely real.

## Core Math

- Most evaluation math is one of four shapes:
  $$
  \text{count ratio}, \quad \text{proper loss}, \quad \text{rank score}, \quad \text{interval around an estimate}
  $$
- The exact definitions live in the canonical modules below.

## Minimal Code Mental Model

```python
metric = choose_metric(task, label_shape, probability_need)
score = evaluate(metric, predictions, labels)
```

## Canonical Modules

- Classification: `classification-metrics-core`, `agreement-metrics`, `binary-rate-comparison-metrics`
- Ranking: `ranking-metrics`
- Calibration: `calibration-metrics`
- Uncertainty: `uncertainty-intervals`
- Statistical testing: `permutation-test`, `ab-test-analysis`, `delong-test`, `bradley-terry-ranking`

## Supporting Modules

- Regression: `mae-vs-mse`, `r2-score`
- Clustering: `silhouette-score`, `davies-bouldin`, `calinski-harabasz`
- Uncertainty guide (`docs/ml/evaluation/uncertainty`)
- Calibration guide (`docs/ml/evaluation/calibration`)

## When To Use What

- Start with the task shape: classification, ranking, probability quality, or experiment comparison.
- Go to the canonical family module for the actual definition and code.
- Use this page mainly as the routing map, not the final metric reference.
