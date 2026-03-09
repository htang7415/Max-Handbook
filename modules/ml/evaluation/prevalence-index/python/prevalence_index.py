from __future__ import annotations


def prevalence_index(labels: list[int], baseline_rate: float) -> float:
    if not 0.0 <= baseline_rate <= 1.0:
        raise ValueError("baseline_rate must lie in [0, 1]")
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")
    if not labels:
        return 0.0

    rate = sum(labels) / len(labels)
    if baseline_rate == 0.0:
        return 0.0 if rate == 0.0 else float("inf")
    return rate / baseline_rate
