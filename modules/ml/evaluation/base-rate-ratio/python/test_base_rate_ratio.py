import math

import pytest

from base_rate_ratio import base_rate_ratio


def test_base_rate_ratio_returns_ratio_of_two_positive_rates() -> None:
    ratio = base_rate_ratio([1, 0, 1, 1], [0, 1, 0, 0])

    assert ratio == pytest.approx(3.0)


def test_base_rate_ratio_returns_infinity_when_denominator_rate_is_zero() -> None:
    assert math.isinf(base_rate_ratio([1, 1], [0, 0]))


def test_base_rate_ratio_returns_zero_when_both_rates_are_zero() -> None:
    assert base_rate_ratio([], []) == pytest.approx(0.0)


def test_base_rate_ratio_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        base_rate_ratio([1, 2], [0, 1])
