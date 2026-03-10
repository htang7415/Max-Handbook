import math

import pytest

from vote_metrics import (
    answer_stability,
    answer_uniqueness_rate,
    candidate_diversity,
    consensus_disagreement_rate,
    majority_vote_margin,
    minority_cluster_entropy,
    normalize_answer,
    top_vote_share,
    vote_entropy,
)


def test_normalization_collapses_surface_forms() -> None:
    assert normalize_answer("The Answer!") == "answer"


def test_answer_stability_counts_pairwise_agreement() -> None:
    stability = answer_stability(["Paris", "paris", "London"])

    assert stability == pytest.approx(1 / 3)


def test_margin_and_top_share_capture_winner_strength() -> None:
    answers = ["A", "a", "B", "C"]

    assert majority_vote_margin(answers) == pytest.approx(0.25)
    assert top_vote_share(answers) == pytest.approx(0.5)
    assert consensus_disagreement_rate(answers) == pytest.approx(0.5)


def test_entropy_and_uniqueness_capture_fragmentation() -> None:
    answers = ["A", "B", "C", "C"]

    expected_entropy = -(
        0.25 * math.log(0.25)
        + 0.25 * math.log(0.25)
        + 0.5 * math.log(0.5)
    )
    assert vote_entropy(answers) == pytest.approx(expected_entropy)
    assert answer_uniqueness_rate(answers) == pytest.approx(0.75)
    assert candidate_diversity(answers) == pytest.approx(0.75)


def test_minority_cluster_entropy_ignores_the_winning_cluster() -> None:
    answers = ["A", "A", "B", "C", "C"]

    expected = -(1 / 3) * math.log(1 / 3) - (2 / 3) * math.log(2 / 3)
    assert minority_cluster_entropy(answers) == pytest.approx(expected)


def test_empty_inputs_return_zero_like_summaries() -> None:
    assert answer_stability([]) == 0.0
    assert majority_vote_margin([]) == 0.0
    assert vote_entropy([]) == 0.0
    assert minority_cluster_entropy(["only"]) == 0.0
