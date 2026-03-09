import math


def gaussian_log_likelihood(x: list[float], mean: list[float], var: list[float]) -> float:
    if len(x) != len(mean) or len(mean) != len(var):
        raise ValueError("x, mean, and var must have the same length")

    ll = 0.0
    for xi, mu, v in zip(x, mean, var):
        if v <= 0:
            raise ValueError("variances must be positive")
        ll += -0.5 * (math.log(2 * math.pi * v) + ((xi - mu) ** 2) / v)
    return ll
