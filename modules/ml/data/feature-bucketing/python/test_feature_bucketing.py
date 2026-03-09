import pytest

from feature_bucketing import bucketize


def test_bucketize_assigns_values_to_expected_bins() -> None:
    buckets = bucketize(values=[-1.0, 0.5, 2.0, 5.0], boundaries=[0.0, 2.0, 4.0])

    assert buckets == [0, 1, 2, 3]


def test_bucketize_returns_last_bucket_for_large_values() -> None:
    assert bucketize(values=[10.0], boundaries=[1.0, 2.0]) == [2]


def test_bucketize_requires_sorted_boundaries() -> None:
    with pytest.raises(ValueError, match="sorted"):
        bucketize(values=[1.0], boundaries=[2.0, 1.0])
