from __future__ import annotations


def chi_square_feature_score(
    present_positive: int,
    present_negative: int,
    absent_positive: int,
    absent_negative: int,
) -> float:
    counts = [present_positive, present_negative, absent_positive, absent_negative]
    if any(count < 0 for count in counts):
        raise ValueError("counts must be non-negative")

    total = sum(counts)
    if total == 0:
        return 0.0

    present_total = present_positive + present_negative
    absent_total = absent_positive + absent_negative
    positive_total = present_positive + absent_positive
    negative_total = present_negative + absent_negative

    observed = [
        present_positive,
        present_negative,
        absent_positive,
        absent_negative,
    ]
    expected = [
        present_total * positive_total / total,
        present_total * negative_total / total,
        absent_total * positive_total / total,
        absent_total * negative_total / total,
    ]

    score = 0.0
    for observed_count, expected_count in zip(observed, expected):
        if expected_count > 0.0:
            score += (observed_count - expected_count) ** 2 / expected_count
    return score
