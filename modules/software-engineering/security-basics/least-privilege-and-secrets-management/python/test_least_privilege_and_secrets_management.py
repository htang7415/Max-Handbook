from __future__ import annotations

import pytest

from least_privilege_and_secrets_management import (
    least_privilege_scopes,
    privilege_escalation_required,
    secret_handling_action,
)


def test_least_privilege_collects_only_required_scopes() -> None:
    capability_scopes = {
        "read-docs": ["docs:read"],
        "write-docs": ["docs:read", "docs:write"],
        "manage-secrets": ["secrets:read"],
    }

    assert least_privilege_scopes(["read-docs", "write-docs"], capability_scopes) == [
        "docs:read",
        "docs:write",
    ]


def test_secret_handling_distinguishes_deny_redact_and_managed_paths() -> None:
    assert secret_handling_action("OPENAI_API_KEY", "log") == "deny"
    assert secret_handling_action("OPENAI_API_KEY", "config-file") == "redact"
    assert secret_handling_action("OPENAI_API_KEY", "secret-manager") == "store-managed"
    assert secret_handling_action("OPENAI_API_KEY", "process-env") == "inject-ephemeral"


def test_privilege_escalation_requires_review_for_new_scope_or_secret_access() -> None:
    assert privilege_escalation_required(["docs:read"], ["docs:read"]) is False
    assert privilege_escalation_required(["docs:read"], ["docs:read", "docs:write"]) is True
    assert privilege_escalation_required(["docs:read"], ["docs:read"], secret_access=True) is True

    with pytest.raises(ValueError):
        least_privilege_scopes([], {})
