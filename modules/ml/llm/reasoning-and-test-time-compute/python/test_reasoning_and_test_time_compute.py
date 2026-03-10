from __future__ import annotations

import pytest

from reasoning_and_test_time_compute import (
    best_of_n_success_probability,
    majority_vote_success_probability,
    test_time_compute_multiplier,
    total_inference_tokens,
)


def test_total_tokens_and_multiplier_capture_reasoning_cost() -> None:
    assert total_inference_tokens(1200, 1800, 200, samples=4) == 12800
    assert test_time_compute_multiplier(1200, 1800, 200, samples=4) == pytest.approx(
        12800 / 1400
    )


def test_best_of_n_success_grows_with_more_samples() -> None:
    assert best_of_n_success_probability(0.35, 1) == pytest.approx(0.35)
    assert best_of_n_success_probability(0.35, 4) == pytest.approx(0.82149375)


def test_majority_vote_success_probability_uses_binomial_majority() -> None:
    assert majority_vote_success_probability(0.7, 5) == pytest.approx(0.83692)


def test_validation_rejects_invalid_reasoning_inputs() -> None:
    with pytest.raises(ValueError):
        total_inference_tokens(-1, 0, 0)
    with pytest.raises(ValueError):
        test_time_compute_multiplier(0, 10, 0)
    with pytest.raises(ValueError):
        best_of_n_success_probability(1.2, 3)
    with pytest.raises(ValueError):
        majority_vote_success_probability(0.5, 4)
