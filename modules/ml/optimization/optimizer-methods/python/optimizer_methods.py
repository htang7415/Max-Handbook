from __future__ import annotations

import math


def sgd_step(w: float, grad: float, lr: float) -> float:
    return w - lr * grad


def momentum_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
    v = mu * v + grad
    w = w - lr * v
    return w, v


def nesterov_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
    v_new = mu * v + grad
    w_new = w - lr * (mu * v_new + grad)
    return w_new, v_new


def adagrad_step(w: float, grad: float, g2: float, lr: float, eps: float) -> tuple[float, float]:
    g2 = g2 + grad**2
    w = w - lr * grad / (math.sqrt(g2) + eps)
    return w, g2


def rmsprop_step(w: float, grad: float, v: float, lr: float, beta: float, eps: float) -> tuple[float, float]:
    v = beta * v + (1 - beta) * (grad**2)
    w = w - lr * grad / (math.sqrt(v) + eps)
    return w, v


def adam_step(
    w: float, grad: float, m: float, v: float, lr: float, beta1: float, beta2: float, eps: float
) -> tuple[float, float, float]:
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * (grad**2)
    w = w - lr * m / (math.sqrt(v) + eps)
    return w, m, v


def adamw_step(
    w: float,
    grad: float,
    m: float,
    v: float,
    lr: float,
    wd: float,
    beta1: float,
    beta2: float,
    eps: float,
) -> tuple[float, float, float]:
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * (grad**2)
    w = w - lr * m / (math.sqrt(v) + eps) - lr * wd * w
    return w, m, v
