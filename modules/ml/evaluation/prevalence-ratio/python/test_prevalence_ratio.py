import math

import pytest

from prevalence_ratio import prevalence_ratio


def test_prevalence_ratio_returns_ratio_of_positive_rates() -> None:
    ratio = prevalence_ratio([1, 0, 1, 1], [0, 1, 0, 0])

    assert ratio == pytest.approx(3.0)


def test_prevalence_ratio_returns_infinity_when_denominator_rate_is_zero() -> None:
    assert math.isinf(prevalence_ratio([1, 1], [0, 0]))


def test_prevalence_ratio_returns_zero_when_both_groups_have_zero_rate() -> None:
    assert prevalence_ratio([], []) == pytest.approx(0.0)


def test_prevalence_ratio_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        prevalence_ratio([1, 2], [0, 1])
