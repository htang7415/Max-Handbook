from cdc_vs_application_events import (
    application_event,
    application_event_names,
    cdc_event,
    event_kinds,
    latest_row_from_cdc,
)


def test_cdc_events_can_reconstruct_latest_row_state() -> None:
    events = [
        cdc_event("orders", "insert", "o1", {"status": "placed", "customer_id": "c1"}),
        cdc_event("orders", "update", "o1", {"status": "paid", "customer_id": "c1"}),
    ]

    assert latest_row_from_cdc(events, "orders", "o1") == {
        "status": "paid",
        "customer_id": "c1",
    }


def test_cdc_delete_removes_the_reconstructed_row() -> None:
    events = [
        cdc_event("orders", "insert", "o1", {"status": "placed"}),
        cdc_event("orders", "delete", "o1", None),
    ]

    assert latest_row_from_cdc(events, "orders", "o1") is None


def test_application_events_preserve_business_intent_names() -> None:
    events = [
        cdc_event("orders", "insert", "o1", {"status": "placed"}),
        application_event("order.created", "o1", {"customer_id": "c1"}),
        application_event("order.confirmed", "o1", {"email_sent": True}),
    ]

    assert event_kinds(events) == ["cdc", "application", "application"]
    assert application_event_names(events) == ["order.created", "order.confirmed"]
