# Prevalence Ratio

> Track: `ml` | Topic: `evaluation`

## Concept

Prevalence ratio compares two binary positive rates multiplicatively instead of subtracting them.

## Math

$$
\mathrm{PrevalenceRatio} = \frac{p_A}{p_B}
$$

- $p_A$ -- positive rate of group A
- $p_B$ -- positive rate of group B

## Key Points

- Ratios highlight relative differences between cohorts.
- A value above 1 means group A has the higher prevalence.
- This module treats an all-zero denominator rate as infinite when the numerator rate is positive.

## Function

```python
def prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/prevalence-ratio/python -q
```
