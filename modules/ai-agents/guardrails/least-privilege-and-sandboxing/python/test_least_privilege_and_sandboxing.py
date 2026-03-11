from __future__ import annotations

import pytest

from least_privilege_and_sandboxing import (
    least_privilege_scopes,
    sandbox_profile,
    scope_escalation_required,
)


def test_least_privilege_scopes_returns_minimal_union() -> None:
    tool_scopes = {
        "search_docs": ["docs:read"],
        "read_repo": ["repo:read"],
        "send_email": ["email:send", "contacts:read"],
    }

    assert least_privilege_scopes(["search_docs", "read_repo"], tool_scopes) == [
        "docs:read",
        "repo:read",
    ]


def test_sandbox_profile_and_scope_escalation_cover_common_cases() -> None:
    assert sandbox_profile(needs_write=False, needs_network=False, handles_secrets=False) == "read-only"
    assert sandbox_profile(needs_write=False, needs_network=True, handles_secrets=False) == "read-only-network"
    assert sandbox_profile(needs_write=True, needs_network=False, handles_secrets=False) == "workspace-write"
    assert sandbox_profile(needs_write=True, needs_network=True, handles_secrets=True) == "isolated-review"

    assert scope_escalation_required(["repo:read"], ["repo:read", "email:send"]) is True
    assert scope_escalation_required(["repo:read", "docs:read"], ["docs:read"]) is False


def test_least_privilege_and_sandboxing_validation() -> None:
    with pytest.raises(ValueError):
        least_privilege_scopes([], {"search_docs": ["docs:read"]})
    with pytest.raises(ValueError):
        least_privilege_scopes(["unknown"], {"search_docs": ["docs:read"]})
    with pytest.raises(ValueError):
        scope_escalation_required(["repo:read"], [])
