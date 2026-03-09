from __future__ import annotations


def overload_duration_share(observations: list[float], threshold: float) -> float:
    if threshold < 0.0:
        raise ValueError("threshold must be non-negative")
    if not observations:
        return 0.0
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")

    return sum(observation > threshold for observation in observations) / len(observations)
