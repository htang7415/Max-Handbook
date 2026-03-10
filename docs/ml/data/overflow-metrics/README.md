# Overflow Metrics

Overflow metrics describe what happens when examples exceed a hard token or length budget.

## Metric Families

- Incidence metrics: truncation rate, overflow count, overflow presence rate
- Mean severity metrics: mean overflow, budget overrun share, overflow density
- Distribution metrics: overflow quantile, peak, spread, Gini
- Thresholded metrics: overflow threshold rate and count
- Unacceptable-case metrics: overflow cutoff mean, median, IQR, range, skew
- Upper-tail metrics: cutoff upper tail, tail mass, tail Gini, tail mean, tail variance

## How to Use Them

- Start with incidence metrics to see whether the cap is a routine event or a rare edge case.
- Use mean severity metrics when comparing datasets or prompting strategies.
- Use distribution metrics when a single average hides a few severe failures.
- Use cutoff metrics when only overflow above a policy threshold should count.
- Use upper-tail metrics when the most severe truncation cases drive quality regressions.

## Good Defaults

- Start with the canonical module `overflow-metrics`
- Use `truncation_rate` for the first dashboard number
- Use `budget_overrun_share` for normalized cross-dataset comparisons
- Use `overflow_quantile` for worst-case visibility
- Use `overflow_cutoff_rate` plus `overflow_cutoff_tail_mass` when a product threshold defines failure
