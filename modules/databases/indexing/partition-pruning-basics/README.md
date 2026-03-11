# Partition Pruning Basics

> Track: `databases` | Topic: `indexing`

## Concept

Partition pruning skips entire physical partitions when the query predicate proves they cannot contain matching rows.

## Key Points

- Partitioning only helps when queries include the partition key or a range that can be mapped onto partitions.
- A monthly date partition is useful when most reads ask for recent windows.
- Pruning reduces the number of partitions touched before row-level filters run.
- Bad partition choices still leave the engine scanning many irrelevant partitions.

## Minimal Code Mental Model

```python
partitions = build_monthly_partitions(
    [
        {"id": "e1", "workspace_id": 7, "event_date": "2026-01-28"},
        {"id": "e2", "workspace_id": 7, "event_date": "2026-03-04"},
    ]
)
scanned, matches = query_partitioned_rows(
    partitions,
    workspace_id=7,
    start_date="2026-03-01",
    end_date="2026-03-31",
)
```

## Function

```python
def month_key(date_text: str) -> str:
def build_monthly_partitions(
    rows: list[dict[str, object]],
) -> dict[str, list[dict[str, object]]]:
def pruned_partition_keys(
    partitions: dict[str, list[dict[str, object]]],
    start_date: str,
    end_date: str,
) -> list[str]:
def query_partitioned_rows(
    partitions: dict[str, list[dict[str, object]]],
    workspace_id: int,
    start_date: str,
    end_date: str,
) -> tuple[list[str], list[str]]:
```

## Run tests

```bash
pytest modules/databases/indexing/partition-pruning-basics/python -q
```
