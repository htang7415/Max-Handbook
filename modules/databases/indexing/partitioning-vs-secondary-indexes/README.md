# Partitioning Vs Secondary Indexes

> Track: `databases` | Topic: `indexing`

## Concept

Partitioning reduces the partitions you touch. Secondary indexes reduce the rows you touch inside those partitions. They solve different parts of the read path.

## Key Points

- Partition pruning is best for large date or tenant ranges that can skip whole chunks of data.
- A secondary index still matters inside each remaining partition when the query filters on another key.
- Partitioning alone does not make per-tenant or per-user lookups cheap.
- Good indexing design usually combines both ideas instead of treating them as substitutes.

## Boundary

Use `partition-pruning-basics` to learn how partitions are skipped. Use this module when the design question is whether pruning is enough or each remaining partition still needs its own secondary access path.

## Minimal Code Mental Model

```python
partitions = build_monthly_partitions(rows)
secondary = build_workspace_secondary_index(partitions)
scanned, inspected, matches = query_with_secondary_index(
    partitions,
    secondary,
    workspace_id=7,
    start_date="2026-02-01",
    end_date="2026-03-31",
)
```

## Function

```python
def build_workspace_secondary_index(
    partitions: dict[str, list[dict[str, object]]],
) -> dict[str, dict[int, list[dict[str, object]]]]:
def query_with_partitioning_only(
    partitions: dict[str, list[dict[str, object]]],
    workspace_id: int,
    start_date: str,
    end_date: str,
) -> tuple[list[str], int, list[str]]:
def query_with_secondary_index(
    partitions: dict[str, list[dict[str, object]]],
    secondary_indexes: dict[str, dict[int, list[dict[str, object]]]],
    workspace_id: int,
    start_date: str,
    end_date: str,
) -> tuple[list[str], int, list[str]]:
```

## Run tests

```bash
pytest modules/databases/indexing/partitioning-vs-secondary-indexes/python -q
```
