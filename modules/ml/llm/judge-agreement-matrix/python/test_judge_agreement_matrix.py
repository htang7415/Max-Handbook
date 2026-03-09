import pytest

from judge_agreement_matrix import judge_agreement_matrix


def test_judge_agreement_matrix_reports_pairwise_match_rates() -> None:
    matrix = judge_agreement_matrix(
        [
            [1, 1, 0, -1],
            [1, 0, 0, -1],
            [-1, -1, 0, 1],
        ]
    )

    assert matrix[0] == pytest.approx([1.0, 0.75, 0.25])
    assert matrix[1] == pytest.approx([0.75, 1.0, 0.25])
    assert matrix[2] == pytest.approx([0.25, 0.25, 1.0])


def test_judge_agreement_matrix_returns_empty_for_no_judges() -> None:
    assert judge_agreement_matrix([]) == []


def test_judge_agreement_matrix_requires_same_number_of_items() -> None:
    with pytest.raises(ValueError, match="same number of items"):
        judge_agreement_matrix([[1, 0], [1]])


def test_judge_agreement_matrix_requires_valid_decisions() -> None:
    with pytest.raises(ValueError, match="-1, 0, or 1"):
        judge_agreement_matrix([[2], [1]])
