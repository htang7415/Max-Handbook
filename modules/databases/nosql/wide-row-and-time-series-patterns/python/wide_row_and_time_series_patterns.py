"""wide_row_and_time_series_patterns - partitioned appends for time-series reads."""

from __future__ import annotations


Store = dict[tuple[str, str], list[dict[str, object]]]


def partition_key(series_id: str, timestamp: str) -> tuple[str, str]:
    return series_id, timestamp[:10]


def write_point(
    store: Store,
    series_id: str,
    timestamp: str,
    value: float,
) -> None:
    key = partition_key(series_id, timestamp)
    store.setdefault(key, []).append({"timestamp": timestamp, "value": value})
    store[key].sort(key=lambda point: str(point["timestamp"]))


def points_for_day(
    store: Store,
    series_id: str,
    day: str,
) -> list[dict[str, object]]:
    return list(store.get((series_id, day), []))


def recent_points(
    store: Store,
    series_id: str,
    day_buckets: list[str],
    limit: int,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for day in day_buckets:
        rows.extend(points_for_day(store, series_id, day))
    rows.sort(key=lambda point: str(point["timestamp"]), reverse=True)
    return rows[:limit]
