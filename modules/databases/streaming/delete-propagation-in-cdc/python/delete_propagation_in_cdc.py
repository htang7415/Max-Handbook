"""delete_propagation_in_cdc - downstream state goes stale if delete events are ignored."""

from __future__ import annotations


def cdc_event(
    sequence: int,
    table: str,
    row_id: str,
    op: str,
    after: dict[str, object] | None,
) -> dict[str, object]:
    return {
        "sequence": sequence,
        "table": table,
        "row_id": row_id,
        "op": op,
        "after": after,
    }


def apply_cdc_ignoring_deletes(events: list[dict[str, object]]) -> dict[tuple[str, str], dict[str, object]]:
    rows: dict[tuple[str, str], dict[str, object]] = {}
    for event in sorted(events, key=lambda item: int(item["sequence"])):
        key = (str(event["table"]), str(event["row_id"]))
        if str(event["op"]) == "delete":
            continue
        rows[key] = dict(event.get("after") or {})
    return rows


def apply_cdc_with_deletes(events: list[dict[str, object]]) -> dict[tuple[str, str], dict[str, object]]:
    rows: dict[tuple[str, str], dict[str, object]] = {}
    for event in sorted(events, key=lambda item: int(item["sequence"])):
        key = (str(event["table"]), str(event["row_id"]))
        if str(event["op"]) == "delete":
            rows.pop(key, None)
            continue
        rows[key] = dict(event.get("after") or {})
    return rows


def propagation_summary(events: list[dict[str, object]]) -> dict[str, object]:
    return {
        "ignoring_deletes": apply_cdc_ignoring_deletes(events),
        "propagating_deletes": apply_cdc_with_deletes(events),
    }
