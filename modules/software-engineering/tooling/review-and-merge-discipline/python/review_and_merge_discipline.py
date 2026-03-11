from __future__ import annotations


def review_requirement(changed_paths: list[str], lines_changed: int) -> str:
    if lines_changed < 0:
        raise ValueError("lines_changed must be non-negative")

    normalized_paths = [path.strip().lower() for path in changed_paths if path.strip()]
    sensitive_markers = ("auth", "permission", "billing", "payment", "security", "secret")

    if any(marker in path for path in normalized_paths for marker in sensitive_markers):
        return "security-review"
    if lines_changed >= 300 or len(normalized_paths) >= 8:
        return "senior-review"
    return "standard-review"


def ready_for_merge(
    open_threads: int,
    checks_passed: bool,
    approvals: int,
    required_approvals: int = 1,
) -> bool:
    if open_threads < 0 or approvals < 0 or required_approvals <= 0:
        raise ValueError("review counts must be non-negative and required_approvals positive")
    return open_threads == 0 and checks_passed and approvals >= required_approvals


def merge_decision(
    changed_paths: list[str],
    lines_changed: int,
    checks_passed: bool,
    open_threads: int,
    approvals: int,
) -> str:
    requirement = review_requirement(changed_paths, lines_changed)
    required_approvals = 2 if requirement == "security-review" else 1

    if not ready_for_merge(open_threads, checks_passed, approvals, required_approvals):
        return "block"
    return "merge"
