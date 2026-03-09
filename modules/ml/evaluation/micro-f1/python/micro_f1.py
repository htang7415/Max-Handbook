from __future__ import annotations


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
