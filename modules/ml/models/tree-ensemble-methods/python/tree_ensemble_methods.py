from __future__ import annotations

import math
from collections import Counter


def class_probabilities(labels: list[int]) -> list[float]:
    if not labels:
        return []
    counts = Counter(labels)
    n = len(labels)
    return [count / n for count in counts.values()]


def gini_impurity(labels: list[int]) -> float:
    if not labels:
        return 0.0
    return 1 - sum(probability**2 for probability in class_probabilities(labels))


def bootstrap_indices(n: int, seed: int = 0) -> list[int]:
    if n <= 0:
        raise ValueError("n must be positive")
    indices: list[int] = []
    state = seed
    for _ in range(n):
        state = (1103515245 * state + 12345) % (2**31)
        indices.append(state % n)
    return indices


def update_weights(weights: list[float], errors: list[int], alpha: float) -> list[float]:
    if len(weights) != len(errors):
        raise ValueError("weights and errors must have the same length")
    if any(weight < 0.0 for weight in weights):
        raise ValueError("weights must be non-negative")
    updated = [weight * math.exp(alpha * error) for weight, error in zip(weights, errors)]
    total = sum(updated)
    if total == 0.0:
        raise ValueError("updated weights must sum to a positive value")
    return [weight / total for weight in updated]


def gradient_boosting_step(
    targets: list[float],
    predictions: list[float],
    weak_learner_output: list[float],
    learning_rate: float,
) -> tuple[list[float], list[float]]:
    if len(targets) != len(predictions) or len(predictions) != len(weak_learner_output):
        raise ValueError("targets, predictions, and weak_learner_output must have the same length")
    if learning_rate < 0.0:
        raise ValueError("learning_rate must be non-negative")

    updated = [
        prediction + learning_rate * stage
        for prediction, stage in zip(predictions, weak_learner_output)
    ]
    residuals = boosting_residuals(targets, updated)
    return updated, residuals


def boosting_residuals(targets: list[float], predictions: list[float]) -> list[float]:
    if len(targets) != len(predictions):
        raise ValueError("targets and predictions must have the same length")
    return [target - prediction for target, prediction in zip(targets, predictions)]


def split_gain(
    left_grad: float,
    left_hess: float,
    right_grad: float,
    right_hess: float,
    lambda_reg: float,
    gamma: float,
) -> float:
    if left_hess < 0.0 or right_hess < 0.0 or lambda_reg < 0.0:
        raise ValueError("hessians and lambda_reg must be non-negative")

    parent_grad = left_grad + right_grad
    parent_hess = left_hess + right_hess

    left_term = (left_grad ** 2) / (left_hess + lambda_reg)
    right_term = (right_grad ** 2) / (right_hess + lambda_reg)
    parent_term = (parent_grad ** 2) / (parent_hess + lambda_reg)
    return 0.5 * (left_term + right_term - parent_term) - gamma
