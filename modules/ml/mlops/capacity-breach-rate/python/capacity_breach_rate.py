from __future__ import annotations


def capacity_breach_rate(observations: list[float], capacity: float) -> tuple[int, float]:
    if capacity < 0.0:
        raise ValueError("capacity must be non-negative")
    if not observations:
        return 0, 0.0
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")

    breaches = sum(observation > capacity for observation in observations)
    return breaches, breaches / len(observations)
