from __future__ import annotations


def coordination_pattern(shared_resource: bool, can_delay_work: bool, needs_single_owner: bool) -> str:
    if can_delay_work:
        return "queue"
    if shared_resource or needs_single_owner:
        return "lock"
    return "none"


def lock_contention_risk(concurrent_workers: int, critical_section_ms: int) -> str:
    if concurrent_workers < 0 or critical_section_ms < 0:
        raise ValueError("inputs must be non-negative")
    if concurrent_workers <= 1 or critical_section_ms <= 10:
        return "low"
    if concurrent_workers <= 4 and critical_section_ms <= 50:
        return "medium"
    return "high"


def queue_backlog_warning(queue_depth: int, workers: int) -> bool:
    if queue_depth < 0 or workers <= 0:
        raise ValueError("queue_depth must be non-negative and workers must be positive")
    return queue_depth > workers * 10
