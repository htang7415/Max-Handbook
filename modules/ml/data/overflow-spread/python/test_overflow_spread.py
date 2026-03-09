import pytest

from overflow_spread import overflow_spread


def test_overflow_spread_returns_difference_between_two_quantiles() -> None:
    score = overflow_spread([64, 120, 80, 200], max_length=100, low_quantile=0.25, high_quantile=0.75)

    assert score == pytest.approx(40.0)


def test_overflow_spread_returns_zero_for_empty_input() -> None:
    assert overflow_spread([], max_length=64) == pytest.approx(0.0)


def test_overflow_spread_requires_ordered_quantiles() -> None:
    with pytest.raises(ValueError, match="less than or equal"):
        overflow_spread([100], max_length=64, low_quantile=0.9, high_quantile=0.2)
