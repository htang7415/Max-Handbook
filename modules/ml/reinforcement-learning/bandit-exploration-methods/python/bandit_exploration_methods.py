from __future__ import annotations

import math


def incremental_mean(estimate: float, pull_count: int, reward: float) -> float:
    if pull_count <= 0:
        raise ValueError("pull_count must be positive")
    return estimate + (reward - estimate) / pull_count


def epsilon_greedy_probs(action_values: list[float], epsilon: float) -> list[float]:
    if not action_values:
        raise ValueError("action_values must be non-empty")
    if not 0.0 <= epsilon <= 1.0:
        raise ValueError("epsilon must satisfy 0 <= epsilon <= 1")

    num_actions = len(action_values)
    max_value = max(action_values)
    best_actions = [index for index, value in enumerate(action_values) if value == max_value]

    probs = [epsilon / num_actions] * num_actions
    greedy_mass = (1.0 - epsilon) / len(best_actions)
    for index in best_actions:
        probs[index] += greedy_mass
    return probs


def ucb_scores(action_values: list[float], total_steps: int, pull_counts: list[int], c: float = 1.0) -> list[float]:
    if len(action_values) != len(pull_counts):
        raise ValueError("action_values and pull_counts must have the same length")
    if not action_values:
        raise ValueError("action_values and pull_counts must be non-empty")
    if total_steps <= 0:
        raise ValueError("total_steps must be positive")
    if c < 0.0:
        raise ValueError("c must be non-negative")

    scores: list[float] = []
    for value, pulls in zip(action_values, pull_counts):
        if pulls < 0:
            raise ValueError("pull_counts must be non-negative")
        if pulls == 0:
            scores.append(float("inf"))
            continue
        bonus = c * math.sqrt(math.log(total_steps) / pulls)
        scores.append(value + bonus)
    return scores
