import math


def add_noise(x: float, noise: float, alpha: float) -> float:
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must satisfy 0 <= alpha <= 1")

    return math.sqrt(alpha) * x + math.sqrt(1 - alpha) * noise
