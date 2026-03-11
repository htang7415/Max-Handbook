from __future__ import annotations

import pytest

from retries_and_recovery import (
    exponential_backoff_ms,
    fallback_action,
    should_retry,
)


def test_retries_and_recovery_basic_flow() -> None:
    assert should_retry("timeout", attempt=1, max_attempts=3) is True
    assert should_retry("invalid_input", attempt=1, max_attempts=3) is False
    assert exponential_backoff_ms(base_delay_ms=200, attempt=2) == 800
    assert fallback_action("search") == "ask_user_for_clarification"


def test_retries_and_recovery_validation() -> None:
    with pytest.raises(ValueError):
        should_retry("timeout", attempt=-1, max_attempts=3)
    with pytest.raises(ValueError):
        should_retry("timeout", attempt=0, max_attempts=0)
    with pytest.raises(ValueError):
        exponential_backoff_ms(base_delay_ms=0, attempt=1)
    with pytest.raises(ValueError):
        exponential_backoff_ms(base_delay_ms=100, attempt=-1)
    with pytest.raises(ValueError):
        fallback_action("")
