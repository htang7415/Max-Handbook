from __future__ import annotations


def optimistic_write_allowed(current_version: int, expected_version: int) -> bool:
    if current_version < 0 or expected_version < 0:
        raise ValueError("versions must be non-negative")
    return current_version == expected_version


def apply_versioned_update(
    current_value: int,
    delta: int,
    current_version: int,
    expected_version: int,
) -> tuple[int, int]:
    if not optimistic_write_allowed(current_version, expected_version):
        raise ValueError("stale write detected")
    return current_value + delta, current_version + 1


def shared_state_risk(concurrent_writers: int, uses_coordination: bool) -> str:
    if concurrent_writers < 0:
        raise ValueError("concurrent_writers must be non-negative")
    if concurrent_writers <= 1:
        return "low"
    if uses_coordination:
        return "medium"
    return "high"
