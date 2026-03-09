from __future__ import annotations

import math


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
