# Predicate Correlation And Stats

> Track: `databases` | Topic: `query-plans`

## Concept

Cardinality estimates often assume predicates are independent. When filters are correlated, that assumption can badly undercount rows and lead to poor plans unless the engine has better statistics.

## Key Points

- `country = 'US'` and `currency = 'USD'` are not independent filters in many datasets.
- Multiplying selectivities works for independence, but it overfilters when predicates move together.
- Large q-error on correlated predicates is a sign that multicolumn stats or better histograms may matter.
- This is one common cause of “planner chose a weird plan even though each single-column stat looked fine.”

## Minimal Code Mental Model

```python
summary = correlation_summary(table_rows=1_000_000, selectivities=[0.2, 0.2])
```

## Function

```python
def independent_estimate(table_rows: int, selectivities: list[float]) -> int:
def correlated_estimate(table_rows: int, selectivities: list[float]) -> int:
def q_error(estimated_rows: int, actual_rows: int) -> float:
def needs_extended_stats(
    estimated_rows: int,
    actual_rows: int,
    q_error_threshold: float = 4.0,
) -> bool:
def correlation_summary(table_rows: int, selectivities: list[float]) -> dict[str, int | float | bool]:
```

## Run tests

```bash
pytest modules/databases/query-plans/predicate-correlation-and-stats/python -q
```
