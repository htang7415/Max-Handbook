from exactly_once_claims_vs_reality import (
    delivered_event,
    delivery_summary,
    end_to_end_safe,
)


def test_duplicate_delivery_overstates_a_non_idempotent_sink() -> None:
    events = [
        delivered_event("e1", "acct-1", 10),
        delivered_event("e1", "acct-1", 10),
        delivered_event("e2", "acct-1", 5),
    ]

    assert delivery_summary(events) == {
        "duplicate_event_ids": ["e1"],
        "non_idempotent_totals": {"acct-1": 25},
        "idempotent_totals": {"acct-1": 15},
        "needs_sink_dedup": True,
    }


def test_end_to_end_safety_requires_no_duplicates_or_a_deduplicating_sink() -> None:
    events = [
        delivered_event("e1", "acct-1", 10),
        delivered_event("e1", "acct-1", 10),
    ]

    assert end_to_end_safe(events, sink_idempotent=False) is False
    assert end_to_end_safe(events, sink_idempotent=True) is True
