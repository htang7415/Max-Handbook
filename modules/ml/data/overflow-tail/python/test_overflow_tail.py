import pytest

from overflow_tail import overflow_tail


def test_overflow_tail_returns_upper_tail_percentile_of_overflow() -> None:
    score = overflow_tail([64, 120, 80, 200], max_length=100, quantile=0.75)

    assert score == pytest.approx(40.0)


def test_overflow_tail_returns_zero_for_empty_input() -> None:
    assert overflow_tail([], max_length=64) == pytest.approx(0.0)


def test_overflow_tail_requires_quantile_in_unit_interval() -> None:
    with pytest.raises(ValueError, match="0 <= quantile <= 1"):
        overflow_tail([100], max_length=64, quantile=1.2)
