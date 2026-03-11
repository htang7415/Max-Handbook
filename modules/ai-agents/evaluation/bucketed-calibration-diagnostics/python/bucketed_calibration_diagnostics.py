from __future__ import annotations


def confidence_bucket_index(confidence: float, bucket_count: int) -> int:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must satisfy 0 <= value <= 1")
    if bucket_count <= 0:
        raise ValueError("bucket_count must be positive")
    if confidence == 1.0:
        return bucket_count - 1
    return int(confidence * bucket_count)


def bucketed_calibration_table(
    confidences: list[float],
    outcomes: list[bool],
    bucket_count: int,
) -> list[dict[str, object]]:
    if not confidences or not outcomes:
        raise ValueError("confidences and outcomes must be non-empty")
    if len(confidences) != len(outcomes):
        raise ValueError("confidences and outcomes must have the same length")
    if bucket_count <= 0:
        raise ValueError("bucket_count must be positive")

    buckets = [
        {
            "bucket": bucket_index,
            "count": 0,
            "mean_confidence": 0.0,
            "accuracy": 0.0,
            "gap": 0.0,
        }
        for bucket_index in range(bucket_count)
    ]

    confidence_sums = [0.0] * bucket_count
    success_sums = [0] * bucket_count
    for confidence, outcome in zip(confidences, outcomes):
        bucket_index = confidence_bucket_index(confidence, bucket_count)
        buckets[bucket_index]["count"] = int(buckets[bucket_index]["count"]) + 1
        confidence_sums[bucket_index] += confidence
        success_sums[bucket_index] += int(outcome)

    for bucket_index, bucket in enumerate(buckets):
        count = int(bucket["count"])
        if count == 0:
            continue
        mean_confidence = confidence_sums[bucket_index] / count
        accuracy = success_sums[bucket_index] / count
        bucket["mean_confidence"] = mean_confidence
        bucket["accuracy"] = accuracy
        bucket["gap"] = abs(mean_confidence - accuracy)

    return buckets


def expected_calibration_error(
    confidences: list[float],
    outcomes: list[bool],
    bucket_count: int,
) -> float:
    table = bucketed_calibration_table(confidences, outcomes, bucket_count)
    total = sum(int(bucket["count"]) for bucket in table)
    if total == 0:
        raise ValueError("at least one bucket count is required")

    return sum(
        int(bucket["count"]) / total * float(bucket["gap"])
        for bucket in table
        if int(bucket["count"]) > 0
    )


def calibration_diagnostic_route(ece: float, max_ece: float) -> str:
    if not 0.0 <= ece <= 1.0:
        raise ValueError("ece must satisfy 0 <= value <= 1")
    if not 0.0 <= max_ece <= 1.0:
        raise ValueError("max_ece must satisfy 0 <= value <= 1")
    if ece > max_ece:
        return "review"
    return "pass"
