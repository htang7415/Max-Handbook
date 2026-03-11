from wide_row_and_time_series_patterns import (
    partition_key,
    points_for_day,
    recent_points,
    write_point,
)


def build_store():
    store = {}
    write_point(store, "sensor-1", "2026-03-10T23:55:00Z", 18.1)
    write_point(store, "sensor-1", "2026-03-11T10:00:00Z", 18.2)
    write_point(store, "sensor-1", "2026-03-11T10:05:00Z", 18.7)
    write_point(store, "sensor-2", "2026-03-11T10:10:00Z", 22.0)
    return store


def test_partition_key_groups_by_series_and_day_bucket() -> None:
    assert partition_key("sensor-1", "2026-03-11T10:00:00Z") == ("sensor-1", "2026-03-11")


def test_points_for_day_reads_only_the_target_partition() -> None:
    store = build_store()

    assert points_for_day(store, "sensor-1", "2026-03-11") == [
        {"timestamp": "2026-03-11T10:00:00Z", "value": 18.2},
        {"timestamp": "2026-03-11T10:05:00Z", "value": 18.7},
    ]


def test_recent_points_merges_requested_buckets_without_scanning_other_series() -> None:
    store = build_store()

    assert recent_points(store, "sensor-1", ["2026-03-10", "2026-03-11"], limit=2) == [
        {"timestamp": "2026-03-11T10:05:00Z", "value": 18.7},
        {"timestamp": "2026-03-11T10:00:00Z", "value": 18.2},
    ]
