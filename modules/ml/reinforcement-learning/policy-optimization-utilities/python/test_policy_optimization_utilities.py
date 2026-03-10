from __future__ import annotations

import math

import pytest

from policy_optimization_utilities import (
    clip_rewards,
    entropy_bonus,
    normalize_advantages,
    normalize_value_targets,
    policy_entropy,
    reward_scale,
)


def test_policy_entropy_matches_discrete_entropy_definition() -> None:
    assert policy_entropy([0.5, 0.5]) == pytest.approx(math.log(2.0))


def test_entropy_bonus_scales_entropy() -> None:
    entropy = policy_entropy([0.25, 0.75])
    assert entropy_bonus([0.25, 0.75], coefficient=0.1) == pytest.approx(0.1 * entropy)


def test_normalize_advantages_centers_batch() -> None:
    normalized = normalize_advantages([1.0, 2.0, 3.0])
    assert sum(normalized) == pytest.approx(0.0)


def test_normalize_value_targets_returns_stats() -> None:
    normalized, mean, std = normalize_value_targets([1.0, 2.0, 3.0])
    assert mean == pytest.approx(2.0)
    assert std > 0.0
    assert sum(normalized) == pytest.approx(0.0)


def test_reward_scale_uses_mean_absolute_reward() -> None:
    assert reward_scale([-1.0, 2.0, -3.0]) == pytest.approx(2.0)


def test_clip_rewards_respects_bounds() -> None:
    assert clip_rewards([-5.0, 0.5, 4.0], min_reward=-1.0, max_reward=1.0) == [-1.0, 0.5, 1.0]


def test_utilities_validate_inputs() -> None:
    with pytest.raises(ValueError, match="sum to 1"):
        policy_entropy([0.2, 0.2])
    with pytest.raises(ValueError, match="non-negative"):
        entropy_bonus([0.5, 0.5], coefficient=-0.1)
    with pytest.raises(ValueError, match="eps"):
        normalize_advantages([1.0], eps=-1.0)
    with pytest.raises(ValueError, match="cannot exceed"):
        clip_rewards([1.0], min_reward=2.0, max_reward=1.0)
