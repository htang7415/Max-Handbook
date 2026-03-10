# Uncertainty Intervals

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module to understand which interval estimate fits which statistic.

## First Principles

- A point estimate without uncertainty is usually incomplete.
- Mean-style confidence intervals work when normal approximations are reasonable.
- Bootstrap intervals work when you can resample the statistic directly.
- Wilson intervals are a strong default for binary rates, especially with small counts.

## Core Math

- Mean interval:
  $$
  \bar{x} \pm z \frac{s}{\sqrt{n}}
  $$
- Bootstrap percentile interval:
  $$
  [\hat{\theta}_{\alpha/2}, \hat{\theta}_{1-\alpha/2}]
  $$
- Wilson center:
  $$
  \hat{p}_W = \frac{\hat{p} + z^2/(2n)}{1 + z^2/n}
  $$

## From Math To Code

- Compute the sample mean and standard error first for mean intervals.
- Use percentile extraction directly for bootstrap intervals.
- Switch to Wilson when the statistic is a binary rate, not a mean.

## Minimal Code Mental Model

```python
mean, std = sample_mean_and_std(samples)
se = standard_error(samples)
mean_ci = mean_confidence_interval(samples)
boot_ci = bootstrap_percentile_interval(bootstrap_statistics)
wilson_ci = wilson_interval(successes, trials)
```

## Function

```python
def sample_mean_and_std(samples: list[float]) -> tuple[float, float]:
def standard_error(samples: list[float]) -> float:
def mean_confidence_interval(samples: list[float], z: float = 1.96) -> tuple[float, float]:
def bootstrap_percentile_interval(bootstrap_statistics: list[float], alpha: float = 0.05) -> tuple[float, float]:
def wilson_interval(successes: int, trials: int, z: float = 1.96) -> tuple[float, float]:
```

## When To Use What

- Use mean confidence intervals for simple approximately normal statistics.
- Use bootstrap intervals when the estimator is awkward but easy to resample.
- Use Wilson intervals for Bernoulli or binomial proportions.
- Match the interval type to the statistic instead of reusing one interval everywhere.

## Run tests

```bash
pytest modules/ml/evaluation/uncertainty-intervals/python -q
```
