# Watermark Lag Debugging

> Track: `databases` | Topic: `streaming`

## Concept

Watermark lag is the gap between what the source has produced and what the consumer has durably processed. Debugging lag usually starts with per-partition gaps, not one average number.

## Key Points

- One hot or stuck partition can dominate end-to-end freshness.
- Missing consumer progress for a partition usually means full lag on that partition.
- Total lag hides skew; the worst partition often explains the incident.
- Watermark debugging is a state and offsets problem before it is an autoscaling problem.

## Minimal Code Mental Model

```python
summary = lag_summary(
    source_watermarks={0: 120, 1: 90},
    consumer_watermarks={0: 118, 1: 70},
)
```

## Function

```python
def partition_lag(
    source_watermarks: dict[int, int],
    consumer_watermarks: dict[int, int],
) -> dict[int, int]:
def lagging_partitions(
    source_watermarks: dict[int, int],
    consumer_watermarks: dict[int, int],
    min_lag: int,
) -> list[int]:
def most_lagging_partition(
    source_watermarks: dict[int, int],
    consumer_watermarks: dict[int, int],
) -> tuple[int, int] | None:
```

## Run tests

```bash
pytest modules/databases/streaming/watermark-lag-debugging/python -q
```
