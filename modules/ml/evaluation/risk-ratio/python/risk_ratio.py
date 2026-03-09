from __future__ import annotations


def _positive_rate(labels: list[int]) -> float:
    if not labels:
        return 0.0
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")
    return sum(labels) / len(labels)


def risk_ratio(exposed_labels: list[int], baseline_labels: list[int]) -> float:
    exposed_rate = _positive_rate(exposed_labels)
    baseline_rate = _positive_rate(baseline_labels)
    if baseline_rate == 0.0:
        return 0.0 if exposed_rate == 0.0 else float("inf")
    return exposed_rate / baseline_rate
