import pytest

from saturation_rate import saturation_rate


def test_saturation_rate_counts_utilizations_at_or_above_threshold() -> None:
    saturated, rate = saturation_rate([0.7, 1.0, 1.1, 0.95, 1.2], threshold=1.0)

    assert saturated == 3
    assert rate == pytest.approx(3 / 5)


def test_saturation_rate_returns_zero_for_empty_input() -> None:
    assert saturation_rate([]) == (0, 0.0)


def test_saturation_rate_requires_non_negative_utilizations() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        saturation_rate([0.5, -0.1], threshold=1.0)
