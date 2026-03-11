from watermark_lag_debugging import lag_summary, lagging_partitions, most_lagging_partition


def test_partition_lag_identifies_the_main_backlog() -> None:
    source = {0: 120, 1: 90, 2: 100}
    consumer = {0: 118, 1: 70, 2: 95}

    assert lag_summary(source, consumer) == {
        "partition_lag": {0: 2, 1: 20, 2: 5},
        "total_lag": 27,
        "most_lagging_partition": (1, 20),
    }


def test_missing_consumer_watermark_counts_as_full_lag() -> None:
    source = {0: 50, 1: 20}
    consumer = {0: 45}

    assert most_lagging_partition(source, consumer) == (1, 20)
    assert lagging_partitions(source, consumer, min_lag=5) == [0, 1]
