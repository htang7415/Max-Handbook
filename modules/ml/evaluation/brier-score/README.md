# Brier Score

> Track: `ml` | Topic: `evaluation`

## Concept

The Brier score measures how close predicted probabilities are to binary outcomes, combining calibration and sharpness into one squared-error metric.

## Math

$$
\mathrm{Brier} = \frac{1}{n} \sum_{i=1}^{n} (p_i - y_i)^2
$$

- $p_i$ -- predicted probability of the positive class
- $y_i$ -- observed binary outcome
- $n$ -- number of examples

## Key Points

- Lower is better.
- Unlike accuracy, this metric rewards well-calibrated confidence.
- It is a natural companion to ECE and reliability diagrams.

## Function

```python
def brier_score(labels: list[int], probabilities: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/brier-score/python -q
```
