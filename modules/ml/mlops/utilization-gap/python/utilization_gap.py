from __future__ import annotations


def utilization_gap(utilizations: list[float], target: float) -> tuple[list[float], float]:
    if target < 0.0:
        raise ValueError("target must be non-negative")
    if not utilizations:
        return [], 0.0
    if any(utilization < 0.0 for utilization in utilizations):
        raise ValueError("utilizations must be non-negative")

    gaps = [utilization - target for utilization in utilizations]
    return gaps, sum(gaps) / len(gaps)
