import pytest

from utilization_gap import utilization_gap


def test_utilization_gap_returns_per_observation_gaps_and_mean() -> None:
    gaps, mean_gap = utilization_gap([0.7, 0.9, 1.1], target=0.8)

    assert gaps == pytest.approx([-0.1, 0.1, 0.3])
    assert mean_gap == pytest.approx(0.1)


def test_utilization_gap_returns_zero_for_empty_input() -> None:
    assert utilization_gap([], target=0.8) == ([], 0.0)


def test_utilization_gap_requires_non_negative_values() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        utilization_gap([0.5, -0.2], target=0.8)
