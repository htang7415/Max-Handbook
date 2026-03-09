import pytest

from reward_scale import reward_scale


def test_reward_scale_returns_mean_absolute_reward() -> None:
    assert reward_scale([1.0, -3.0, 2.0, -2.0]) == pytest.approx(2.0)


def test_reward_scale_is_zero_for_empty_rewards() -> None:
    assert reward_scale([]) == pytest.approx(0.0)


def test_reward_scale_handles_all_zero_rewards() -> None:
    assert reward_scale([0.0, 0.0, 0.0]) == pytest.approx(0.0)
