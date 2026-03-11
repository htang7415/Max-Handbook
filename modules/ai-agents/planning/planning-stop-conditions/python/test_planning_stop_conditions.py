from __future__ import annotations

from planning_stop_conditions import all_steps_done, stop_decision, stop_due_to_blockers


def test_planning_stop_conditions_choose_done_blocked_or_continue() -> None:
    done_plan = [{"text": "collect", "done": True}, {"text": "write", "done": True}]
    active_plan = [{"text": "collect", "done": True}, {"text": "write", "done": False}]
    assert all_steps_done(done_plan) is True
    assert all_steps_done(active_plan) is False
    assert stop_due_to_blockers(["waiting on approval"]) is True
    assert stop_decision(done_plan, [], needs_review=False) == "done"
    assert stop_decision(active_plan, ["waiting on approval"], needs_review=False) == "blocked"
    assert stop_decision(active_plan, [], needs_review=True) == "review"
    assert stop_decision(active_plan, [], needs_review=False) == "continue"


def test_planning_stop_conditions_empty_plan_is_not_done() -> None:
    assert all_steps_done([]) is False
    assert stop_due_to_blockers(["", "   "]) is False
