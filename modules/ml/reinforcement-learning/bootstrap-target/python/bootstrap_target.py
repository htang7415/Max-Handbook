from __future__ import annotations


def bootstrap_target(reward: float, gamma: float, next_value: float, done: bool) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    if done:
        return reward
    return reward + gamma * next_value
