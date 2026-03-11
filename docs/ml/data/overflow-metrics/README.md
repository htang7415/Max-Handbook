# Overflow Metrics

Overflow metrics describe what happens when examples exceed a hard token or length budget.

## Purpose

Use this guide to choose the right overflow summary when a hard budget exists:
- whether overflow happens at all
- how severe the average overrun is
- how bad the tail is
- whether a product threshold defines failure

## First Principles

- Overflow is a product constraint problem, not just a data-summary problem.
- Incidence and severity answer different questions and should not be collapsed into one number too early.
- Tail cases matter because a few severe overruns can drive most quality loss.
- Thresholded metrics matter when the product defines a clear unacceptable overrun level.

## Core Math

- Per-example overflow:
  $$
  o_i = \max(0, \ell_i - B)
  $$
- Truncation rate:
  $$
  \frac{\#\{i : o_i > 0\}}{N}
  $$
- Normalized overrun share:
  $$
  \frac{1}{N}\sum_i \frac{o_i}{B}
  $$

## Minimal Code Mental Model

```python
overflows = [max(0, length - budget) for length in lengths]
rate = truncation_rate(lengths, budget)
share = budget_overrun_share(lengths, budget)
tail = overflow_quantile(lengths, budget, q=0.95)
```

## Canonical Modules

- Family module: `overflow-metrics`

## When To Use What

- Start with `overflow-metrics` before looking at narrower overflow summaries.
- Use truncation rate for the first dashboard number.
- Use budget overrun share for normalized cross-dataset comparison.
- Use quantiles and tail metrics when a small number of severe overruns drive quality regressions.
- Use cutoff metrics when a product policy defines a hard failure threshold.
