# DuckDB Parquet Query Patterns

> Track: `databases` | Topic: `sql-patterns`

## Concept

DuckDB-style Parquet workflows are mostly about selecting the right files and columns before doing the actual scan.

## Key Points

- Partition pruning skips files that cannot satisfy the filter.
- Column projection avoids reading fields the query does not need.
- Local analytics queries often combine many Parquet fragments into one logical dataset.
- Good Parquet query shape is about reading less, not just scanning faster.

## Minimal Code Mental Model

```python
files = parquet_file_catalog()
selected = prune_partitions(files, filters={"day": "2026-03-11"})
columns = projected_columns(["workspace_id", "score"], ["day", "score"])
plan = query_plan_summary(selected, columns)
```

## Function

```python
def prune_partitions(
    files: list[dict[str, object]],
    filters: dict[str, object],
) -> list[str]:
def projected_columns(select_columns: list[str], available_columns: list[str]) -> list[str]:
def query_plan_summary(
    selected_files: list[str],
    selected_columns: list[str],
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/duckdb-parquet-query-patterns/python -q
```
