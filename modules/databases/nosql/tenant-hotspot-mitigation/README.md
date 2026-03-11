# Tenant Hotspot Mitigation

> Track: `databases` | Topic: `nosql`

## Concept

Hashing one tenant to one shard is simple, but one very large tenant can overload that shard. A common mitigation is to keep normal tenants single-shard while splitting only hot tenants across multiple buckets.

## Key Points

- Default tenant hashing preserves locality for most tenants.
- Hot tenants sometimes need bucketed fan-out instead of a single partition.
- Splitting one tenant trades some locality for lower shard skew.
- The goal is not perfect balance; it is avoiding one overloaded shard.

## Minimal Code Mental Model

```python
loads = shard_loads(rows, shard_count=4, split_tenants={"tenant-hot": 4})
```

## Function

```python
def stable_shard(value: str, shard_count: int) -> int:
def route_row(
    tenant_id: str,
    row_id: str,
    shard_count: int,
    split_tenants: dict[str, int] | None = None,
) -> int:
def shard_loads(
    rows: list[dict[str, object]],
    shard_count: int,
    split_tenants: dict[str, int] | None = None,
) -> dict[int, int]:
def tenant_shard_span(
    rows: list[dict[str, object]],
    shard_count: int,
    split_tenants: dict[str, int] | None = None,
) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/nosql/tenant-hotspot-mitigation/python -q
```
