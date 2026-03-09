from __future__ import annotations


def pr_auc(recall: list[float], precision: list[float]) -> float:
    if len(recall) != len(precision):
        raise ValueError("recall and precision must have the same length")
    if not recall:
        return 0.0
    if any(not 0.0 <= value <= 1.0 for value in recall + precision):
        raise ValueError("recall and precision values must lie in [0, 1]")

    area = 0.0
    for index in range(1, len(recall)):
        if recall[index] < recall[index - 1]:
            raise ValueError("recall must be sorted in nondecreasing order")
        width = recall[index] - recall[index - 1]
        height = (precision[index] + precision[index - 1]) / 2.0
        area += width * height
    return area
