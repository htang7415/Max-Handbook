from tenant_hotspot_mitigation import hottest_shard_load, shard_loads, tenant_shard_span


def test_hot_tenant_split_reduces_hottest_shard_load() -> None:
    rows = [
        {"tenant_id": "tenant-hot", "row_id": f"row-{index}", "weight": 10}
        for index in range(8)
    ] + [
        {"tenant_id": "tenant-cold", "row_id": f"cold-{index}", "weight": 1}
        for index in range(4)
    ]

    default_loads = shard_loads(rows, shard_count=4)
    split_loads = shard_loads(rows, shard_count=4, split_tenants={"tenant-hot": 4})

    assert hottest_shard_load(split_loads) < hottest_shard_load(default_loads)


def test_only_hot_tenant_loses_single_shard_locality() -> None:
    rows = [
        {"tenant_id": "tenant-hot", "row_id": f"row-{index}"}
        for index in range(8)
    ] + [
        {"tenant_id": "tenant-cold", "row_id": f"cold-{index}"}
        for index in range(3)
    ]

    spans = tenant_shard_span(rows, shard_count=4, split_tenants={"tenant-hot": 4})

    assert spans["tenant-hot"] > 1
    assert spans["tenant-cold"] == 1
