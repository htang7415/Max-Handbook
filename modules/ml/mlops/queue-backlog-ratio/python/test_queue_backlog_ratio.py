import pytest

from queue_backlog_ratio import queue_backlog_ratio


def test_queue_backlog_ratio_returns_per_observation_ratios_and_mean() -> None:
    ratios, mean_ratio = queue_backlog_ratio([10.0, 25.0, 40.0], target_age=20.0)

    assert ratios == pytest.approx([0.5, 1.25, 2.0])
    assert mean_ratio == pytest.approx(1.25)


def test_queue_backlog_ratio_returns_zero_for_empty_input() -> None:
    assert queue_backlog_ratio([], target_age=10.0) == ([], 0.0)


def test_queue_backlog_ratio_requires_positive_target() -> None:
    with pytest.raises(ValueError, match="positive"):
        queue_backlog_ratio([1.0], target_age=0.0)
