from __future__ import annotations

import pytest

from orchestrator_workers import (
    orchestrator_assignments,
    orchestrator_summary,
    worker_task_packet,
)


def test_orchestrator_workers_build_assignments_and_packets() -> None:
    assignments = orchestrator_assignments(
        "audit repo and draft summary",
        {
            "researcher": "scan repo for risky files",
            "writer": "draft summary",
        },
    )

    assert assignments == [
        {
            "goal": "audit repo and draft summary",
            "worker": "researcher",
            "subtask": "scan repo for risky files",
        },
        {
            "goal": "audit repo and draft summary",
            "worker": "writer",
            "subtask": "draft summary",
        },
    ]
    assert worker_task_packet(
        "researcher",
        "scan repo for risky files",
        {"repo": "max-handbook"},
        max_steps=2,
    ) == {
        "worker": "researcher",
        "subtask": "scan repo for risky files",
        "shared_context": {"repo": "max-handbook"},
        "max_steps": 2,
    }


def test_orchestrator_summary_reports_done_blocked_and_completion() -> None:
    summary = orchestrator_summary(
        [
            {"worker": "researcher", "status": "done", "result": "2 risky files"},
            {"worker": "writer", "status": "blocked", "result": None},
        ]
    )

    assert summary == {
        "done_workers": ["researcher"],
        "blocked_workers": ["writer"],
        "results": {
            "researcher": "2 risky files",
            "writer": None,
        },
        "complete": False,
    }


def test_orchestrator_workers_validation() -> None:
    with pytest.raises(ValueError):
        orchestrator_assignments("", {"researcher": "scan repo"})
    with pytest.raises(ValueError):
        orchestrator_assignments("goal", {})
    with pytest.raises(ValueError):
        worker_task_packet("", "scan repo", {}, max_steps=1)
    with pytest.raises(ValueError):
        worker_task_packet("researcher", "scan repo", {}, max_steps=0)
