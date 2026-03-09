import pytest

from reciprocal_rank_metric import reciprocal_rank


def test_reciprocal_rank_is_inverse_of_first_relevant_position() -> None:
    assert reciprocal_rank([0, 0, 1, 0]) == pytest.approx(1.0 / 3.0)


def test_reciprocal_rank_is_zero_when_no_relevant_result_exists() -> None:
    assert reciprocal_rank([0, 0, 0]) == pytest.approx(0.0)


def test_reciprocal_rank_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="binary"):
        reciprocal_rank([0, 2])
