# Base Rate Gap

> Track: `ml` | Topic: `evaluation`

## Concept

Base-rate gap measures the difference between two binary positive rates.

## Math

$$
\mathrm{Gap} = p_A - p_B
$$

- $p_A$ -- positive rate of group A
- $p_B$ -- positive rate of group B

## Key Points

- Base-rate gaps are useful when comparing cohorts, slices, or train/test shifts.
- The sign tells you which group has the higher prevalence.
- This module computes the signed difference between two binary label sets.

## Function

```python
def base_rate_gap(group_a: list[int], group_b: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/base-rate-gap/python -q
```
