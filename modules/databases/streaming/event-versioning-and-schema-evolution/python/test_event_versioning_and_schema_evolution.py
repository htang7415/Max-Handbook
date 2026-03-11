import pytest

from event_versioning_and_schema_evolution import (
    normalize_order_event,
    normalized_stream,
    order_event_v1,
    order_event_v2,
)


def test_consumer_can_normalize_mixed_event_versions() -> None:
    events = [
        order_event_v1("o-1", "queued"),
        order_event_v2("o-2", "running", workspace_id=7),
    ]

    assert normalized_stream(events) == [
        {"order_id": "o-1", "status": "queued", "workspace_id": None},
        {"order_id": "o-2", "status": "running", "workspace_id": 7},
    ]


def test_unknown_version_is_rejected() -> None:
    with pytest.raises(ValueError, match="unsupported event version"):
        normalize_order_event({"version": 99, "order_id": "o-1", "status": "queued"})
