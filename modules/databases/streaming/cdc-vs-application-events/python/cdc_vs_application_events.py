"""cdc_vs_application_events - compare row-change capture with business-intent events."""

from __future__ import annotations


def cdc_event(table: str, op: str, row_id: str, after: dict[str, object] | None) -> dict[str, object]:
    return {
        "kind": "cdc",
        "table": table,
        "op": op,
        "row_id": row_id,
        "after": after,
    }


def application_event(name: str, aggregate_id: str, payload: dict[str, object]) -> dict[str, object]:
    return {
        "kind": "application",
        "name": name,
        "aggregate_id": aggregate_id,
        "payload": payload,
    }


def latest_row_from_cdc(
    events: list[dict[str, object]],
    table: str,
    row_id: str,
) -> dict[str, object] | None:
    state: dict[str, object] | None = None
    for event in events:
        if event.get("kind") != "cdc":
            continue
        if event.get("table") != table or event.get("row_id") != row_id:
            continue
        op = event.get("op")
        if op == "delete":
            state = None
        else:
            state = dict(event.get("after") or {})
    return state


def application_event_names(events: list[dict[str, object]]) -> list[str]:
    return [
        str(event["name"])
        for event in events
        if event.get("kind") == "application"
    ]


def event_kinds(events: list[dict[str, object]]) -> list[str]:
    return [str(event["kind"]) for event in events]
