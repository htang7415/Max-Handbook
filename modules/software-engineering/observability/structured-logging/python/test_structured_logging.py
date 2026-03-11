from __future__ import annotations

import pytest

from structured_logging import make_log_event, missing_required_log_fields, redact_context


def test_redact_context_hides_sensitive_keys() -> None:
    assert redact_context({"token": "secret", "request_id": "req_1"}) == {
        "token": "[REDACTED]",
        "request_id": "req_1",
    }


def test_make_log_event_builds_structured_event_with_redacted_context() -> None:
    event = make_log_event("payments", "INFO", "payment created", {"request_id": "req_1", "token": "secret"})

    assert event == {
        "service": "payments",
        "level": "info",
        "message": "payment created",
        "context": {"request_id": "req_1", "token": "[REDACTED]"},
    }


def test_missing_required_log_fields_checks_top_level_and_context_fields() -> None:
    event = make_log_event("payments", "info", "payment created", {"request_id": "req_1"})

    assert missing_required_log_fields(event, ["service", "level", "message", "request_id"]) == []
    assert missing_required_log_fields(event, ["trace_id"]) == ["trace_id"]

    with pytest.raises(ValueError):
        make_log_event("", "info", "payment created", {})
