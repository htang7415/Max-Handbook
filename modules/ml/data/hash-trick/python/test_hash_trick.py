import pytest

from hash_trick import hashed_feature_counts


def test_hashed_feature_counts_preserve_total_token_count() -> None:
    counts = hashed_feature_counts(tokens=["cat", "dog", "cat"], num_buckets=8)

    assert sum(counts) == 3


def test_hashed_feature_counts_are_deterministic() -> None:
    counts_a = hashed_feature_counts(tokens=["apple", "banana", "carrot"], num_buckets=16)
    counts_b = hashed_feature_counts(tokens=["apple", "banana", "carrot"], num_buckets=16)

    assert counts_a == counts_b


def test_hashed_feature_counts_support_extreme_collisions() -> None:
    counts = hashed_feature_counts(tokens=["a", "b", "c"], num_buckets=1)

    assert counts == [3]


def test_hashed_feature_counts_require_positive_bucket_count() -> None:
    with pytest.raises(ValueError, match="positive"):
        hashed_feature_counts(tokens=["x"], num_buckets=0)
