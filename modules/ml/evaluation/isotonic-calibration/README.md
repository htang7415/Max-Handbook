# Isotonic Calibration

> Track: `ml` | Topic: `evaluation`

## Concept

Isotonic calibration fits a monotonic mapping from model scores to probabilities using the pool-adjacent-violators algorithm.

## Math

$$\hat{p}_1 \le \hat{p}_2 \le \cdots \le \hat{p}_n$$

$$\hat{p}_{B} = \frac{1}{|B|} \sum_{i \in B} y_i$$

- $\hat{p}_i$ -- calibrated probability for sorted example $i$
- $B$ -- a pooled block of adjacent examples
- $y_i$ -- binary label for example $i$

## Key Points

- Isotonic regression is flexible because it does not assume a parametric sigmoid shape.
- The fitted probabilities must be non-decreasing with the input score.
- This module returns calibrated values aligned with the original example order.

## Function

```python
def isotonic_calibration(scores: list[float], labels: list[int]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/evaluation/isotonic-calibration/python -q
```
