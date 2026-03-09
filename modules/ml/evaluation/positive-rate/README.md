# Positive Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Positive rate measures the prevalence of the positive class in a binary label set.

## Math

$$
\mathrm{PositiveRate} = \frac{\sum_{i=1}^{N} y_i}{N}
$$

- $y_i \in \{0, 1\}$ -- binary label for example $i$

## Key Points

- Positive rate is the base-rate baseline for binary problems.
- It helps interpret lift, precision, and class imbalance.
- This module expects binary labels only.

## Function

```python
def positive_rate(labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/positive-rate/python -q
```
