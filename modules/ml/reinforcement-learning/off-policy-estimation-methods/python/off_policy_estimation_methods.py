from __future__ import annotations


def _validate_inputs(rewards: list[float], target_probs: list[float], behavior_probs: list[float]) -> None:
    if len(rewards) != len(target_probs) or len(rewards) != len(behavior_probs):
        raise ValueError("rewards, target_probs, and behavior_probs must have the same length")
    if any(probability < 0.0 for probability in target_probs + behavior_probs):
        raise ValueError("probabilities must be non-negative")
    if any(probability == 0.0 for probability in behavior_probs):
        raise ValueError("behavior_probs must be strictly positive")


def importance_weights(target_probs: list[float], behavior_probs: list[float]) -> list[float]:
    if len(target_probs) != len(behavior_probs):
        raise ValueError("target_probs and behavior_probs must have the same length")
    if any(probability < 0.0 for probability in target_probs + behavior_probs):
        raise ValueError("probabilities must be non-negative")
    if any(probability == 0.0 for probability in behavior_probs):
        raise ValueError("behavior_probs must be strictly positive")
    return [target_prob / behavior_prob for target_prob, behavior_prob in zip(target_probs, behavior_probs)]


def importance_sampling_estimate(
    rewards: list[float],
    target_probs: list[float],
    behavior_probs: list[float],
) -> float:
    _validate_inputs(rewards, target_probs, behavior_probs)
    if not rewards:
        return 0.0

    weights = importance_weights(target_probs, behavior_probs)
    weighted_sum = sum(reward * weight for reward, weight in zip(rewards, weights))
    return weighted_sum / len(rewards)


def weighted_importance_sampling_estimate(
    rewards: list[float],
    target_probs: list[float],
    behavior_probs: list[float],
) -> float:
    _validate_inputs(rewards, target_probs, behavior_probs)
    if not rewards:
        return 0.0

    weights = importance_weights(target_probs, behavior_probs)
    weighted_sum = sum(reward * weight for reward, weight in zip(rewards, weights))
    total_weight = sum(weights)
    if total_weight == 0.0:
        return 0.0
    return weighted_sum / total_weight


def off_policy_estimates(
    rewards: list[float],
    target_probs: list[float],
    behavior_probs: list[float],
) -> tuple[float, float]:
    ordinary = importance_sampling_estimate(rewards, target_probs, behavior_probs)
    weighted = weighted_importance_sampling_estimate(rewards, target_probs, behavior_probs)
    return ordinary, weighted
