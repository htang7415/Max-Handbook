def mae(y: list[float], y_hat: list[float]) -> float:
    if len(y) != len(y_hat):
        raise ValueError("y and y_hat must have the same length")
    if not y:
        raise ValueError("inputs must be non-empty")

    return sum(abs(a - b) for a, b in zip(y, y_hat)) / len(y)
