import pytest

from balanced_accuracy import balanced_accuracy


def test_balanced_accuracy_averages_class_recalls() -> None:
    score = balanced_accuracy(true_positives=[8, 1], false_negatives=[0, 3])

    assert score == pytest.approx((1.0 + 0.25) / 2.0)


def test_balanced_accuracy_returns_zero_for_no_classes() -> None:
    assert balanced_accuracy([], []) == pytest.approx(0.0)


def test_balanced_accuracy_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        balanced_accuracy([1], [0, 1])
