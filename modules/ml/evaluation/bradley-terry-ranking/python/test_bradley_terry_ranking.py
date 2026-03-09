import pytest

from bradley_terry_ranking import bradley_terry_probability


def test_bradley_terry_probability_is_half_for_equal_scores() -> None:
    assert bradley_terry_probability(1.0, 1.0) == pytest.approx(0.5)


def test_bradley_terry_probability_matches_logistic_difference() -> None:
    assert bradley_terry_probability(0.0, 1.0) == pytest.approx(0.2689414213699951)


def test_bradley_terry_probability_favors_higher_scored_item() -> None:
    assert bradley_terry_probability(2.0, 0.0) > 0.5
