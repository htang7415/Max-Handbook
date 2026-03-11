from approximate_count_distinct import count_distinct_summary, exact_count_distinct


def test_exact_count_distinct_ignores_duplicates() -> None:
    values = ["u1", "u1", "u2", "u3", "u3"]

    assert exact_count_distinct(values) == 3


def test_more_buckets_improves_estimate_for_same_dataset() -> None:
    values = [f"user-{index}" for index in range(80)] + [f"user-{index}" for index in range(20)]

    low_precision = count_distinct_summary(values, bucket_count=32)
    high_precision = count_distinct_summary(values, bucket_count=256)

    assert high_precision["absolute_error"] <= low_precision["absolute_error"]
    assert high_precision["exact"] == 80
