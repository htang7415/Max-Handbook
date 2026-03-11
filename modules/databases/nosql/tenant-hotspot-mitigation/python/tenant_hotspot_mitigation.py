"""tenant_hotspot_mitigation - split only hot tenants to reduce shard skew."""

from __future__ import annotations


def stable_shard(value: str, shard_count: int) -> int:
    if shard_count <= 0:
        raise ValueError("shard_count must be positive")
    stable_hash = sum((index + 1) * ord(char) for index, char in enumerate(value))
    return stable_hash % shard_count


def route_row(
    tenant_id: str,
    row_id: str,
    shard_count: int,
    split_tenants: dict[str, int] | None = None,
) -> int:
    split_count = 1 if split_tenants is None else int(split_tenants.get(tenant_id, 1))
    if split_count <= 1:
        return stable_shard(tenant_id, shard_count)
    base_shard = stable_shard(tenant_id, shard_count)
    bucket = stable_shard(row_id, split_count)
    return (base_shard + bucket) % shard_count


def shard_loads(
    rows: list[dict[str, object]],
    shard_count: int,
    split_tenants: dict[str, int] | None = None,
) -> dict[int, int]:
    loads = {shard_id: 0 for shard_id in range(shard_count)}
    for row in rows:
        tenant_id = str(row["tenant_id"])
        row_id = str(row["row_id"])
        weight = int(row.get("weight", 1))
        shard_id = route_row(tenant_id, row_id, shard_count, split_tenants)
        loads[shard_id] += weight
    return loads


def tenant_shard_span(
    rows: list[dict[str, object]],
    shard_count: int,
    split_tenants: dict[str, int] | None = None,
) -> dict[str, int]:
    placements: dict[str, set[int]] = {}
    for row in rows:
        tenant_id = str(row["tenant_id"])
        row_id = str(row["row_id"])
        placements.setdefault(tenant_id, set()).add(
            route_row(tenant_id, row_id, shard_count, split_tenants)
        )
    return {
        tenant_id: len(shard_ids)
        for tenant_id, shard_ids in sorted(placements.items())
    }


def hottest_shard_load(loads: dict[int, int]) -> int:
    return max(loads.values(), default=0)
