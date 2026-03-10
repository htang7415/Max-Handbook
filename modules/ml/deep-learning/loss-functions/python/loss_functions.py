from __future__ import annotations

import math


def softmax_probs(logits: list[float]) -> list[float]:
    if not logits:
        raise ValueError("logits must be non-empty")
    maximum = max(logits)
    exps = [math.exp(value - maximum) for value in logits]
    total = sum(exps)
    return [value / total for value in exps]


def cross_entropy(logits: list[float], target: int) -> float:
    if target < 0 or target >= len(logits):
        raise ValueError("target must be a valid logit index")
    probability = softmax_probs(logits)[target]
    return -math.log(probability)


def focal_loss(p: float, gamma: float = 2.0) -> float:
    if not 0.0 < p <= 1.0:
        raise ValueError("p must satisfy 0 < p <= 1")
    if gamma < 0.0:
        raise ValueError("gamma must be non-negative")
    return -((1 - p) ** gamma) * math.log(p)


def hinge_loss(score: float, label: int) -> float:
    if label not in (-1, 1):
        raise ValueError("label must be either -1 or 1")
    return max(0.0, 1 - label * score)


def huber(y: float, y_hat: float, delta: float = 1.0) -> float:
    if delta <= 0.0:
        raise ValueError("delta must be positive")
    error = y - y_hat
    if abs(error) <= delta:
        return 0.5 * error * error
    return delta * (abs(error) - 0.5 * delta)


def residuals(y: list[float], y_hat: list[float]) -> list[float]:
    if len(y) != len(y_hat):
        raise ValueError("y and y_hat must have the same length")
    return [truth - pred for truth, pred in zip(y, y_hat)]


def mae(y: list[float], y_hat: list[float]) -> float:
    if not y:
        raise ValueError("inputs must be non-empty")
    return sum(abs(error) for error in residuals(y, y_hat)) / len(y)


def mse(y: list[float], y_hat: list[float]) -> float:
    if not y:
        raise ValueError("inputs must be non-empty")
    return sum(error * error for error in residuals(y, y_hat)) / len(y)


def rmse(y: list[float], y_hat: list[float]) -> float:
    return math.sqrt(mse(y, y_hat))
