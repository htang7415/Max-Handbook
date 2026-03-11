from __future__ import annotations

from secure_sdlc_basics import (
    missing_security_checks,
    release_allowed,
    required_security_checks,
)


def test_required_security_checks_expand_with_change_scope() -> None:
    assert required_security_checks(["api", "auth", "dependency-change"]) == [
        "secret-scan",
        "authz-review",
        "dependency-scan",
    ]


def test_missing_security_checks_reports_unfinished_required_controls() -> None:
    assert missing_security_checks(["api", "auth"], ["secret-scan"]) == ["authz-review"]


def test_release_allowed_requires_all_required_security_checks() -> None:
    assert release_allowed(["api", "auth"], ["secret-scan", "authz-review"]) is True
    assert release_allowed(["api", "auth"], ["secret-scan"]) is False
