import pytest

from overflow_presence_rate import overflow_presence_rate


def test_overflow_presence_rate_counts_examples_over_the_limit() -> None:
    overflowing, rate = overflow_presence_rate([64, 120, 80, 200], max_length=100)

    assert overflowing == 2
    assert rate == pytest.approx(0.5)


def test_overflow_presence_rate_returns_zero_for_empty_input() -> None:
    assert overflow_presence_rate([], max_length=64) == (0, 0.0)


def test_overflow_presence_rate_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_presence_rate([10, -1], max_length=64)
