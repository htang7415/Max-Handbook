from __future__ import annotations


def cohen_kappa(confusion_matrix: list[list[int]]) -> float:
    if not confusion_matrix:
        return 0.0

    size = len(confusion_matrix)
    if any(len(row) != size for row in confusion_matrix):
        raise ValueError("confusion_matrix must be square")
    if any(value < 0 for row in confusion_matrix for value in row):
        raise ValueError("confusion_matrix counts must be non-negative")

    total = sum(sum(row) for row in confusion_matrix)
    if total == 0:
        return 0.0

    observed = sum(confusion_matrix[index][index] for index in range(size)) / total
    row_totals = [sum(row) for row in confusion_matrix]
    column_totals = [
        sum(confusion_matrix[row_index][column_index] for row_index in range(size))
        for column_index in range(size)
    ]
    expected = sum(row * column for row, column in zip(row_totals, column_totals)) / (total * total)
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return (observed - expected) / (1.0 - expected)
