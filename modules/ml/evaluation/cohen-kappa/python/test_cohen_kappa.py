import pytest

from cohen_kappa import cohen_kappa


def test_cohen_kappa_is_one_for_perfect_agreement() -> None:
    score = cohen_kappa([[3, 0], [0, 2]])

    assert score == pytest.approx(1.0)


def test_cohen_kappa_discounts_chance_agreement() -> None:
    score = cohen_kappa([[20, 5], [10, 15]])

    assert score == pytest.approx(0.4)


def test_cohen_kappa_returns_zero_for_empty_matrix() -> None:
    assert cohen_kappa([]) == pytest.approx(0.0)


def test_cohen_kappa_requires_square_matrix() -> None:
    with pytest.raises(ValueError, match="square"):
        cohen_kappa([[1, 0, 0], [0, 1, 0]])
