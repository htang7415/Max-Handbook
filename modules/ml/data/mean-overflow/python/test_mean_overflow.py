import pytest

from mean_overflow import mean_overflow


def test_mean_overflow_returns_average_excess_length_per_example() -> None:
    score = mean_overflow([64, 120, 80, 200], max_length=100)

    assert score == pytest.approx(30.0)


def test_mean_overflow_returns_zero_for_empty_input() -> None:
    assert mean_overflow([], max_length=64) == pytest.approx(0.0)


def test_mean_overflow_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        mean_overflow([10, -1], max_length=64)
