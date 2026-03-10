# Calibration Metrics

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module to understand whether predicted probabilities can be trusted as
probabilities, not just as ranking scores.

## First Principles

- A calibrated model predicts `0.8` when roughly `80%` of those cases are truly positive.
- Ranking quality and calibration are different; a model can rank well and still be overconfident.
- Some tools measure miscalibration, while others actively recalibrate scores.
- In modern ML systems, calibration matters whenever probabilities drive thresholds, routing, or review.

## Core Math

- Expected calibration error:
  $$
  \mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n}\left|\mathrm{acc}(B_m)-\mathrm{conf}(B_m)\right|
  $$
- Brier score:
  $$
  \frac{1}{n}\sum_{i=1}^{n}(p_i-y_i)^2
  $$
- Isotonic calibration learns a monotonic mapping from score to probability.

## From Math To Code

- Put predictions into confidence bins first.
- Compare average confidence with average accuracy inside each bin.
- Aggregate those bin gaps into ECE.
- Use a monotonic remapping only when recalibration itself is the goal.

## Minimal Code Mental Model

```python
bins = calibration_bins(confidences, predictions, labels, num_bins=10)
ece = expected_calibration_error(confidences, predictions, labels)
score = brier_score(labels, probabilities)
calibrated = isotonic_calibration(scores, labels)
```

## Function

```python
def expected_calibration_error(
    confidences: list[float],
    predictions: list[int],
    labels: list[int],
    num_bins: int = 10,
) -> float:
def calibration_bins(
    confidences: list[float],
    predictions: list[int],
    labels: list[int],
    num_bins: int = 10,
) -> list[dict[str, float]]:
def brier_score(labels: list[int], probabilities: list[float]) -> float:
def isotonic_calibration(scores: list[float], labels: list[int]) -> list[float]:
```

## When To Use What

- Use ECE when you want a simple summary of confidence-vs-accuracy mismatch.
- Use Brier score when you want a proper scoring rule for binary probabilities.
- Use isotonic calibration when post-hoc monotonic recalibration is the main need.
- Do calibration work only on held-out calibration data, not the same data used to fit the model.

## Run tests

```bash
pytest modules/ml/evaluation/calibration-metrics/python -q
```
