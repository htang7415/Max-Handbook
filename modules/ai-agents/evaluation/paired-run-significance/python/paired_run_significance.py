from __future__ import annotations


def paired_outcome_counts(baseline: list[bool], candidate: list[bool]) -> dict[str, int]:
    if not baseline or not candidate:
        raise ValueError("baseline and candidate must be non-empty")
    if len(baseline) != len(candidate):
        raise ValueError("baseline and candidate must have the same length")

    counts = {
        "both_success": 0,
        "baseline_only": 0,
        "candidate_only": 0,
        "both_fail": 0,
    }
    for baseline_ok, candidate_ok in zip(baseline, candidate):
        if baseline_ok and candidate_ok:
            counts["both_success"] += 1
        elif baseline_ok and not candidate_ok:
            counts["baseline_only"] += 1
        elif not baseline_ok and candidate_ok:
            counts["candidate_only"] += 1
        else:
            counts["both_fail"] += 1
    return counts


def mcnemar_statistic(baseline_only: int, candidate_only: int) -> float:
    if baseline_only < 0 or candidate_only < 0:
        raise ValueError("discordant counts must be non-negative")

    discordant = baseline_only + candidate_only
    if discordant == 0:
        return 0.0
    return (abs(baseline_only - candidate_only) - 1) ** 2 / discordant


def paired_significance_route(counts: dict[str, int], threshold: float) -> str:
    if threshold < 0.0:
        raise ValueError("threshold must be non-negative")
    required_keys = {"both_success", "baseline_only", "candidate_only", "both_fail"}
    if set(counts) != required_keys:
        raise ValueError("counts must include both_success, baseline_only, candidate_only, both_fail")

    statistic = mcnemar_statistic(
        int(counts["baseline_only"]),
        int(counts["candidate_only"]),
    )
    if statistic < threshold:
        return "inconclusive"
    if int(counts["candidate_only"]) > int(counts["baseline_only"]):
        return "candidate-better"
    if int(counts["candidate_only"]) < int(counts["baseline_only"]):
        return "baseline-better"
    return "inconclusive"
