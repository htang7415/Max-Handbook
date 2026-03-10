import pytest

from classification_metrics_core import (
    accuracy,
    balanced_accuracy,
    confusion_matrix,
    f1_score,
    hamming_loss,
    log_loss,
    macro_f1_score,
    matthews_correlation,
    micro_f1_score,
    precision_recall,
    roc_auc,
    top_k_accuracy,
)


def test_top_k_accuracy_checks_label_presence_in_prefix() -> None:
    score = top_k_accuracy([[2, 1, 0], [0, 1, 2]], [1, 2], k=2)
    assert score == pytest.approx(0.5)


def test_accuracy_and_confusion_matrix_capture_basic_binary_results() -> None:
    assert accuracy([0, 1, 1], [0, 0, 1]) == pytest.approx(2 / 3)
    assert confusion_matrix([0, 1, 1], [0, 0, 1]) == [[1, 0], [1, 1]]


def test_precision_recall_f1_chain_together() -> None:
    precision, recall = precision_recall([1, 0, 1], [1, 1, 0])
    assert precision == pytest.approx(0.5)
    assert recall == pytest.approx(0.5)
    assert f1_score(precision, recall) == pytest.approx(0.5)


def test_macro_and_micro_f1_capture_different_averaging_schemes() -> None:
    macro = macro_f1_score([5, 1], [1, 3], [0, 2])
    micro = micro_f1_score([5, 1], [1, 3], [0, 2])
    assert macro != micro


def test_balanced_accuracy_averages_class_recall() -> None:
    assert balanced_accuracy([8, 2], [2, 8]) == pytest.approx((0.8 + 0.2) / 2.0)


def test_hamming_loss_counts_labelwise_mismatches() -> None:
    score = hamming_loss([[1, 0], [0, 1]], [[1, 1], [0, 0]])
    assert score == pytest.approx(0.5)


def test_log_loss_penalizes_confident_mistakes() -> None:
    mild = log_loss([1, 0], [0.8, 0.2])
    harsh = log_loss([1, 0], [0.99, 0.99])
    assert harsh > mild


def test_roc_auc_and_mcc_cover_probability_and_binary_balance_views() -> None:
    assert roc_auc([0.0, 1.0], [0.0, 1.0]) == pytest.approx(0.5)
    assert matthews_correlation(1, 1, 0, 0) == pytest.approx(1.0)


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="same length"):
        top_k_accuracy([[1]], [], k=1)
