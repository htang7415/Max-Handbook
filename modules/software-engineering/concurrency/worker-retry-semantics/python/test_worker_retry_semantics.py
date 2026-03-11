from __future__ import annotations

import pytest

from worker_retry_semantics import next_retry_delay_ms, worker_ack_state, worker_retry_action


def test_worker_retry_action_retries_transient_errors_then_dead_letters() -> None:
    assert worker_retry_action("timeout", attempt=1, max_attempts=3) == "retry"
    assert worker_retry_action("timeout", attempt=3, max_attempts=3) == "dead-letter"
    assert worker_retry_action("validation_error", attempt=1, max_attempts=3) == "fail-fast"


def test_next_retry_delay_ms_is_exponential_and_capped() -> None:
    assert next_retry_delay_ms(base_delay_ms=200, attempt=0, max_delay_ms=1000) == 200
    assert next_retry_delay_ms(base_delay_ms=200, attempt=3, max_delay_ms=1000) == 1000


def test_worker_ack_state_matches_retry_action() -> None:
    assert worker_ack_state("retry") == "nack-retry"
    assert worker_ack_state("dead-letter") == "ack-dead-letter"
    assert worker_ack_state("fail-fast") == "ack-failure"

    with pytest.raises(ValueError):
        worker_ack_state("unknown")
