from __future__ import annotations


def l1_penalty(weights: list[float], lam: float) -> float:
    return round(lam * sum(abs(weight) for weight in weights), 10)


def l2_penalty(weights: list[float], lam: float) -> float:
    return lam * sum(weight * weight for weight in weights)


def weight_decay_step(w: float, grad: float, lr: float, lam: float) -> float:
    return w - lr * (grad + lam * w)


def dropout(x: list[float], p: float, seed: int = 0) -> list[float]:
    if not 0.0 <= p < 1.0:
        raise ValueError("p must satisfy 0 <= p < 1")

    out: list[float] = []
    state = seed
    for value in x:
        state = (1103515245 * state + 12345) % (2**31)
        keep = (state / (2**31 - 1)) > p
        out.append(value / (1 - p) if keep else 0.0)
    return out


def should_stop(losses: list[float], patience: int) -> bool:
    best = float("inf")
    bad = 0
    for loss in losses:
        if loss < best:
            best = loss
            bad = 0
        else:
            bad += 1
            if bad >= patience:
                return True
    return False
