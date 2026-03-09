# A/B Test Analysis

> Track: `ml` | Topic: `evaluation`

## Concept

A/B test analysis goes beyond raw conversion rates and asks whether the observed lift is statistically distinguishable from noise.

## Math

$$
z = \frac{\hat{p}_B - \hat{p}_A}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_A} + \frac{1}{n_B}\right)}}
$$

- $\hat{p}_A, \hat{p}_B$ -- observed conversion rates
- $\hat{p}$ -- pooled conversion rate
- $n_A, n_B$ -- sample sizes

## Key Points

- Conversion lift alone is not enough; uncertainty matters.
- A two-sided normal approximation is a common baseline for large samples.
- This module returns the rates, relative lift, z-score, and p-value together.

## Function

```python
def ab_test_analysis(
    control_conversions: int,
    control_trials: int,
    treatment_conversions: int,
    treatment_trials: int,
) -> ABTestResult:
```

## Run tests

```bash
pytest modules/ml/evaluation/ab-test-analysis/python -q
```
