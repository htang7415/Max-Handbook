from __future__ import annotations


def select_regression_cases(
    changed_paths: list[str],
    historical_case_map: dict[str, list[str]],
    recent_bugfix_case_ids: list[str] | None = None,
    touches_generated_code: bool = False,
) -> list[str]:
    normalized_paths = [path.strip().lower() for path in changed_paths if path.strip()]
    selected = {"smoke"}

    for marker, case_ids in historical_case_map.items():
        lowered_marker = marker.strip().lower()
        if lowered_marker and any(lowered_marker in path for path in normalized_paths):
            selected.update(case_ids)

    if recent_bugfix_case_ids:
        selected.update(case_id.strip() for case_id in recent_bugfix_case_ids if case_id.strip())
    if touches_generated_code:
        selected.add("generated-output-drift")

    return sorted(selected)


def missing_regression_cases(required_case_ids: list[str], executed_case_ids: list[str]) -> list[str]:
    required = {case_id.strip() for case_id in required_case_ids if case_id.strip()}
    executed = {case_id.strip() for case_id in executed_case_ids if case_id.strip()}
    return sorted(required - executed)


def release_ready(required_case_ids: list[str], passed_case_ids: list[str]) -> bool:
    return not missing_regression_cases(required_case_ids, passed_case_ids)
