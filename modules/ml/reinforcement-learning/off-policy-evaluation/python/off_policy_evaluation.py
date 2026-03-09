from __future__ import annotations


def off_policy_estimates(
    rewards: list[float],
    target_probs: list[float],
    behavior_probs: list[float],
) -> tuple[float, float]:
    if len(rewards) != len(target_probs) or len(rewards) != len(behavior_probs):
        raise ValueError("rewards, target_probs, and behavior_probs must have the same length")
    if not rewards:
        return 0.0, 0.0
    if any(probability < 0.0 for probability in target_probs + behavior_probs):
        raise ValueError("probabilities must be non-negative")
    if any(probability == 0.0 for probability in behavior_probs):
        raise ValueError("behavior_probs must be strictly positive")

    weighted_rewards = []
    total_weight = 0.0

    for reward, target_prob, behavior_prob in zip(rewards, target_probs, behavior_probs):
        weight = target_prob / behavior_prob
        weighted_rewards.append(reward * weight)
        total_weight += weight

    ordinary = sum(weighted_rewards) / len(rewards)
    weighted = 0.0 if total_weight == 0.0 else sum(weighted_rewards) / total_weight
    return ordinary, weighted
