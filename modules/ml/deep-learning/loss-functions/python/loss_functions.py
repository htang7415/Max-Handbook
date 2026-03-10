from __future__ import annotations

import math


def cross_entropy(logits: list[float], target: int) -> float:
    maximum = max(logits)
    exps = [math.exp(value - maximum) for value in logits]
    total = sum(exps)
    probability = exps[target] / total
    return -math.log(probability)


def focal_loss(p: float, gamma: float = 2.0) -> float:
    return -((1 - p) ** gamma) * math.log(p)


def hinge_loss(score: float, label: int) -> float:
    if label not in (-1, 1):
        raise ValueError("label must be either -1 or 1")
    return max(0.0, 1 - label * score)


def huber(y: float, y_hat: float, delta: float = 1.0) -> float:
    error = y - y_hat
    if abs(error) <= delta:
        return 0.5 * error * error
    return delta * (abs(error) - 0.5 * delta)


def mae(y: list[float], y_hat: list[float]) -> float:
    if len(y) != len(y_hat):
        raise ValueError("y and y_hat must have the same length")
    if not y:
        raise ValueError("inputs must be non-empty")
    return sum(abs(truth - pred) for truth, pred in zip(y, y_hat)) / len(y)


def mse(y: list[float], y_hat: list[float]) -> float:
    if len(y) != len(y_hat):
        raise ValueError("y and y_hat must have the same length")
    if not y:
        raise ValueError("inputs must be non-empty")
    return sum((truth - pred) ** 2 for truth, pred in zip(y, y_hat)) / len(y)


def rmse(y: list[float], y_hat: list[float]) -> float:
    return math.sqrt(mse(y, y_hat))
