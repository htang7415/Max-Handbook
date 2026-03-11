"""materialized_view_patterns - incremental status aggregates from events."""

from __future__ import annotations


def empty_view() -> dict[str, object]:
    return {
        "latest_by_order": {},
        "counts_by_workspace": {},
    }


def apply_order_status_event(
    view: dict[str, object],
    event: dict[str, object],
) -> None:
    latest_by_order = view["latest_by_order"]
    counts_by_workspace = view["counts_by_workspace"]
    assert isinstance(latest_by_order, dict)
    assert isinstance(counts_by_workspace, dict)

    order_id = str(event["order_id"])
    workspace_id = int(event["workspace_id"])
    new_status = str(event["status"])
    previous = latest_by_order.get(order_id)

    workspace_counts = counts_by_workspace.setdefault(workspace_id, {})
    assert isinstance(workspace_counts, dict)

    if previous is not None:
        old_workspace_id = int(previous["workspace_id"])
        old_status = str(previous["status"])
        old_counts = counts_by_workspace.setdefault(old_workspace_id, {})
        assert isinstance(old_counts, dict)
        old_counts[old_status] = max(int(old_counts.get(old_status, 0)) - 1, 0)

    workspace_counts[new_status] = int(workspace_counts.get(new_status, 0)) + 1
    latest_by_order[order_id] = {
        "workspace_id": workspace_id,
        "status": new_status,
    }


def rebuild_view(events: list[dict[str, object]]) -> dict[str, object]:
    view = empty_view()
    for event in events:
        apply_order_status_event(view, event)
    return view


def workspace_status_counts(
    view: dict[str, object],
    workspace_id: int,
) -> dict[str, int]:
    counts_by_workspace = view["counts_by_workspace"]
    assert isinstance(counts_by_workspace, dict)
    raw = counts_by_workspace.get(workspace_id, {})
    assert isinstance(raw, dict)
    return {status: count for status, count in raw.items() if int(count) > 0}
