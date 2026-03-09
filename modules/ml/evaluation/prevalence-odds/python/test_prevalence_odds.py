import math

import pytest

from prevalence_odds import prevalence_odds


def test_prevalence_odds_returns_odds_of_positive_rate() -> None:
    assert prevalence_odds([1, 0, 1, 1]) == pytest.approx(3.0)


def test_prevalence_odds_returns_infinity_when_rate_is_one() -> None:
    assert math.isinf(prevalence_odds([1, 1, 1]))


def test_prevalence_odds_returns_zero_for_empty_input() -> None:
    assert prevalence_odds([]) == pytest.approx(0.0)


def test_prevalence_odds_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        prevalence_odds([1, 2, 0])
