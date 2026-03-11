# Calibration

Calibration asks whether model confidence matches empirical correctness.

## Purpose

Use this guide to keep probability quality separate from ranking or threshold quality:
- confidence versus accuracy
- calibration summaries
- post-hoc calibration
- neighboring classification metrics

## First Principles

- A model can rank examples well and still assign bad probabilities.
- Calibration is about probability quality, not label accuracy alone.
- Reliability diagrams and ECE summarize mismatch between confidence and correctness.
- Post-hoc calibration changes probability outputs without changing the base representation.

## Core Math

- Expected calibration error:
  $$
  \mathrm{ECE} = \sum_b \frac{n_b}{N}\lvert \mathrm{acc}(b) - \mathrm{conf}(b) \rvert
  $$
- Brier score:
  $$
  \frac{1}{N}\sum_i (\hat{p}_i - y_i)^2
  $$

## Minimal Code Mental Model

```python
ece = expected_calibration_error(probs, labels, bins=10)
brier = brier_score(probs, labels)
calibrated = isotonic_calibration(scores, labels)
```

## Canonical Modules

- Family module: `calibration-metrics`

## Supporting Modules

- `expected-calibration-error`
- `brier-score`
- `isotonic-calibration`

## When To Use What

- Start with `calibration-metrics` for the family overview.
- Use ECE when you need a compact reliability summary.
- Use Brier score when a probability-sensitive loss summary is enough.
- Use isotonic calibration when you need a monotonic post-hoc fix.
- Use ROC-AUC or precision/recall only when ranking or threshold behavior is the main question instead of probability quality.
