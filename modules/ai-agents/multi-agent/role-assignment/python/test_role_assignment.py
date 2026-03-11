from __future__ import annotations

from role_assignment import assign_roles, role_assignment_summary, role_owners


def test_role_assignment_selects_roles_and_summarizes() -> None:
    roles = assign_roles(
        "investigate outage and write summary",
        {
            "researcher": ["investigate", "analyze"],
            "writer": ["write", "summarize"],
            "executor": ["click", "run"],
        },
    )
    assert roles == ["researcher", "writer"]
    assert role_owners(roles) == {
        "researcher": "researcher-worker",
        "writer": "writer-worker",
    }
    assert role_assignment_summary(roles) == "Roles: researcher, writer"


def test_role_assignment_handles_empty_task() -> None:
    assert assign_roles("", {"writer": ["write"]}) == []
    assert role_assignment_summary([]) == "No roles assigned."
