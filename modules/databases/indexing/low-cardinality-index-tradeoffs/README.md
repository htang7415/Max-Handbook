# Low Cardinality Index Tradeoffs

> Track: `databases` | Topic: `indexing`

## Concept

Indexes help most when they avoid touching most of a table. On low-cardinality predicates like `is_active = true`, the index can become unattractive because too many rows still match.

## Key Points

- Selectivity matters more than the existence of an index.
- When a predicate matches a large share of rows, a sequential scan can be cheaper.
- Low-cardinality columns often need composite or partial indexes to become useful.
- This is why “index every filter column” is a bad rule.

## Minimal Code Mental Model

```python
summary = tradeoff_summary(total_rows=1_000_000, match_fraction=0.5)
```

## Function

```python
def matching_rows(total_rows: int, match_fraction: float) -> int:
def seq_scan_cost(total_rows: int) -> int:
def index_scan_cost(
    total_rows: int,
    match_fraction: float,
    probe_overhead: int = 8,
    heap_fetch_cost: int = 2,
) -> int:
def recommended_path(
    total_rows: int,
    match_fraction: float,
    probe_overhead: int = 8,
    heap_fetch_cost: int = 2,
) -> str:
def tradeoff_summary(
    total_rows: int,
    match_fraction: float,
    probe_overhead: int = 8,
    heap_fetch_cost: int = 2,
) -> dict[str, int | float | str]:
```

## Run tests

```bash
pytest modules/databases/indexing/low-cardinality-index-tradeoffs/python -q
```
