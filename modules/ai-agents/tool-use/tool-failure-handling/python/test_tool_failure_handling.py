from __future__ import annotations

import pytest

from tool_failure_handling import failure_kind, fallback_tool, next_action


def test_tool_failure_handling_classifies_and_routes_failures() -> None:
    timeout_result = {"status": "error", "message": "tool timeout after 5s"}
    assert failure_kind(timeout_result) == "timeout"
    assert next_action("timeout", retryable_errors={"timeout", "rate_limit"}) == "retry"
    assert next_action("tool_error", retryable_errors={"timeout"}, fallback_map={"search": "browse_docs"}) == "fallback"
    assert fallback_tool("search", {"search": "browse_docs"}) == "browse_docs"


def test_tool_failure_handling_validation_and_non_error_case() -> None:
    assert failure_kind({"status": "ok"}) == "ok"
    assert next_action("ok", retryable_errors={"timeout"}) == "continue"
    assert next_action("auth", retryable_errors={"timeout"}) == "escalate"
    with pytest.raises(ValueError):
        fallback_tool("", {"search": "browse_docs"})
