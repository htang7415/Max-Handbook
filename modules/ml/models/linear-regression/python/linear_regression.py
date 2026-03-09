def predict(x: list[float], w: list[float], b: float) -> float:
    if len(x) != len(w):
        raise ValueError("x and w must have the same length")

    return sum(wi * xi for wi, xi in zip(w, x)) + b
