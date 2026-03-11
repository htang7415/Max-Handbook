from __future__ import annotations


def recommended_output_test(stable_output: bool, large_structured_output: bool) -> str:
    if stable_output and large_structured_output:
        return "snapshot"
    if stable_output:
        return "golden"
    return "assert-specific-fields"


def snapshot_noise_risk(changed_lines: int, has_nondeterministic_values: bool) -> str:
    if changed_lines < 0:
        raise ValueError("changed_lines must be non-negative")
    if has_nondeterministic_values:
        return "high"
    if changed_lines >= 25:
        return "medium"
    return "low"


def snapshot_update_allowed(
    changed_lines: int,
    has_nondeterministic_values: bool,
    reviewer_signed_off: bool,
) -> bool:
    risk = snapshot_noise_risk(changed_lines, has_nondeterministic_values)
    if risk == "high":
        return False
    if risk == "medium":
        return reviewer_signed_off
    return reviewer_signed_off
