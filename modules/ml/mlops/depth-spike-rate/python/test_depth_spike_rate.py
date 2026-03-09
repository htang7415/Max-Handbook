import pytest

from depth_spike_rate import depth_spike_rate


def test_depth_spike_rate_counts_depths_above_threshold() -> None:
    spikes, rate = depth_spike_rate([2, 5, 7, 3, 8], threshold=4)

    assert spikes == 3
    assert rate == pytest.approx(3 / 5)


def test_depth_spike_rate_returns_zero_for_empty_input() -> None:
    assert depth_spike_rate([], threshold=4) == (0, 0.0)


def test_depth_spike_rate_requires_non_negative_depths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        depth_spike_rate([1, -1, 3], threshold=2)
