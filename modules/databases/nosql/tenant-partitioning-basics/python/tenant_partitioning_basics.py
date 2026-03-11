"""tenant_partitioning_basics - partition by tenant to keep each tenant localized."""

from __future__ import annotations


def stable_partition(value: str, partition_count: int) -> int:
    if partition_count <= 0:
        raise ValueError("partition_count must be positive")
    stable_hash = sum((index + 1) * ord(char) for index, char in enumerate(value))
    return stable_hash % partition_count


def partition_rows_by_tenant(
    rows: list[dict[str, str]],
    partition_count: int,
) -> dict[int, list[str]]:
    partitions = {partition_id: [] for partition_id in range(partition_count)}
    for row in rows:
        partition_id = stable_partition(str(row["tenant_id"]), partition_count)
        partitions[partition_id].append(str(row["row_id"]))
    return partitions


def partition_rows_by_row_id(
    rows: list[dict[str, str]],
    partition_count: int,
) -> dict[int, list[str]]:
    partitions = {partition_id: [] for partition_id in range(partition_count)}
    for row in rows:
        partition_id = stable_partition(str(row["row_id"]), partition_count)
        partitions[partition_id].append(str(row["row_id"]))
    return partitions


def tenant_partition_span(
    rows: list[dict[str, str]],
    partition_count: int,
    strategy: str,
) -> dict[str, int]:
    partitions = (
        partition_rows_by_tenant(rows, partition_count)
        if strategy == "tenant"
        else partition_rows_by_row_id(rows, partition_count)
    )
    spans: dict[str, set[int]] = {}
    for partition_id, row_ids in partitions.items():
        for row_id in row_ids:
            tenant_id = next(str(row["tenant_id"]) for row in rows if str(row["row_id"]) == row_id)
            spans.setdefault(tenant_id, set()).add(partition_id)
    return {tenant_id: len(partition_ids) for tenant_id, partition_ids in spans.items()}
