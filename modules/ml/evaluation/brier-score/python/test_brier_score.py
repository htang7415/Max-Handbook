import pytest

from brier_score import brier_score


def test_brier_score_matches_mean_squared_probability_error() -> None:
    score = brier_score(labels=[1, 0, 1], probabilities=[0.9, 0.2, 0.6])

    assert score == pytest.approx(0.07)


def test_brier_score_is_zero_for_perfect_probabilities() -> None:
    assert brier_score(labels=[1, 0], probabilities=[1.0, 0.0]) == pytest.approx(0.0)


def test_brier_score_requires_valid_probabilities() -> None:
    with pytest.raises(ValueError, match="0 <= p <= 1"):
        brier_score(labels=[1], probabilities=[1.5])
