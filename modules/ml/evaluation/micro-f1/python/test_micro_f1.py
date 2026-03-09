import pytest

from micro_f1 import micro_f1_score


def test_micro_f1_score_aggregates_counts_before_computing_f1() -> None:
    score = micro_f1_score(
        true_positives=[8, 1],
        false_positives=[2, 1],
        false_negatives=[0, 3],
    )

    assert score == pytest.approx(2 * 9 / (2 * 9 + 3 + 3))


def test_micro_f1_score_returns_zero_for_no_classes() -> None:
    assert micro_f1_score([], [], []) == pytest.approx(0.0)


def test_micro_f1_score_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        micro_f1_score([1], [0, 1], [0])
