from __future__ import annotations

import math

import pytest

from bandit_exploration_methods import epsilon_greedy_probs, incremental_mean, ucb_scores


def test_incremental_mean_matches_online_average_update() -> None:
    assert incremental_mean(estimate=2.0, pull_count=4, reward=6.0) == pytest.approx(3.0)


def test_epsilon_greedy_probs_puts_extra_mass_on_greedy_action() -> None:
    probs = epsilon_greedy_probs([1.0, 4.0, 2.0], epsilon=0.3)

    assert probs == pytest.approx([0.1, 0.8, 0.1])


def test_epsilon_greedy_probs_splits_greedy_mass_across_ties() -> None:
    probs = epsilon_greedy_probs([5.0, 5.0], epsilon=0.2)

    assert probs == pytest.approx([0.5, 0.5])


def test_ucb_scores_treat_untried_arms_as_high_priority() -> None:
    scores = ucb_scores([1.0, 2.0], total_steps=10, pull_counts=[3, 0], c=1.0)

    assert math.isfinite(scores[0])
    assert scores[1] == float("inf")


def test_ucb_scores_require_valid_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        ucb_scores([1.0], total_steps=10, pull_counts=[1, 2])
    with pytest.raises(ValueError, match="positive"):
        ucb_scores([1.0], total_steps=0, pull_counts=[1])
