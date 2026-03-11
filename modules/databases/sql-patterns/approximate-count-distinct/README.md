# Approximate Count Distinct

> Track: `databases` | Topic: `sql-patterns`

## Concept

Exact `COUNT(DISTINCT ...)` can get expensive on large streams or rollups. Approximate distinct counting uses a compact sketch to trade a small amount of error for much lower memory and merge cost.

## Key Points

- Distinct counting is expensive because duplicates must collapse somewhere.
- Approximate sketches keep fixed-size state instead of one slot per unique value.
- More buckets usually mean lower error.
- Approximate counts are good for dashboards and monitoring, not exact billing.

## Minimal Code Mental Model

```python
summary = count_distinct_summary(user_ids, bucket_count=128)
```

## Function

```python
def stable_bucket(value: str, bucket_count: int) -> int:
def exact_count_distinct(values: list[str]) -> int:
def approximate_count_distinct(values: list[str], bucket_count: int) -> int:
def count_distinct_summary(values: list[str], bucket_count: int) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/approximate-count-distinct/python -q
```
