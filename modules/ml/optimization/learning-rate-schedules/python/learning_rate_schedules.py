from __future__ import annotations

import math


def constant_lr(lr: float) -> float:
    return lr


def step_decay(lr: float, step: int, gamma: float, t: int) -> float:
    return lr * (gamma ** (t // step))


def exp_decay(lr: float, k: float, t: float) -> float:
    return lr * math.exp(-k * t)


def cosine_decay(lr: float, t: int, t_max: int) -> float:
    return lr * 0.5 * (1 + math.cos(math.pi * t / t_max))


def warmup_lr(lr: float, t: int, warmup_steps: int) -> float:
    return lr * min(1.0, t / warmup_steps)


def cosine_restart_lr(base_lr: float, step: int, cycle_length: int) -> float:
    if base_lr < 0.0:
        raise ValueError("base_lr must be non-negative")
    if step < 0:
        raise ValueError("step must be non-negative")
    if cycle_length <= 0:
        raise ValueError("cycle_length must be positive")
    position = step % cycle_length
    return base_lr * 0.5 * (1.0 + math.cos(math.pi * position / cycle_length))


def warmup_cosine_lr(
    base_lr: float,
    step: int,
    warmup_steps: int,
    total_steps: int,
) -> float:
    if base_lr < 0.0:
        raise ValueError("base_lr must be non-negative")
    if step < 0:
        raise ValueError("step must be non-negative")
    if warmup_steps < 0:
        raise ValueError("warmup_steps must be non-negative")
    if total_steps <= 0:
        raise ValueError("total_steps must be positive")
    if warmup_steps > total_steps:
        raise ValueError("warmup_steps cannot exceed total_steps")

    if warmup_steps > 0 and step < warmup_steps:
        return base_lr * step / warmup_steps
    if total_steps == warmup_steps:
        return base_lr

    progress = (step - warmup_steps) / (total_steps - warmup_steps)
    progress = min(max(progress, 0.0), 1.0)
    return 0.5 * base_lr * (1.0 + math.cos(math.pi * progress))


def one_cycle_lr(
    max_lr: float,
    step: int,
    total_steps: int,
    pct_start: float = 0.3,
    div_factor: float = 25.0,
    final_div_factor: float = 1.0e4,
) -> float:
    if max_lr <= 0.0:
        raise ValueError("max_lr must be positive")
    if step < 0:
        raise ValueError("step must be non-negative")
    if total_steps <= 0:
        raise ValueError("total_steps must be positive")
    if not 0.0 < pct_start < 1.0:
        raise ValueError("pct_start must satisfy 0 < pct_start < 1")
    if div_factor <= 0.0 or final_div_factor <= 0.0:
        raise ValueError("div_factor and final_div_factor must be positive")

    if total_steps == 1:
        return max_lr

    initial_lr = max_lr / div_factor
    final_lr = initial_lr / final_div_factor
    last_step = total_steps - 1
    step = min(step, last_step)
    up_steps = max(1, int(last_step * pct_start))

    if step <= up_steps:
        progress = step / up_steps
        return initial_lr + progress * (max_lr - initial_lr)

    down_steps = last_step - up_steps
    progress = (step - up_steps) / down_steps
    cosine_weight = 0.5 * (1.0 + math.cos(math.pi * progress))
    return final_lr + cosine_weight * (max_lr - final_lr)
