import pytest

from headroom_gap import headroom_gap


def test_headroom_gap_returns_per_observation_gap_and_mean() -> None:
    gaps, mean_gap = headroom_gap([0.7, 0.9, 1.1], ceiling=1.0)

    assert gaps == pytest.approx([0.3, 0.1, -0.1])
    assert mean_gap == pytest.approx(0.1)


def test_headroom_gap_returns_zero_for_empty_input() -> None:
    assert headroom_gap([], ceiling=1.0) == ([], 0.0)


def test_headroom_gap_requires_non_negative_values() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        headroom_gap([0.5, -0.2], ceiling=1.0)
