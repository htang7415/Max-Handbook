from __future__ import annotations


def _positive_rate(labels: list[int]) -> float:
    if not labels:
        return 0.0
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")
    return sum(labels) / len(labels)


def base_rate_gap(group_a: list[int], group_b: list[int]) -> float:
    return _positive_rate(group_a) - _positive_rate(group_b)
