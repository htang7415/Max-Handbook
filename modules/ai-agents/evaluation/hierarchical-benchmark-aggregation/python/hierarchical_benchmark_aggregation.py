from __future__ import annotations


def weighted_group_score(bucket_to_metrics: dict[str, dict[str, float]]) -> dict[str, float]:
    if not bucket_to_metrics:
        raise ValueError("bucket_to_metrics must be non-empty")

    weighted_sum = 0.0
    total_weight = 0.0
    for bucket_name, metrics in bucket_to_metrics.items():
        cleaned_name = bucket_name.strip()
        if not cleaned_name:
            raise ValueError("bucket names must be non-empty")
        score = float(metrics.get("score", 0.0))
        weight = float(metrics.get("weight", 0.0))
        if not 0.0 <= score <= 1.0:
            raise ValueError("bucket scores must satisfy 0 <= value <= 1")
        if weight <= 0.0:
            raise ValueError("bucket weights must be positive")
        weighted_sum += score * weight
        total_weight += weight

    return {
        "score": weighted_sum / total_weight,
        "weight": total_weight,
    }


def hierarchical_benchmark_summary(group_to_buckets: dict[str, dict[str, dict[str, float]]]) -> dict[str, object]:
    if not group_to_buckets:
        raise ValueError("group_to_buckets must be non-empty")

    group_scores: dict[str, float] = {}
    total_weighted_score = 0.0
    total_weight = 0.0
    for group_name, buckets in group_to_buckets.items():
        cleaned_name = group_name.strip()
        if not cleaned_name:
            raise ValueError("group names must be non-empty")
        group_summary = weighted_group_score(buckets)
        group_scores[cleaned_name] = group_summary["score"]
        total_weighted_score += group_summary["score"] * group_summary["weight"]
        total_weight += group_summary["weight"]

    return {
        "group_scores": group_scores,
        "overall_score": total_weighted_score / total_weight,
    }


def hierarchical_benchmark_route(
    summary: dict[str, object],
    min_overall_score: float,
    min_group_score: float,
) -> str:
    if not 0.0 <= min_overall_score <= 1.0:
        raise ValueError("min_overall_score must satisfy 0 <= value <= 1")
    if not 0.0 <= min_group_score <= 1.0:
        raise ValueError("min_group_score must satisfy 0 <= value <= 1")
    overall_score = float(summary.get("overall_score", -1.0))
    group_scores = summary.get("group_scores")
    if not isinstance(group_scores, dict) or not group_scores:
        raise ValueError("summary.group_scores must be a non-empty dict")
    if not 0.0 <= overall_score <= 1.0:
        raise ValueError("summary.overall_score must satisfy 0 <= value <= 1")

    if overall_score < min_overall_score:
        return "fail"
    if any(float(score) < min_group_score for score in group_scores.values()):
        return "review"
    return "pass"
