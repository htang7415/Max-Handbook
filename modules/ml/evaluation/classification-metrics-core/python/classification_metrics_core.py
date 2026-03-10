from __future__ import annotations

import math


def accuracy(y_true: list[int], y_pred: list[int]) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if not y_true:
        return 0.0
    correct = sum(1 for truth, pred in zip(y_true, y_pred) if truth == pred)
    return correct / len(y_true)


def confusion_matrix(y_true: list[int], y_pred: list[int]) -> list[list[int]]:
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if any(label not in {0, 1} for label in y_true + y_pred):
        raise ValueError("confusion_matrix currently expects binary labels")

    tn = sum(1 for truth, pred in zip(y_true, y_pred) if truth == 0 and pred == 0)
    fp = sum(1 for truth, pred in zip(y_true, y_pred) if truth == 0 and pred == 1)
    fn = sum(1 for truth, pred in zip(y_true, y_pred) if truth == 1 and pred == 0)
    tp = sum(1 for truth, pred in zip(y_true, y_pred) if truth == 1 and pred == 1)
    return [[tn, fp], [fn, tp]]


def precision_recall(y_true: list[int], y_pred: list[int]) -> tuple[float, float]:
    matrix = confusion_matrix(y_true, y_pred)
    tn, fp = matrix[0]
    fn, tp = matrix[1]
    del tn
    precision = tp / (tp + fp) if tp + fp > 0 else 0.0
    recall = tp / (tp + fn) if tp + fn > 0 else 0.0
    return precision, recall


def f1_score(precision: float, recall: float) -> float:
    if precision < 0.0 or recall < 0.0:
        raise ValueError("precision and recall must be non-negative")
    if precision + recall == 0.0:
        return 0.0
    return 2.0 * precision * recall / (precision + recall)


def roc_auc(fpr: list[float], tpr: list[float]) -> float:
    if len(fpr) != len(tpr):
        raise ValueError("fpr and tpr must have the same length")
    if len(fpr) < 2:
        return 0.0
    if any(value < 0.0 or value > 1.0 for value in fpr + tpr):
        raise ValueError("fpr and tpr must stay in [0, 1]")

    area = 0.0
    for i in range(1, len(fpr)):
        area += (fpr[i] - fpr[i - 1]) * (tpr[i] + tpr[i - 1]) / 2.0
    return area


def matthews_correlation(tp: int, tn: int, fp: int, fn: int) -> float:
    if any(value < 0 for value in [tp, tn, fp, fn]):
        raise ValueError("confusion counts must be non-negative")
    denominator = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    if denominator == 0.0:
        return 0.0
    return (tp * tn - fp * fn) / denominator


def top_k_accuracy(predicted_rankings: list[list[int]], labels: list[int], k: int) -> float:
    if len(predicted_rankings) != len(labels):
        raise ValueError("predicted_rankings and labels must have the same length")
    if k <= 0:
        raise ValueError("k must be positive")
    if not labels:
        return 0.0

    correct = 0
    for ranking, label in zip(predicted_rankings, labels):
        if label in ranking[:k]:
            correct += 1
    return correct / len(labels)


def macro_f1_score(
    true_positives: list[int],
    false_positives: list[int],
    false_negatives: list[int],
) -> float:
    if len(true_positives) != len(false_positives) or len(true_positives) != len(false_negatives):
        raise ValueError("all class-stat lists must have the same length")
    if any(value < 0 for value in true_positives + false_positives + false_negatives):
        raise ValueError("class statistics must be non-negative")
    if not true_positives:
        return 0.0

    total = 0.0
    for tp, fp, fn in zip(true_positives, false_positives, false_negatives):
        precision = 0.0 if tp + fp == 0 else tp / (tp + fp)
        recall = 0.0 if tp + fn == 0 else tp / (tp + fn)
        total += 0.0 if precision + recall == 0.0 else 2.0 * precision * recall / (precision + recall)
    return total / len(true_positives)


def micro_f1_score(
    true_positives: list[int],
    false_positives: list[int],
    false_negatives: list[int],
) -> float:
    if len(true_positives) != len(false_positives) or len(true_positives) != len(false_negatives):
        raise ValueError("all class-stat lists must have the same length")
    if any(value < 0 for value in true_positives + false_positives + false_negatives):
        raise ValueError("class statistics must be non-negative")
    if not true_positives:
        return 0.0

    tp = sum(true_positives)
    fp = sum(false_positives)
    fn = sum(false_negatives)
    denominator = 2 * tp + fp + fn
    return 0.0 if denominator == 0 else 2 * tp / denominator


def balanced_accuracy(true_positives: list[int], false_negatives: list[int]) -> float:
    if len(true_positives) != len(false_negatives):
        raise ValueError("true_positives and false_negatives must have the same length")
    if any(value < 0 for value in true_positives + false_negatives):
        raise ValueError("class statistics must be non-negative")
    if not true_positives:
        return 0.0

    total = 0.0
    for tp, fn in zip(true_positives, false_negatives):
        total += 0.0 if tp + fn == 0 else tp / (tp + fn)
    return total / len(true_positives)


def hamming_loss(predictions: list[list[int]], labels: list[list[int]]) -> float:
    if len(predictions) != len(labels):
        raise ValueError("predictions and labels must have the same length")
    if not labels:
        return 0.0

    total_positions = 0
    mismatches = 0
    for prediction_row, label_row in zip(predictions, labels):
        if len(prediction_row) != len(label_row):
            raise ValueError("each prediction row must match its label row length")
        if any(value not in {0, 1} for value in prediction_row + label_row):
            raise ValueError("predictions and labels must be binary")

        total_positions += len(label_row)
        mismatches += sum(prediction != label for prediction, label in zip(prediction_row, label_row))
    return 0.0 if total_positions == 0 else mismatches / total_positions


def log_loss(labels: list[int], probabilities: list[float], eps: float = 1.0e-15) -> float:
    if len(labels) != len(probabilities):
        raise ValueError("labels and probabilities must have the same length")
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must be binary")
    if any(probability < 0.0 or probability > 1.0 for probability in probabilities):
        raise ValueError("probabilities must satisfy 0 <= p <= 1")
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    if not labels:
        return 0.0

    total = 0.0
    for label, probability in zip(labels, probabilities):
        clipped = min(max(probability, eps), 1.0 - eps)
        total += label * math.log(clipped) + (1 - label) * math.log(1.0 - clipped)
    return -total / len(labels)
