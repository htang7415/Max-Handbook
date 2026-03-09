from __future__ import annotations


def _positive_rate(labels: list[int]) -> float:
    if not labels:
        return 0.0
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")
    return sum(labels) / len(labels)


def prevalence_delta(baseline_labels: list[int], comparison_labels: list[int]) -> float:
    return _positive_rate(comparison_labels) - _positive_rate(baseline_labels)
