import pytest

from overload_margin import overload_margin


def test_overload_margin_returns_mean_positive_excess_above_capacity() -> None:
    margin = overload_margin([0.8, 1.0, 1.3, 0.9, 1.5], capacity=1.0)

    assert margin == pytest.approx((0.0 + 0.0 + 0.3 + 0.0 + 0.5) / 5)


def test_overload_margin_returns_zero_for_empty_input() -> None:
    assert overload_margin([], capacity=1.0) == pytest.approx(0.0)


def test_overload_margin_requires_non_negative_observations() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overload_margin([1.0, -0.1], capacity=1.0)
