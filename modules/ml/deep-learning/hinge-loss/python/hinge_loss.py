def hinge_loss(score: float, label: int) -> float:
    if label not in (-1, 1):
        raise ValueError("label must be either -1 or 1")

    return max(0.0, 1 - label * score)
