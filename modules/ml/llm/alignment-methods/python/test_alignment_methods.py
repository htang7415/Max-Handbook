from __future__ import annotations

import math

from alignment_methods import anchored_loss, dpo_loss, kl_penalty, preference_loss, reward_model_loss, sft_loss


def test_sft_loss_respects_mask() -> None:
    logits = [[2.0, 0.0], [0.0, 2.0]]
    loss = sft_loss(logits, [0, 1], [1, 0])
    assert loss < 0.2


def test_preference_loss_matches_pairwise_logistic_form() -> None:
    loss = preference_loss(2.0, 0.5)
    expected = math.log1p(math.exp(-(2.0 - 0.5)))
    assert math.isclose(loss, expected, rel_tol=1e-6)


def test_dpo_loss_is_small_when_policy_margin_beats_reference() -> None:
    loss = dpo_loss(1.0, 0.2, beta=0.5)
    assert loss < 0.6


def test_reward_model_loss_prefers_higher_chosen_score() -> None:
    loss = reward_model_loss(1.2, 0.0)
    assert loss < 0.4


def test_kl_penalty_is_positive_for_mismatched_distributions() -> None:
    penalty = kl_penalty([0.5, 0.5], [0.9, 0.1], beta=0.1)
    assert penalty > 0.0


def test_anchored_loss_mixes_alignment_and_ptx_terms() -> None:
    loss = anchored_loss(1.0, 0.5, 0.2)
    assert abs(loss - 0.9) < 1.0e-6
