# Sparse Index Selectivity

> Track: `databases` | Topic: `indexing`

## Concept

A sparse index stores entries only for rows where an optional column is populated. When that column is rare, the index stays much smaller and each lookup searches a much tighter candidate set.

## Key Points

- Optional fields like `error_code`, `deleted_at`, or `published_at` are often sparse.
- Indexing only populated rows can save substantial storage.
- Sparse indexes are most useful when queries mostly target the populated subset.
- If almost every row has the value, the sparse advantage mostly disappears.

## Minimal Code Mental Model

```python
summary = selectivity_summary(total_rows=1_000_000, populated_fraction=0.01, matching_rows=100)
```

## Function

```python
def sparse_index_entries(total_rows: int, populated_fraction: float) -> int:
def full_index_entries(total_rows: int) -> int:
def selectivity_summary(
    total_rows: int,
    populated_fraction: float,
    matching_rows: int,
) -> dict[str, int | float]:
```

## Run tests

```bash
pytest modules/databases/indexing/sparse-index-selectivity/python -q
```
