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

- Precision, recall, and F1:
  $$
  P = \frac{TP}{TP + FP}, \quad R = \frac{TP}{TP + FN}, \quad F1 = \frac{2PR}{P + R}
  $$
- Log loss:
  $$
  -\frac{1}{N}\sum_{i=1}^{N} y_i \log p_i + (1-y_i)\log(1-p_i)
  $$
- Brier score:
  $$
  \frac{1}{N}\sum_{i=1}^{N}(p_i - y_i)^2
  $$
- Reciprocal rank:
  $$
  \mathrm{RR} = \frac{1}{\mathrm{rank\ of\ first\ relevant\ item}}
  $$
- Confidence interval shape:
  $$
  \mathrm{estimate} \pm z \cdot \mathrm{SE}
  $$

## Minimal Code Mental Model

```python
classification = f1_score(y_true, y_pred)
ranking = mean_reciprocal_rank(relevance_lists)
calibration = brier_score(probabilities, labels)
interval = bootstrap_interval(metric_values)
experiment = ab_test_analysis(control, treatment)
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

- Use classification metrics when decisions are discrete.
- Use ranking metrics when order matters more than the raw score.
- Use calibration metrics when probabilities drive thresholds, routing, or review.
- Use uncertainty intervals when the estimate itself has sampling noise.
- Use statistical tests when comparing systems, experiments, or models.
