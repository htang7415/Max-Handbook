from __future__ import annotations


def generalized_advantages(
    rewards: list[float],
    values: list[float],
    gamma: float,
    lam: float,
    next_value: float = 0.0,
) -> list[float]:
    if len(rewards) != len(values):
        raise ValueError("rewards and values must have the same length")
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    if not 0.0 <= lam <= 1.0:
        raise ValueError("lam must satisfy 0 <= lam <= 1")

    advantages = [0.0] * len(rewards)
    running_advantage = 0.0

    for index in range(len(rewards) - 1, -1, -1):
        bootstrapped_value = next_value if index == len(rewards) - 1 else values[index + 1]
        delta = rewards[index] + gamma * bootstrapped_value - values[index]
        running_advantage = delta + gamma * lam * running_advantage
        advantages[index] = running_advantage

    return advantages
