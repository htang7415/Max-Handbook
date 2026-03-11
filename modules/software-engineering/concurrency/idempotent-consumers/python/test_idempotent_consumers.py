from __future__ import annotations

import pytest

from idempotent_consumers import dedupe_key, mark_processed, should_process_message


def test_dedupe_key_binds_consumer_and_message_identity() -> None:
    assert dedupe_key("msg_1", "invoice-writer") == "invoice-writer:msg_1"


def test_should_process_message_blocks_duplicate_delivery_for_same_consumer() -> None:
    seen = mark_processed("msg_1", seen_keys=set(), consumer_name="invoice-writer")

    assert should_process_message("msg_1", seen, consumer_name="invoice-writer") is False
    assert should_process_message("msg_1", seen, consumer_name="email-sender") is True


def test_validation_rejects_blank_message_or_consumer_name() -> None:
    with pytest.raises(ValueError):
        dedupe_key(" ", "invoice-writer")
    with pytest.raises(ValueError):
        dedupe_key("msg_1", " ")
