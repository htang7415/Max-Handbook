# Uncertainty

Uncertainty is useful only when it changes a decision, threshold, or deployment policy.

## Purpose

Use this guide to route uncertainty questions into the right family:
- interval estimates
- bootstrap-based uncertainty
- binomial proportion intervals
- uncertainty in predicted probabilities

## First Principles

- Statistical uncertainty asks how noisy an estimate is.
- Predictive uncertainty asks whether the model should trust its own probabilities.
- Intervals matter only when they can change a launch, routing, or review decision.
- Overconfident probabilities are dangerous even when average accuracy looks acceptable.

## Core Math

- Confidence interval template:
  $$
  \hat{\theta} \pm z \cdot \mathrm{SE}(\hat{\theta})
  $$
- Wilson interval and bootstrap intervals are practical alternatives when normal approximations are weak or awkward.

## Minimal Code Mental Model

```python
lo, hi = confidence_interval(samples)
boot = bootstrap_interval(samples, q=0.95)
wilson = wilson_interval(successes, total, q=0.95)
```

## Canonical Modules

- Family module: `uncertainty-intervals`

## Supporting Modules

- `confidence-intervals`
- `bootstrap-intervals`
- `wilson-interval`

## When To Use What

- Start with `uncertainty-intervals` for the family overview.
- Use confidence intervals for the standard analytic case.
- Use bootstrap intervals when the estimator is awkward or distributional assumptions are weak.
- Use Wilson intervals for binomial-rate summaries with limited samples.
- Switch to calibration modules when the real problem is probability quality rather than estimate uncertainty.
