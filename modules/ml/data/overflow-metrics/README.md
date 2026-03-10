# Overflow Metrics

> Track: `ml` | Topic: `data`

## Concept

Overflow metrics summarize what happens when examples exceed a hard token or
length budget. The main questions are: how often does overflow happen, how big
is it, and how bad is the tail after a product cutoff.

## Math

- Overflow amount:
  $$
  o_i = \max(0, \ell_i - L)
  $$
- Truncation rate:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[o_i > 0]
  $$
- Overrun share:
  $$
  \frac{\sum_i o_i}{\sum_i \ell_i}
  $$
- Cutoff rate:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[o_i \ge c]
  $$

- $\ell_i$ -- sequence length
- $L$ -- allowed budget
- $o_i$ -- overflow amount
- $c$ -- product cutoff for unacceptable overflow

## Key Points

- Start with truncation rate to see whether the budget is routinely violated.
- Overrun share normalizes overflow by total traffic, so it compares datasets
  better than a raw count.
- Quantiles show whether a small number of examples cause most of the damage.
- Cutoff metrics matter when a product treats only large overflow as failure.

## Function

```python
def truncation_rate(lengths: list[int], max_length: int) -> tuple[int, float]:
def budget_overrun_share(lengths: list[int], max_length: int) -> float:
def overflow_quantile(lengths: list[int], max_length: int, quantile: float) -> float:
def overflow_cutoff_rate(lengths: list[int], max_length: int, cutoff: int) -> float:
def overflow_cutoff_tail_mass(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-metrics/python -q
```
