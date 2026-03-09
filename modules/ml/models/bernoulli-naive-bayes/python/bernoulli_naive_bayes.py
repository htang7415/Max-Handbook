import math


def bernoulli_log_likelihood(x: list[int], prob: list[float]) -> float:
    if len(x) != len(prob):
        raise ValueError("x and prob must have the same length")

    ll = 0.0
    for xi, p in zip(x, prob):
        if xi not in (0, 1):
            raise ValueError("x must contain only binary values")
        if not 0.0 < p < 1.0:
            raise ValueError("probabilities must be strictly between 0 and 1")
        ll += xi * math.log(p) + (1 - xi) * math.log(1 - p)
    return ll
