import pytest

from candidate_diversity import candidate_diversity


def test_candidate_diversity_counts_unique_normalized_candidates() -> None:
    score = candidate_diversity(
        ["Paris", "paris", " London ", "Rome"]
    )

    assert score == pytest.approx(3 / 4)


def test_candidate_diversity_returns_zero_for_no_candidates() -> None:
    assert candidate_diversity([]) == pytest.approx(0.0)


def test_candidate_diversity_is_one_when_all_candidates_differ() -> None:
    assert candidate_diversity(["A", "B", "C"]) == pytest.approx(1.0)
