import pytest

from partition_pruning_basics import (
    build_monthly_partitions,
    month_key,
    pruned_partition_keys,
    query_partitioned_rows,
)


def test_pruning_only_keeps_overlapping_months():
    partitions = build_monthly_partitions(
        [
            {"id": "e1", "workspace_id": 7, "event_date": "2026-01-28"},
            {"id": "e2", "workspace_id": 7, "event_date": "2026-02-05"},
            {"id": "e3", "workspace_id": 7, "event_date": "2026-03-04"},
        ]
    )

    assert month_key("2026-03-11") == "2026-03"
    assert pruned_partition_keys(partitions, "2026-02-10", "2026-03-15") == [
        "2026-02",
        "2026-03",
    ]


def test_query_scans_only_pruned_partitions_and_filters_rows():
    partitions = build_monthly_partitions(
        [
            {"id": "e1", "workspace_id": 7, "event_date": "2026-01-28"},
            {"id": "e2", "workspace_id": 7, "event_date": "2026-02-14"},
            {"id": "e3", "workspace_id": 8, "event_date": "2026-03-03"},
            {"id": "e4", "workspace_id": 7, "event_date": "2026-03-04"},
        ]
    )

    scanned, matches = query_partitioned_rows(
        partitions,
        workspace_id=7,
        start_date="2026-02-10",
        end_date="2026-03-05",
    )

    assert scanned == ["2026-02", "2026-03"]
    assert matches == ["e2", "e4"]


def test_invalid_range_raises():
    with pytest.raises(ValueError):
        pruned_partition_keys({}, "2026-03-02", "2026-03-01")
