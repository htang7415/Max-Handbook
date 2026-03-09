import pytest

from overflow_count import overflow_count


def test_overflow_count_sums_all_excess_length() -> None:
    assert overflow_count([64, 120, 80, 200], max_length=100) == 120


def test_overflow_count_is_zero_when_no_lengths_overflow() -> None:
    assert overflow_count([20, 30, 40], max_length=50) == 0


def test_overflow_count_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_count([10, -1], max_length=64)
