import pytest

from chi_square_feature_selection import chi_square_feature_score


def test_chi_square_feature_score_is_zero_under_independence() -> None:
    score = chi_square_feature_score(5, 5, 10, 10)

    assert score == pytest.approx(0.0)


def test_chi_square_feature_score_is_large_for_strong_association() -> None:
    score = chi_square_feature_score(10, 0, 0, 10)

    assert score == pytest.approx(20.0)


def test_chi_square_feature_score_requires_non_negative_counts() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        chi_square_feature_score(-1, 0, 1, 0)
