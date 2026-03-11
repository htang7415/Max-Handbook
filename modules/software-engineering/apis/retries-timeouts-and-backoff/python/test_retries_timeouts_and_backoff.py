from __future__ import annotations

import pytest

from retries_timeouts_and_backoff import (
    capped_backoff_ms,
    per_attempt_timeout_ms,
    retryable_request,
    should_retry_http,
)


def test_retryable_request_requires_idempotency_for_post() -> None:
    assert retryable_request("GET") is True
    assert retryable_request("POST") is False
    assert retryable_request("POST", has_idempotency_key=True) is True


def test_should_retry_http_only_retries_retryable_statuses_and_safe_requests() -> None:
    assert should_retry_http(503, "GET") is True
    assert should_retry_http(503, "POST") is False
    assert should_retry_http(503, "POST", has_idempotency_key=True) is True
    assert should_retry_http(400, "GET") is False


def test_backoff_and_timeout_budget_are_bounded_and_validated() -> None:
    assert capped_backoff_ms(base_delay_ms=200, attempt=0, max_delay_ms=1000) == 200
    assert capped_backoff_ms(base_delay_ms=200, attempt=3, max_delay_ms=1000) == 1000
    assert per_attempt_timeout_ms(total_deadline_ms=1200, max_attempts=3) == 400

    with pytest.raises(ValueError):
        capped_backoff_ms(base_delay_ms=0, attempt=1, max_delay_ms=1000)
    with pytest.raises(ValueError):
        should_retry_http(700, "GET")
