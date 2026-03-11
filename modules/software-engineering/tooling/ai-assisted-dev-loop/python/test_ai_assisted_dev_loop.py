from __future__ import annotations

import pytest

from ai_assisted_dev_loop import make_change_request, next_stage, review_risk


def test_make_change_request_normalizes_inputs() -> None:
    request = make_change_request(
        " Add retry guard ",
        [" keep API stable ", "", "preserve metrics"],
        [" contract tests ", " targeted retry tests "],
    )

    assert request == {
        "task": "Add retry guard",
        "constraints": ["keep API stable", "preserve metrics"],
        "acceptance_checks": ["contract tests", "targeted retry tests"],
    }


def test_make_change_request_requires_task_and_checks() -> None:
    with pytest.raises(ValueError):
        make_change_request("", [], ["check"])
    with pytest.raises(ValueError):
        make_change_request("task", [], ["", " "])


def test_next_stage_follows_generate_check_review_ship_order() -> None:
    assert next_stage(False, False, False) == "draft_patch"
    assert next_stage(True, False, False) == "run_checks"
    assert next_stage(True, True, False) == "human_review"
    assert next_stage(True, True, True) == "ship"


def test_review_risk_flags_sensitive_or_generated_changes() -> None:
    assert review_risk(["services/auth/policy.py"]) == "high"
    assert review_risk(["app/a.py", "app/b.py", "app/c.py", "app/d.py", "app/e.py", "app/f.py"]) == "medium"
    assert review_risk(["docs/guide.md"], touches_generated_code=True) == "high"
    assert review_risk(["docs/guide.md"]) == "low"
