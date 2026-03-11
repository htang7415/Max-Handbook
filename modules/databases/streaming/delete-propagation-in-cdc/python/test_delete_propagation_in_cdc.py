from delete_propagation_in_cdc import cdc_event, propagation_summary


def test_ignoring_deletes_leaves_stale_rows_in_the_sink() -> None:
    events = [
        cdc_event(1, "documents", "doc-1", "upsert", {"title": "Guide"}),
        cdc_event(2, "documents", "doc-1", "delete", None),
    ]

    assert propagation_summary(events) == {
        "ignoring_deletes": {("documents", "doc-1"): {"title": "Guide"}},
        "propagating_deletes": {},
    }


def test_later_reinsert_after_delete_rebuilds_the_row() -> None:
    events = [
        cdc_event(1, "documents", "doc-1", "upsert", {"title": "Guide"}),
        cdc_event(2, "documents", "doc-1", "delete", None),
        cdc_event(3, "documents", "doc-1", "upsert", {"title": "Guide v2"}),
    ]

    assert propagation_summary(events)["propagating_deletes"] == {
        ("documents", "doc-1"): {"title": "Guide v2"}
    }
