from __future__ import annotations

import pytest

from queues_vs_locks import coordination_pattern, lock_contention_risk, queue_backlog_warning


def test_coordination_pattern_prefers_queue_when_work_can_be_delayed() -> None:
    assert coordination_pattern(shared_resource=True, can_delay_work=True, needs_single_owner=False) == "queue"
    assert coordination_pattern(shared_resource=True, can_delay_work=False, needs_single_owner=False) == "lock"
    assert coordination_pattern(shared_resource=False, can_delay_work=False, needs_single_owner=False) == "none"


def test_lock_contention_risk_rises_with_workers_and_critical_section_duration() -> None:
    assert lock_contention_risk(concurrent_workers=1, critical_section_ms=80) == "low"
    assert lock_contention_risk(concurrent_workers=3, critical_section_ms=30) == "medium"
    assert lock_contention_risk(concurrent_workers=6, critical_section_ms=80) == "high"


def test_queue_backlog_warning_flags_large_backlogs() -> None:
    assert queue_backlog_warning(queue_depth=50, workers=10) is False
    assert queue_backlog_warning(queue_depth=200, workers=10) is True

    with pytest.raises(ValueError):
        queue_backlog_warning(queue_depth=-1, workers=10)
