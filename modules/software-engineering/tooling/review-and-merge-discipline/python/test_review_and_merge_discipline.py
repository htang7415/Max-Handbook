from __future__ import annotations

import pytest

from review_and_merge_discipline import merge_decision, ready_for_merge, review_requirement


def test_review_requirement_rises_for_sensitive_or_large_changes() -> None:
    assert review_requirement(["services/auth/policy.py"], lines_changed=40) == "security-review"
    assert review_requirement(["app/a.py", "app/b.py"], lines_changed=320) == "senior-review"
    assert review_requirement(["app/a.py"], lines_changed=20) == "standard-review"


def test_ready_for_merge_requires_checks_approvals_and_no_open_threads() -> None:
    assert ready_for_merge(open_threads=0, checks_passed=True, approvals=1) is True
    assert ready_for_merge(open_threads=1, checks_passed=True, approvals=1) is False
    assert ready_for_merge(open_threads=0, checks_passed=False, approvals=1) is False


def test_merge_decision_blocks_sensitive_changes_without_extra_approval() -> None:
    assert merge_decision(
        changed_paths=["services/auth/policy.py"],
        lines_changed=40,
        checks_passed=True,
        open_threads=0,
        approvals=1,
    ) == "block"
    assert merge_decision(
        changed_paths=["services/auth/policy.py"],
        lines_changed=40,
        checks_passed=True,
        open_threads=0,
        approvals=2,
    ) == "merge"

    with pytest.raises(ValueError):
        review_requirement(["app/a.py"], lines_changed=-1)
