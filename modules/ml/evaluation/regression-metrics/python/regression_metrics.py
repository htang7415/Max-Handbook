from __future__ import annotations


def mae_mse(y_true: list[float], y_pred: list[float]) -> tuple[float, float]:
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if not y_true:
        return 0.0, 0.0

    mae = sum(abs(truth - pred) for truth, pred in zip(y_true, y_pred)) / len(y_true)
    mse = sum((truth - pred) ** 2 for truth, pred in zip(y_true, y_pred)) / len(y_true)
    return mae, mse


def r2_score(y_true: list[float], y_pred: list[float]) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if not y_true:
        return 0.0

    mean = sum(y_true) / len(y_true)
    ss_res = sum((truth - pred) ** 2 for truth, pred in zip(y_true, y_pred))
    ss_tot = sum((truth - mean) ** 2 for truth in y_true)
    return 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
