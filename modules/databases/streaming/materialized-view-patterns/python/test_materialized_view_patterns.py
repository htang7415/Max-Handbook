from materialized_view_patterns import (
    apply_order_status_event,
    empty_view,
    rebuild_view,
    workspace_status_counts,
)


EVENTS = [
    {"order_id": "o1", "workspace_id": 7, "status": "queued"},
    {"order_id": "o2", "workspace_id": 7, "status": "queued"},
    {"order_id": "o1", "workspace_id": 7, "status": "completed"},
    {"order_id": "o3", "workspace_id": 8, "status": "failed"},
]


def test_incremental_updates_move_counts_between_statuses() -> None:
    view = empty_view()
    for event in EVENTS[:3]:
        apply_order_status_event(view, event)

    assert workspace_status_counts(view, 7) == {
        "queued": 1,
        "completed": 1,
    }


def test_full_rebuild_matches_incremental_application() -> None:
    incremental = empty_view()
    for event in EVENTS:
        apply_order_status_event(incremental, event)

    rebuilt = rebuild_view(EVENTS)

    assert workspace_status_counts(incremental, 7) == workspace_status_counts(rebuilt, 7)
    assert workspace_status_counts(incremental, 8) == workspace_status_counts(rebuilt, 8)


def test_separate_workspaces_keep_separate_aggregates() -> None:
    view = rebuild_view(EVENTS)

    assert workspace_status_counts(view, 8) == {"failed": 1}
