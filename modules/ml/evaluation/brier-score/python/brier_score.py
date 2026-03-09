from __future__ import annotations


def brier_score(labels: list[int], probabilities: list[float]) -> float:
    if len(labels) != len(probabilities):
        raise ValueError("labels and probabilities must have the same length")
    if any(label not in (0, 1) for label in labels):
        raise ValueError("labels must be binary")
    if any(probability < 0.0 or probability > 1.0 for probability in probabilities):
        raise ValueError("probabilities must satisfy 0 <= p <= 1")
    if not labels:
        return 0.0

    return sum((probability - label) ** 2 for label, probability in zip(labels, probabilities)) / len(labels)
