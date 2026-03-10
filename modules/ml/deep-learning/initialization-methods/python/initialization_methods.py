from __future__ import annotations

import math


def xavier_limit(fan_in: int, fan_out: int) -> float:
    if fan_in <= 0 or fan_out <= 0:
        raise ValueError("fan_in and fan_out must be positive")
    return math.sqrt(6 / (fan_in + fan_out))


def xavier_uniform(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
    limit = xavier_limit(fan_in, fan_out)
    values: list[float] = []
    state = seed
    for _ in range(fan_in * fan_out):
        state = (1103515245 * state + 12345) % (2**31)
        values.append(-limit + (state / (2**31 - 1)) * (2 * limit))
    return values


def he_std(fan_in: int) -> float:
    if fan_in <= 0:
        raise ValueError("fan_in must be positive")
    return math.sqrt(2 / fan_in)


def he_normal(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
    if fan_out <= 0:
        raise ValueError("fan_out must be positive")
    std = he_std(fan_in)
    values: list[float] = []
    state = seed
    for _ in range(fan_in * fan_out // 2 + 1):
        state = (1103515245 * state + 12345) % (2**31)
        u1 = (state / (2**31 - 1)) or 1e-6
        state = (1103515245 * state + 12345) % (2**31)
        u2 = state / (2**31 - 1)
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        values.extend([z0 * std, z1 * std])
    return values[: fan_in * fan_out]
