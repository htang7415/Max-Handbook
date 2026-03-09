from __future__ import annotations


def ks_drift_score(reference: list[float], current: list[float]) -> float:
    if not reference or not current:
        raise ValueError("reference and current must be non-empty")

    reference_sorted = sorted(reference)
    current_sorted = sorted(current)
    all_values = sorted(set(reference_sorted + current_sorted))

    reference_index = 0
    current_index = 0
    max_difference = 0.0

    for value in all_values:
        while reference_index < len(reference_sorted) and reference_sorted[reference_index] <= value:
            reference_index += 1
        while current_index < len(current_sorted) and current_sorted[current_index] <= value:
            current_index += 1

        reference_cdf = reference_index / len(reference_sorted)
        current_cdf = current_index / len(current_sorted)
        max_difference = max(max_difference, abs(reference_cdf - current_cdf))

    return max_difference


def drift_detected(reference: list[float], current: list[float], threshold: float = 0.2) -> bool:
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must satisfy 0 <= threshold <= 1")

    return ks_drift_score(reference, current) > threshold
