import pytest

from truncation_rate import truncation_rate


def test_truncation_rate_counts_lengths_over_the_limit() -> None:
    truncated, rate = truncation_rate([64, 120, 80, 200], max_length=100)

    assert truncated == 2
    assert rate == pytest.approx(0.5)


def test_truncation_rate_returns_zero_for_empty_input() -> None:
    assert truncation_rate([], max_length=128) == (0, 0.0)


def test_truncation_rate_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        truncation_rate([32, -1], max_length=64)
