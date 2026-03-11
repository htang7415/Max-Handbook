from __future__ import annotations

import math


def _validate_rate(rate: float, name: str) -> None:
    if not 0.0 < rate < 1.0:
        raise ValueError(f"{name} must satisfy 0 < value < 1")


def sprt_log_likelihood_ratio(successes: int, failures: int, null_rate: float, alt_rate: float) -> float:
    if successes < 0 or failures < 0:
        raise ValueError("successes and failures must be non-negative")
    _validate_rate(null_rate, "null_rate")
    _validate_rate(alt_rate, "alt_rate")
    if null_rate == alt_rate:
        raise ValueError("null_rate and alt_rate must differ")

    return successes * math.log(alt_rate / null_rate) + failures * math.log(
        (1.0 - alt_rate) / (1.0 - null_rate)
    )


def sprt_boundaries(alpha: float, beta: float) -> dict[str, float]:
    _validate_rate(alpha, "alpha")
    _validate_rate(beta, "beta")
    return {
        "upper": math.log((1.0 - beta) / alpha),
        "lower": math.log(beta / (1.0 - alpha)),
    }


def sprt_route(log_likelihood_ratio: float, upper_boundary: float, lower_boundary: float) -> str:
    if lower_boundary >= upper_boundary:
        raise ValueError("lower_boundary must be smaller than upper_boundary")
    if log_likelihood_ratio >= upper_boundary:
        return "accept-alt"
    if log_likelihood_ratio <= lower_boundary:
        return "accept-null"
    return "continue"
