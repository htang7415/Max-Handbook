from __future__ import annotations


def make_change_request(
    task: str,
    constraints: list[str],
    acceptance_checks: list[str],
) -> dict[str, object]:
    cleaned_task = task.strip()
    if not cleaned_task:
        raise ValueError("task must be non-empty")

    cleaned_constraints = [constraint.strip() for constraint in constraints if constraint.strip()]
    cleaned_checks = [check.strip() for check in acceptance_checks if check.strip()]
    if not cleaned_checks:
        raise ValueError("acceptance_checks must include at least one non-empty item")

    return {
        "task": cleaned_task,
        "constraints": cleaned_constraints,
        "acceptance_checks": cleaned_checks,
    }


def next_stage(patch_ready: bool, checks_passed: bool, review_signed_off: bool) -> str:
    if not patch_ready:
        return "draft_patch"
    if not checks_passed:
        return "run_checks"
    if not review_signed_off:
        return "human_review"
    return "ship"


def review_risk(changed_paths: list[str], touches_generated_code: bool = False) -> str:
    cleaned_paths = [path.strip().lower() for path in changed_paths if path.strip()]
    sensitive_markers = ("auth", "permission", "billing", "payment", "secret", "migration", "security")

    if touches_generated_code:
        return "high"
    if any(marker in path for path in cleaned_paths for marker in sensitive_markers):
        return "high"
    if len(cleaned_paths) >= 6:
        return "medium"
    return "low"
