from __future__ import annotations

import pytest

from idempotency_keys import idempotency_decision, request_fingerprint, store_response


def test_same_key_and_same_payload_replays_stored_response() -> None:
    fingerprint = request_fingerprint("POST", "/v1/payments", {"amount_cents": 2500, "currency": "USD"})
    record = store_response("pay_123", fingerprint, 201, {"payment_id": "p_1"})

    assert idempotency_decision("pay_123", fingerprint, record) == "replay"


def test_same_key_and_different_payload_conflicts() -> None:
    first = request_fingerprint("POST", "/v1/payments", {"amount_cents": 2500, "currency": "USD"})
    second = request_fingerprint("POST", "/v1/payments", {"amount_cents": 5000, "currency": "USD"})
    record = store_response("pay_123", first, 201, {"payment_id": "p_1"})

    assert idempotency_decision("pay_123", second, record) == "conflict"


def test_validation_rejects_blank_keys_and_invalid_paths() -> None:
    fingerprint = request_fingerprint("POST", "/v1/payments", {"amount_cents": 2500})

    with pytest.raises(ValueError):
        idempotency_decision("", fingerprint, None)
    with pytest.raises(ValueError):
        request_fingerprint("POST", "v1/payments", {"amount_cents": 2500})
    with pytest.raises(ValueError):
        store_response("pay_123", fingerprint, 199, {"payment_id": "p_1"})
