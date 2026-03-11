# Index Merge Vs Composite Indexes

> Track: `databases` | Topic: `indexing`

## Concept

Two single-column indexes can sometimes be combined, but a composite index on the actual filter shape is usually better for repeated conjunctions. Composite indexes reduce candidate rows earlier and preserve useful ordering.

## Key Points

- Index merge starts with two separate candidate sets.
- Composite indexes can jump directly to the combined predicate.
- Broad predicates can still make a sequential scan cheaper than either index strategy.
- The overlap between predicates cannot exceed either individual predicate.
- This is why hot query shapes should drive composite index design.

## Minimal Code Mental Model

```python
summary = strategy_summary(
    total_rows=1_000_000,
    left_selectivity=0.01,
    right_selectivity=0.02,
    overlap_selectivity=0.0005,
)
```

## Function

```python
def matching_rows(total_rows: int, selectivity: float) -> int:
def index_merge_cost(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
    row_fetch_cost: int = 2,
) -> int:
def composite_index_cost(
    total_rows: int,
    overlap_selectivity: float,
    probe_overhead: int = 8,
    row_fetch_cost: int = 2,
) -> int:
def recommended_strategy(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> str:
def strategy_summary(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> dict[str, int | float | str]:
```

## Run tests

```bash
pytest modules/databases/indexing/index-merge-vs-composite-indexes/python -q
```
