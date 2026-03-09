from __future__ import annotations


def lift_at_k(labels: list[int], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not labels:
        return 0.0
    if k > len(labels):
        raise ValueError("k must not exceed the number of labels")
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")

    base_rate = sum(labels) / len(labels)
    if base_rate == 0.0:
        return 0.0

    precision_at_k = sum(labels[:k]) / k
    return precision_at_k / base_rate
