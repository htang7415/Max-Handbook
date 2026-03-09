import pytest

from delong_test import delong_auc_test


def test_delong_auc_test_detects_a_better_model() -> None:
    labels = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    scores_a = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    scores_b = [3, 12, 10, 9, 4, 13, 2, 6, 5, 11, 15, 8, 0, 7, 14, 1]

    result = delong_auc_test(labels=labels, scores_a=scores_a, scores_b=scores_b)

    assert result.auc_a == pytest.approx(1.0)
    assert result.auc_b == pytest.approx(0.484375)
    assert result.auc_difference == pytest.approx(0.515625)
    assert result.z_score > 0.0
    assert result.p_value < 0.01


def test_delong_auc_test_returns_neutral_result_for_identical_scores() -> None:
    labels = [1, 1, 0, 0]
    scores = [0.9, 0.7, 0.6, 0.2]

    result = delong_auc_test(labels=labels, scores_a=scores, scores_b=scores)

    assert result.auc_difference == pytest.approx(0.0)
    assert result.z_score == pytest.approx(0.0)
    assert result.p_value == pytest.approx(1.0)


def test_delong_auc_test_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="binary"):
        delong_auc_test(labels=[0, 2], scores_a=[0.1, 0.9], scores_b=[0.2, 0.8])
