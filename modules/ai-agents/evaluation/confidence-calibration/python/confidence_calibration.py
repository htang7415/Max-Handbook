from __future__ import annotations


def mean_confidence(confidences: list[float]) -> float:
    if not confidences:
        raise ValueError("confidences must be non-empty")
    if any(confidence < 0.0 or confidence > 1.0 for confidence in confidences):
        raise ValueError("confidences must satisfy 0 <= value <= 1")
    return sum(confidences) / len(confidences)


def observed_accuracy(outcomes: list[bool]) -> float:
    if not outcomes:
        raise ValueError("outcomes must be non-empty")
    return sum(1 for outcome in outcomes if outcome) / len(outcomes)


def calibration_gap(mean_confidence_value: float, observed_accuracy_value: float) -> float:
    if not 0.0 <= mean_confidence_value <= 1.0:
        raise ValueError("mean_confidence_value must satisfy 0 <= value <= 1")
    if not 0.0 <= observed_accuracy_value <= 1.0:
        raise ValueError("observed_accuracy_value must satisfy 0 <= value <= 1")
    return abs(mean_confidence_value - observed_accuracy_value)


def calibration_route(
    mean_confidence_value: float,
    observed_accuracy_value: float,
    max_gap: float,
    min_accuracy: float,
) -> str:
    if max_gap < 0.0:
        raise ValueError("max_gap must be non-negative")
    if not 0.0 <= min_accuracy <= 1.0:
        raise ValueError("min_accuracy must satisfy 0 <= value <= 1")

    gap = calibration_gap(mean_confidence_value, observed_accuracy_value)
    if observed_accuracy_value < min_accuracy:
        return "review"
    if gap > max_gap:
        return "review"
    return "pass"
