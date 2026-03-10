from __future__ import annotations

import math


def policy_entropy(probabilities: list[float]) -> float:
    if not probabilities:
        return 0.0
    if any(probability < 0.0 for probability in probabilities):
        raise ValueError("probabilities must be non-negative")

    total_probability = sum(probabilities)
    if not math.isclose(total_probability, 1.0, rel_tol=1.0e-9, abs_tol=1.0e-9):
        raise ValueError("probabilities must sum to 1")

    return -sum(probability * math.log(probability) for probability in probabilities if probability > 0.0)


def entropy_bonus(probabilities: list[float], coefficient: float) -> float:
    if coefficient < 0.0:
        raise ValueError("coefficient must be non-negative")
    return coefficient * policy_entropy(probabilities)


def normalize_advantages(advantages: list[float], eps: float = 1.0e-8) -> list[float]:
    if eps < 0.0:
        raise ValueError("eps must be non-negative")
    if not advantages:
        return []

    mean = sum(advantages) / len(advantages)
    variance = sum((advantage - mean) ** 2 for advantage in advantages) / len(advantages)
    std = math.sqrt(variance)
    return [(advantage - mean) / (std + eps) for advantage in advantages]


def normalize_value_targets(values: list[float], eps: float = 1.0e-8) -> tuple[list[float], float, float]:
    if eps < 0.0:
        raise ValueError("eps must be non-negative")
    if not values:
        return [], 0.0, 0.0

    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    std = math.sqrt(variance)
    normalized = [(value - mean) / (std + eps) for value in values]
    return normalized, mean, std


def reward_scale(rewards: list[float]) -> float:
    if not rewards:
        return 0.0
    return sum(abs(reward) for reward in rewards) / len(rewards)


def clip_rewards(rewards: list[float], min_reward: float = -1.0, max_reward: float = 1.0) -> list[float]:
    if min_reward > max_reward:
        raise ValueError("min_reward cannot exceed max_reward")
    return [min(max(reward, min_reward), max_reward) for reward in rewards]
