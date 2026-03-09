from __future__ import annotations


def overload_margin(observations: list[float], capacity: float) -> float:
    if capacity < 0.0:
        raise ValueError("capacity must be non-negative")
    if not observations:
        return 0.0
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")

    return sum(max(0.0, observation - capacity) for observation in observations) / len(observations)
