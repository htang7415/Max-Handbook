# Prevalence Index

> Track: `ml` | Topic: `evaluation`

## Concept

Prevalence index normalizes a group's positive rate relative to a baseline positive rate.

## Math

$$
\mathrm{PrevalenceIndex} = \frac{p}{p_0}
$$

- $p$ -- positive rate of the evaluated group
- $p_0$ -- baseline positive rate

## Key Points

- A value above 1 means the evaluated group has higher prevalence than baseline.
- This is a direct baseline-normalized prevalence score.
- This module treats a zero baseline as infinite when the evaluated rate is positive.

## Function

```python
def prevalence_index(labels: list[int], baseline_rate: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/prevalence-index/python -q
```
