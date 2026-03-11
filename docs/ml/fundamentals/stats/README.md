# Statistics for ML

Statistics turns noisy observations into estimates, intervals, and decisions.

## Purpose

Use this guide to connect noisy measurements to decisions:
- summary behavior
- uncertainty intervals
- comparison tests
- action thresholds

## First Principles

- Statistics matters when you need to decide whether observed metric movement is real enough to act on.
- Summary statistics compress data, but intervals and tests tell you how uncertain that summary is.
- Hypothesis tests are useful only when they change a product, experiment, or deployment decision.
- Robust decisions come from matching uncertainty estimates to the real question, not from blindly applying a test.

## Core Math

- Sample mean:
  $$
  \hat{\mu} = \frac{1}{n}\sum_i x_i
  $$
- Covariance:
  $$
  \mathrm{Cov}(X, Y) = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)]
  $$
- Two-sample t-statistic:
  $$
  t = \frac{\bar{x}_1 - \bar{x}_2}{\mathrm{SE}}
  $$

## Minimal Code Mental Model

```python
cov = covariance(x, y)
t_stat = two_sample_t_test(group_a, group_b)
posterior = beta_binomial_update(alpha, beta, successes, failures)
```

## Canonical Modules

- Summary structure: `covariance`
- Statistical comparison: `two-sample-t-test`
- Bayesian update intuition: `beta-binomial`

## When To Use What

- Start with `covariance` for dependency and summary behavior.
- Use `two-sample-t-test` when you need a small classical comparison example.
- Use `beta-binomial` when you want interval and update intuition in one concrete setting.
- Move to the evaluation section when the real question becomes metric choice rather than statistical machinery.
