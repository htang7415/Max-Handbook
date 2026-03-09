import math

import pytest

from risk_ratio import risk_ratio


def test_risk_ratio_returns_ratio_of_exposed_to_baseline_rates() -> None:
    ratio = risk_ratio([1, 1, 0, 1], [0, 1, 0, 0])

    assert ratio == pytest.approx(3.0)


def test_risk_ratio_returns_infinity_when_baseline_rate_is_zero() -> None:
    assert math.isinf(risk_ratio([1, 1], [0, 0]))


def test_risk_ratio_returns_zero_when_both_rates_are_zero() -> None:
    assert risk_ratio([], []) == pytest.approx(0.0)


def test_risk_ratio_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        risk_ratio([1, 2], [0, 1])
