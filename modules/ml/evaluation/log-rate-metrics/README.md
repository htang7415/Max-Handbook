# Log Rate Metrics

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module when several event metrics all reduce to the same idea:
take a binary event rate and view it on a log scale.

## First Principles

- A hit rate, miss rate, drop rate, timeout rate, or abort rate is still just:
  $$
  \text{event rate} = \frac{\text{event count}}{\text{total count}}
  $$
- The log transform does not create a new metric family. It only changes the scale:
  $$
  \log \text{event rate} = \log \left(\frac{c}{n}\right)
  $$
- This is most useful when the events are rare and you care about order-of-magnitude differences.

## Core Math

For any event count $c$ and total count $n$:
$$
\log \text{rate} = \log \left(\frac{c}{n}\right)
$$

- $c$ -- count of the event of interest
- $n$ -- total count

If $c = 0$, the log rate is negative infinity.

## Minimal Code Mental Model

```python
log_timeout = log_rate(timeout_count, total_count)
summary = log_rate_table({"drop": 3, "abort": 1}, total_count=1000)
```

## Function

```python
def log_rate(event_count: int, total_count: int) -> float:
def log_rate_table(event_counts: dict[str, int], total_count: int) -> dict[str, float]:
```

## When To Use What

- Use the raw rate when ordinary reporting is enough.
- Use the log rate when the events are rare and relative differences matter more than absolute percentages.
- Keep `abandon`, `abort`, `drop`, `miss`, `timeout`, and similar labels together. They are naming variants of the same formula, not separate learning units.

## Run tests

```bash
pytest modules/ml/evaluation/log-rate-metrics/python -q
```
