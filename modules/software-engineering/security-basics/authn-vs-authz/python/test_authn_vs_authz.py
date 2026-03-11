from __future__ import annotations

import pytest

from authn_vs_authz import access_decision, authenticate_credential, authorize_action


def test_authentication_and_authorization_are_separate_checks() -> None:
    token_directory = {"token_admin": "alice", "token_viewer": "bob"}
    scope_directory = {
        "alice": ["docs:read", "docs:write"],
        "bob": ["docs:read"],
    }

    assert authenticate_credential("token_admin", token_directory) == "alice"
    assert authorize_action(scope_directory["bob"], "docs:write") is False
    assert access_decision("token_admin", token_directory, scope_directory, "docs:write") == "allow"
    assert access_decision("token_viewer", token_directory, scope_directory, "docs:write") == "deny:unauthorized"


def test_access_decision_denies_unknown_credentials() -> None:
    assert access_decision("token_missing", {"token_admin": "alice"}, {"alice": ["docs:read"]}, "docs:read") == (
        "deny:unauthenticated"
    )


def test_validation_rejects_blank_credential_and_scope() -> None:
    with pytest.raises(ValueError):
        authenticate_credential(" ", {"token_admin": "alice"})
    with pytest.raises(ValueError):
        authorize_action(["docs:read"], " ")
