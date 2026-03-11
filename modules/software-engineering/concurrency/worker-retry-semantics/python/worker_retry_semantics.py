from __future__ import annotations


TRANSIENT_ERRORS = {"timeout", "rate_limit", "temporary_unavailable"}


def worker_retry_action(error_type: str, attempt: int, max_attempts: int) -> str:
    if attempt < 0 or max_attempts <= 0:
        raise ValueError("attempt must be non-negative and max_attempts positive")

    normalized_error = error_type.strip().lower()
    if normalized_error in TRANSIENT_ERRORS and attempt < max_attempts:
        return "retry"
    if normalized_error in TRANSIENT_ERRORS:
        return "dead-letter"
    return "fail-fast"


def next_retry_delay_ms(base_delay_ms: int, attempt: int, max_delay_ms: int) -> int:
    if base_delay_ms <= 0 or attempt < 0 or max_delay_ms < base_delay_ms:
        raise ValueError("invalid retry delay inputs")
    return min(max_delay_ms, base_delay_ms * (2 ** attempt))


def worker_ack_state(action: str) -> str:
    normalized_action = action.strip().lower()
    if normalized_action == "retry":
        return "nack-retry"
    if normalized_action == "dead-letter":
        return "ack-dead-letter"
    if normalized_action == "fail-fast":
        return "ack-failure"
    raise ValueError("action must be retry, dead-letter, or fail-fast")
