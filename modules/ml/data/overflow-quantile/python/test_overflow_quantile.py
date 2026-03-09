import pytest

from overflow_quantile import overflow_quantile


def test_overflow_quantile_returns_requested_percentile_of_overflow() -> None:
    score = overflow_quantile([64, 120, 80, 200], max_length=100, quantile=0.5)

    assert score == pytest.approx(10.0)


def test_overflow_quantile_returns_zero_for_empty_input() -> None:
    assert overflow_quantile([], max_length=64, quantile=0.9) == pytest.approx(0.0)


def test_overflow_quantile_requires_valid_quantile() -> None:
    with pytest.raises(ValueError, match="0 <= quantile <= 1"):
        overflow_quantile([100], max_length=64, quantile=-0.1)
