# Tenant Partitioning Basics

> Track: `databases` | Topic: `nosql`

## Concept

Tenant partitioning keeps one tenant’s rows together behind the same partition key. That reduces cross-partition reads for tenant-scoped workloads and makes movement or isolation decisions easier later.

## Key Points

- Partitioning by tenant localizes tenant reads and writes.
- Partitioning by row ID can spread one tenant across many partitions.
- Locality is often more valuable than perfectly even distribution for multi-tenant operational workloads.
- Large tenants may still need overrides or dedicated partitions once they outgrow the default pattern.

## Minimal Code Mental Model

```python
span = tenant_partition_span(rows, partition_count=4, strategy="tenant")
```

## Function

```python
def stable_partition(value: str, partition_count: int) -> int:
def partition_rows_by_tenant(rows: list[dict[str, str]], partition_count: int) -> dict[int, list[str]]:
def partition_rows_by_row_id(rows: list[dict[str, str]], partition_count: int) -> dict[int, list[str]]:
def tenant_partition_span(
    rows: list[dict[str, str]],
    partition_count: int,
    strategy: str,
) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/nosql/tenant-partitioning-basics/python -q
```
