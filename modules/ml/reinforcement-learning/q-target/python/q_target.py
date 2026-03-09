from __future__ import annotations


def q_target(reward: float, gamma: float, next_q_values: list[float]) -> float:
    if not next_q_values:
        raise ValueError("next_q_values must be non-empty")
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")

    return reward + gamma * max(next_q_values)
