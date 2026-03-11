from tenant_partitioning_basics import tenant_partition_span


def test_partitioning_by_tenant_keeps_each_tenant_on_one_partition() -> None:
    rows = [
        {"tenant_id": "t1", "row_id": "t1-doc-1"},
        {"tenant_id": "t1", "row_id": "t1-doc-2"},
        {"tenant_id": "t2", "row_id": "t2-doc-1"},
        {"tenant_id": "t2", "row_id": "t2-doc-2"},
    ]

    assert tenant_partition_span(rows, partition_count=4, strategy="tenant") == {
        "t1": 1,
        "t2": 1,
    }


def test_partitioning_by_row_id_can_spread_one_tenant_across_many_partitions() -> None:
    rows = [
        {"tenant_id": "t1", "row_id": "alpha"},
        {"tenant_id": "t1", "row_id": "bravo"},
        {"tenant_id": "t1", "row_id": "charlie"},
    ]

    assert tenant_partition_span(rows, partition_count=4, strategy="row")["t1"] >= 2
