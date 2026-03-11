from __future__ import annotations


RETRYABLE_ERRORS = {
    "timeout",
    "rate_limit",
    "temporary_tool_error",
}


def should_retry(error_type: str, attempt: int, max_attempts: int) -> bool:
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive")
    return error_type.strip().lower() in RETRYABLE_ERRORS and attempt < max_attempts


def exponential_backoff_ms(base_delay_ms: int, attempt: int) -> int:
    if base_delay_ms <= 0:
        raise ValueError("base_delay_ms must be positive")
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    return base_delay_ms * (2 ** attempt)


def fallback_action(
    primary_action: str,
    fallback_map: dict[str, str] | None = None,
) -> str | None:
    if fallback_map is None:
        fallback_map = {
            "browser_search": "search_docs",
            "search": "ask_user_for_clarification",
            "web_lookup": "search_docs",
        }
    cleaned = primary_action.strip()
    if not cleaned:
        raise ValueError("primary_action must be non-empty")
    return fallback_map.get(cleaned)
