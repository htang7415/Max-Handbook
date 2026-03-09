from __future__ import annotations


def queue_backlog_ratio(queue_ages: list[float], target_age: float) -> tuple[list[float], float]:
    if target_age <= 0.0:
        raise ValueError("target_age must be positive")
    if not queue_ages:
        return [], 0.0
    if any(age < 0.0 for age in queue_ages):
        raise ValueError("queue_ages must be non-negative")

    ratios = [age / target_age for age in queue_ages]
    return ratios, sum(ratios) / len(ratios)
