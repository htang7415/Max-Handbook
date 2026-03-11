from __future__ import annotations

import math


def momentum_velocity(grad: float, v: float, mu: float) -> float:
    if not 0.0 <= mu <= 1.0:
        raise ValueError("mu must satisfy 0 <= mu <= 1")
    return mu * v + grad


def sgd_step(w: float, grad: float, lr: float) -> float:
    if lr < 0.0:
        raise ValueError("lr must be non-negative")
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
    if lr < 0.0:
        raise ValueError("lr must be non-negative")
    if g2 < 0.0:
        raise ValueError("g2 must be non-negative")
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    g2 = g2 + grad**2
    w = w - lr * grad / (math.sqrt(g2) + eps)
    return w, g2


def rmsprop_step(w: float, grad: float, v: float, lr: float, beta: float, eps: float) -> tuple[float, float]:
    if lr < 0.0:
        raise ValueError("lr must be non-negative")
    if not 0.0 <= beta <= 1.0:
        raise ValueError("beta must satisfy 0 <= beta <= 1")
    if v < 0.0:
        raise ValueError("v must be non-negative")
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    v = beta * v + (1 - beta) * (grad**2)
    w = w - lr * grad / (math.sqrt(v) + eps)
    return w, v


def adam_step(
    w: float, grad: float, m: float, v: float, lr: float, beta1: float, beta2: float, eps: float
) -> tuple[float, float, float]:
    if lr < 0.0:
        raise ValueError("lr must be non-negative")
    if not 0.0 <= beta1 <= 1.0 or not 0.0 <= beta2 <= 1.0:
        raise ValueError("beta1 and beta2 must satisfy 0 <= value <= 1")
    if v < 0.0:
        raise ValueError("v must be non-negative")
    if eps <= 0.0:
        raise ValueError("eps must be positive")
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
    if wd < 0.0:
        raise ValueError("wd must be non-negative")
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * (grad**2)
    w = w - lr * m / (math.sqrt(v) + eps) - weight_decay_term(w, lr=lr, wd=wd)
    return w, m, v


def weight_decay_term(w: float, lr: float, wd: float) -> float:
    if lr < 0.0:
        raise ValueError("lr must be non-negative")
    if wd < 0.0:
        raise ValueError("wd must be non-negative")
    return lr * wd * w
