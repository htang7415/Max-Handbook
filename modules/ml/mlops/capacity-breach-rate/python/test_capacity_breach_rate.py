import pytest

from capacity_breach_rate import capacity_breach_rate


def test_capacity_breach_rate_counts_observations_above_capacity() -> None:
    breaches, rate = capacity_breach_rate([0.8, 1.0, 1.3, 0.9, 1.5], capacity=1.0)

    assert breaches == 2
    assert rate == pytest.approx(2 / 5)


def test_capacity_breach_rate_returns_zero_for_empty_input() -> None:
    assert capacity_breach_rate([], capacity=1.0) == (0, 0.0)


def test_capacity_breach_rate_requires_non_negative_observations() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        capacity_breach_rate([1.0, -0.1], capacity=1.0)
