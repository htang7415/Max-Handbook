from __future__ import annotations


RETRYABLE_HTTP_STATUSES = {408, 429, 500, 502, 503, 504}
INHERENTLY_RETRYABLE_METHODS = {"GET", "HEAD", "OPTIONS", "PUT", "DELETE"}


def retryable_request(method: str, has_idempotency_key: bool = False) -> bool:
    normalized_method = method.strip().upper()
    if not normalized_method:
        raise ValueError("method must be non-empty")
    return normalized_method in INHERENTLY_RETRYABLE_METHODS or (
        normalized_method == "POST" and has_idempotency_key
    )


def should_retry_http(status_code: int, method: str, has_idempotency_key: bool = False) -> bool:
    if not 100 <= status_code <= 599:
        raise ValueError("status_code must be between 100 and 599")
    return status_code in RETRYABLE_HTTP_STATUSES and retryable_request(
        method,
        has_idempotency_key=has_idempotency_key,
    )


def capped_backoff_ms(base_delay_ms: int, attempt: int, max_delay_ms: int) -> int:
    if base_delay_ms <= 0:
        raise ValueError("base_delay_ms must be positive")
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    if max_delay_ms < base_delay_ms:
        raise ValueError("max_delay_ms must be at least base_delay_ms")
    return min(max_delay_ms, base_delay_ms * (2 ** attempt))


def per_attempt_timeout_ms(total_deadline_ms: int, max_attempts: int) -> int:
    if total_deadline_ms <= 0:
        raise ValueError("total_deadline_ms must be positive")
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive")
    return total_deadline_ms // max_attempts
