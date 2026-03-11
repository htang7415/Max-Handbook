"""serializable_retries - retry loops for serialization failures."""

from __future__ import annotations


def run_serializable_retry_loop(
    conflicts: list[bool],
    max_retries: int,
) -> dict[str, int | bool]:
    attempts = 0
    retries_used = 0

    for conflict in conflicts:
        attempts += 1
        if not conflict:
            return {
                "attempts": attempts,
                "retries_used": retries_used,
                "committed": True,
            }
        if retries_used >= max_retries:
            return {
                "attempts": attempts,
                "retries_used": retries_used,
                "committed": False,
            }
        retries_used += 1

    return {
        "attempts": attempts,
        "retries_used": retries_used,
        "committed": attempts == 0,
    }


def should_backoff(conflicts: list[bool]) -> bool:
    return any(conflicts)
