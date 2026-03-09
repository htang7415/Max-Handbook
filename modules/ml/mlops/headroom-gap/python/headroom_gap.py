from __future__ import annotations


def headroom_gap(observations: list[float], ceiling: float) -> tuple[list[float], float]:
    if ceiling < 0.0:
        raise ValueError("ceiling must be non-negative")
    if not observations:
        return [], 0.0
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")

    gaps = [ceiling - observation for observation in observations]
    return gaps, sum(gaps) / len(gaps)
