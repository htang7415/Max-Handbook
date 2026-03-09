from __future__ import annotations

import math


def cosine_restart_lr(base_lr: float, step: int, cycle_length: int) -> float:
    if base_lr < 0.0:
        raise ValueError("base_lr must be non-negative")
    if step < 0:
        raise ValueError("step must be non-negative")
    if cycle_length <= 0:
        raise ValueError("cycle_length must be positive")

    position = step % cycle_length
    return base_lr * 0.5 * (1.0 + math.cos(math.pi * position / cycle_length))
