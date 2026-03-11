"""watermark_lag_debugging - quantify how far each partition trails the source watermark."""

from __future__ import annotations


def partition_lag(
    source_watermarks: dict[int, int],
    consumer_watermarks: dict[int, int],
) -> dict[int, int]:
    lags: dict[int, int] = {}
    for partition, source_value in source_watermarks.items():
        consumer_value = consumer_watermarks.get(partition, 0)
        lags[partition] = max(source_value - consumer_value, 0)
    return lags


def lagging_partitions(
    source_watermarks: dict[int, int],
    consumer_watermarks: dict[int, int],
    min_lag: int,
) -> list[int]:
    return sorted(
        partition
        for partition, lag in partition_lag(source_watermarks, consumer_watermarks).items()
        if lag >= min_lag
    )


def most_lagging_partition(
    source_watermarks: dict[int, int],
    consumer_watermarks: dict[int, int],
) -> tuple[int, int] | None:
    lags = partition_lag(source_watermarks, consumer_watermarks)
    if not lags:
        return None
    partition = max(sorted(lags), key=lambda key: lags[key])
    return partition, lags[partition]


def lag_summary(
    source_watermarks: dict[int, int],
    consumer_watermarks: dict[int, int],
) -> dict[str, object]:
    lags = partition_lag(source_watermarks, consumer_watermarks)
    most_lagging = most_lagging_partition(source_watermarks, consumer_watermarks)
    return {
        "partition_lag": lags,
        "total_lag": sum(lags.values()),
        "most_lagging_partition": most_lagging,
    }
