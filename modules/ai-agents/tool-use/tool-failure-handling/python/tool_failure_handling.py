from __future__ import annotations


def failure_kind(result: dict[str, object]) -> str:
    status = str(result.get("status", "")).strip().lower()
    message = str(result.get("message", "")).strip().lower()
    if status != "error" and not bool(result.get("is_error", False)):
        return "ok"
    if "timeout" in message:
        return "timeout"
    if "rate" in message and "limit" in message:
        return "rate_limit"
    if "auth" in message or "permission" in message:
        return "auth"
    return "tool_error"


def next_action(
    failure: str,
    retryable_errors: set[str],
    fallback_map: dict[str, str] | None = None,
) -> str:
    if failure == "ok":
        return "continue"
    if failure in retryable_errors:
        return "retry"
    if fallback_map:
        return "fallback"
    return "escalate"


def fallback_tool(tool_name: str, fallback_map: dict[str, str]) -> str | None:
    cleaned = tool_name.strip()
    if not cleaned:
        raise ValueError("tool_name must be non-empty")
    return fallback_map.get(cleaned)
