import pytest

from pr_auc import pr_auc


def test_pr_auc_integrates_precision_recall_curve() -> None:
    score = pr_auc(
        recall=[0.0, 0.5, 1.0],
        precision=[1.0, 0.75, 0.5],
    )

    assert score == pytest.approx(0.75)


def test_pr_auc_returns_zero_for_empty_curve() -> None:
    assert pr_auc([], []) == pytest.approx(0.0)


def test_pr_auc_requires_sorted_recall() -> None:
    with pytest.raises(ValueError, match="sorted"):
        pr_auc([0.0, 0.8, 0.6], [1.0, 0.7, 0.5])


def test_pr_auc_requires_values_between_zero_and_one() -> None:
    with pytest.raises(ValueError, match="\\[0, 1\\]"):
        pr_auc([0.0, 1.2], [1.0, 0.3])
