from __future__ import annotations


def soft_update_gap(target_values: list[float], online_values: list[float], tau: float) -> float:
    if len(target_values) != len(online_values):
        raise ValueError("target_values and online_values must have the same length")
    if not 0.0 <= tau <= 1.0:
        raise ValueError("tau must satisfy 0 <= tau <= 1")
    if not target_values:
        return 0.0

    gaps = []
    for target_value, online_value in zip(target_values, online_values):
        updated_target = (1.0 - tau) * target_value + tau * online_value
        gaps.append(abs(online_value - updated_target))
    return sum(gaps) / len(gaps)
