import pytest

from decoding_methods import (
    beam_search_step,
    greedy_choice,
    sampling_pipeline_candidates,
    temperature_scaled_logits,
    temperature_probabilities,
    top_k_filter,
    top_p_filter,
)


def test_greedy_choice_returns_argmax_index() -> None:
    assert greedy_choice([0.1, 3.5, 2.0]) == 1


def test_temperature_probabilities_are_normalized_and_sharpen_with_lower_temperature() -> None:
    cold = temperature_probabilities([0.0, 2.0], temperature=0.5)
    warm = temperature_probabilities([0.0, 2.0], temperature=2.0)

    assert sum(cold) == pytest.approx(1.0)
    assert sum(warm) == pytest.approx(1.0)
    assert cold[1] > warm[1]


def test_temperature_scaled_logits_divide_by_temperature() -> None:
    assert temperature_scaled_logits([2.0, 0.0], temperature=0.5) == [4.0, 0.0]


def test_top_k_and_top_p_filters_keep_expected_candidates() -> None:
    probabilities = [0.5, 0.3, 0.2]

    assert top_k_filter(probabilities, k=2) == [0, 1]
    assert top_p_filter(probabilities, p=0.75) == [0, 1]


def test_sampling_pipeline_applies_temperature_then_filters() -> None:
    kept = sampling_pipeline_candidates(
        logits=[3.0, 2.0, 0.0, -2.0],
        temperature=1.0,
        top_k=3,
        top_p=0.8,
    )

    assert kept == [0, 1]


def test_beam_search_step_returns_best_expansions() -> None:
    out = beam_search_step(
        beams=[([1], -0.2), ([2], -0.4)],
        next_token_log_probs=[[-0.1, -0.7], [-0.2, -0.3]],
        beam_width=2,
    )

    assert out == [([1, 0], -0.30000000000000004), ([2, 0], -0.6000000000000001)]


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        greedy_choice([])

    with pytest.raises(ValueError, match="positive"):
        temperature_probabilities([1.0], temperature=0.0)
