# Base Rate Ratio

> Track: `ml` | Topic: `evaluation`

## Concept

Base-rate ratio compares two binary positive rates multiplicatively.

## Math

$$
\mathrm{BaseRateRatio} = \frac{p_A}{p_B}
$$

- $p_A$ -- positive rate of group A
- $p_B$ -- positive rate of group B

## Key Points

- This is an alternative naming convention for prevalence ratio.
- Ratios above 1 mean group A has the higher positive rate.
- This module treats a zero denominator rate as infinite when the numerator rate is positive.

## Function

```python
def base_rate_ratio(group_a: list[int], group_b: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/base-rate-ratio/python -q
```
