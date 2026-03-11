from __future__ import annotations

from replanning import remaining_steps, replan_needed, replan_summary


def test_replanning_detects_need_and_summarizes_remaining_work() -> None:
    plan = [
        {"text": "collect metrics", "done": True},
        {"text": "write summary", "done": False},
        {"text": "send report", "done": False},
    ]
    assert replan_needed(
        goal_changed=False,
        blocked_step=True,
        new_constraints=["Need manager approval"],
    ) is True
    assert remaining_steps(plan) == ["write summary", "send report"]
    assert replan_summary(
        ["write summary", "send report"],
        ["Need manager approval"],
    ) == "Remaining: write summary, send report | Constraints: Need manager approval"


def test_replanning_handles_stable_plan_without_constraints() -> None:
    assert replan_needed(False, False, ["", "   "]) is False
    assert remaining_steps([{"text": "", "done": False}, {"text": "done step", "done": True}]) == []
    assert replan_summary([], []) == "Remaining: none"
