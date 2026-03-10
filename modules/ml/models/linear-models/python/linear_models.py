from __future__ import annotations

import math


def linear_predict(x: list[float], w: list[float], b: float) -> float:
    if len(x) != len(w):
        raise ValueError("x and w must have the same length")
    return sum(weight * value for weight, value in zip(w, x)) + b


def logistic_predict_proba(x: list[float], w: list[float], b: float) -> float:
    z = linear_predict(x, w, b)
    return 1 / (1 + math.exp(-z))


def softmax_probabilities(logits: list[float]) -> list[float]:
    maximum = max(logits)
    exps = [math.exp(value - maximum) for value in logits]
    total = sum(exps)
    return [value / total for value in exps]


def elastic_net_penalty(weights: list[float], l1: float, l2: float) -> float:
    return l1 * sum(abs(value) for value in weights) + l2 * sum(value * value for value in weights)
