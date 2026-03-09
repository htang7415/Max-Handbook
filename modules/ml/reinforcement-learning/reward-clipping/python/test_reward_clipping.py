import pytest

from reward_clipping import clip_rewards


def test_clip_rewards_limits_values_to_configured_range() -> None:
    clipped = clip_rewards(rewards=[-5.0, -0.5, 2.0], min_reward=-1.0, max_reward=1.0)

    assert clipped == pytest.approx([-1.0, -0.5, 1.0])


def test_clip_rewards_allows_custom_bounds() -> None:
    clipped = clip_rewards(rewards=[0.0, 3.0], min_reward=0.0, max_reward=2.0)

    assert clipped == pytest.approx([0.0, 2.0])


def test_clip_rewards_requires_valid_bounds() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        clip_rewards(rewards=[1.0], min_reward=2.0, max_reward=1.0)
