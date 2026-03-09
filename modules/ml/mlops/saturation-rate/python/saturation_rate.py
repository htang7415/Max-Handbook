from __future__ import annotations


def saturation_rate(utilizations: list[float], threshold: float = 1.0) -> tuple[int, float]:
    if threshold < 0.0:
        raise ValueError("threshold must be non-negative")
    if not utilizations:
        return 0, 0.0
    if any(utilization < 0.0 for utilization in utilizations):
        raise ValueError("utilizations must be non-negative")

    saturated = sum(utilization >= threshold for utilization in utilizations)
    return saturated, saturated / len(utilizations)
