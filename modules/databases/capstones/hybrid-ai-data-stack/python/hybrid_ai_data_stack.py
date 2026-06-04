from __future__ import annotations


REQUIRED_CHECKS = [
    "source_constraints",
    "cdc_watermark_fresh",
    "analytics_backfill_ready",
    "retrieval_permissions_filtered",
    "retrieval_eval_passed",
]


def route_data_request(
    needs_transaction: bool,
    needs_similarity: bool,
    needs_large_scan: bool,
    needs_fresh_read: bool = False,
) -> str:
    if needs_transaction or needs_fresh_read:
        return "source-of-truth"
    if needs_similarity:
        return "retrieval-layer"
    if needs_large_scan:
        return "analytics-layer"
    return "read-replica-or-cache"


def stack_readiness(checks: dict[str, bool]) -> dict[str, object]:
    missing = [name for name in REQUIRED_CHECKS if name not in checks]
    if missing:
        raise ValueError(f"missing checks: {', '.join(missing)}")

    failed = [name for name in REQUIRED_CHECKS if not bool(checks[name])]
    return {
        "ready": not failed,
        "failed_checks": failed,
        "passed_checks": [name for name in REQUIRED_CHECKS if name not in failed],
    }


def release_gate(
    readiness: dict[str, object],
    max_cdc_lag_seconds: int,
    observed_cdc_lag_seconds: int,
) -> dict[str, object]:
    if max_cdc_lag_seconds < 0:
        raise ValueError("max_cdc_lag_seconds must be non-negative")
    if observed_cdc_lag_seconds < 0:
        raise ValueError("observed_cdc_lag_seconds must be non-negative")

    reasons = list(readiness.get("failed_checks", []))
    if observed_cdc_lag_seconds > max_cdc_lag_seconds:
        reasons.append("cdc-lag-over-budget")

    return {
        "decision": "ship" if not reasons else "hold",
        "reasons": reasons,
        "cdc_lag_seconds": observed_cdc_lag_seconds,
    }
