def dropout(x: list[float], p: float, seed: int = 0) -> list[float]:
    if not 0.0 <= p < 1.0:
        raise ValueError("p must satisfy 0 <= p < 1")

    out = []
    state = seed
    for v in x:
        state = (1103515245 * state + 12345) % (2**31)
        keep = (state / (2**31 - 1)) > p
        out.append(v / (1 - p) if keep else 0.0)
    return out
