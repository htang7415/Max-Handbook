from __future__ import annotations


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
