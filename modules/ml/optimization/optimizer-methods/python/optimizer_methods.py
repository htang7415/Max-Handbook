from __future__ import annotations

import math


def momentum_velocity(grad: float, v: float, mu: float) -> float:
    return mu * v + grad


def sgd_step(w: float, grad: float, lr: float) -> float:
    return w - lr * grad


def momentum_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
    v = momentum_velocity(grad, v, mu)
    w = w - lr * v
    return w, v


def nesterov_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
    v_new = momentum_velocity(grad, v, mu)
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
    w = w - lr * m / (math.sqrt(v) + eps) - weight_decay_term(w, lr=lr, wd=wd)
    return w, m, v


def weight_decay_term(w: float, lr: float, wd: float) -> float:
    return lr * wd * w
