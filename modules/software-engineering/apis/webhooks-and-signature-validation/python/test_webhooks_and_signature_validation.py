from __future__ import annotations

import pytest

from webhooks_and_signature_validation import (
    webhook_decision,
    webhook_request_valid,
    webhook_signature,
)


def test_valid_webhook_request_needs_matching_signature_and_fresh_timestamp() -> None:
    signature = webhook_signature("secret", timestamp=1_700_000_000, body='{"event":"paid"}')

    assert webhook_request_valid(
        "secret",
        timestamp=1_700_000_000,
        body='{"event":"paid"}',
        provided_signature=signature,
        now_timestamp=1_700_000_120,
    ) is True


def test_invalid_signature_or_stale_timestamp_is_rejected() -> None:
    signature = webhook_signature("secret", timestamp=1_700_000_000, body='{"event":"paid"}')

    assert webhook_request_valid(
        "secret",
        timestamp=1_700_000_000,
        body='{"event":"paid"}',
        provided_signature="bad-signature",
        now_timestamp=1_700_000_120,
    ) is False
    assert webhook_request_valid(
        "secret",
        timestamp=1_700_000_000,
        body='{"event":"paid"}',
        provided_signature=signature,
        now_timestamp=1_700_000_400,
    ) is False


def test_webhook_decision_requires_non_empty_event_type() -> None:
    assert webhook_decision(True, "payment.paid") == "process:payment.paid"
    assert webhook_decision(False, "payment.paid") == "reject"

    with pytest.raises(ValueError):
        webhook_decision(True, " ")
