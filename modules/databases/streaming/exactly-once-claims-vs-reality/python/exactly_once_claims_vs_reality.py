"""exactly_once_claims_vs_reality - duplicate delivery still needs end-to-end handling."""

from __future__ import annotations


def delivered_event(event_id: str, key: str, amount: int) -> dict[str, object]:
    return {
        "event_id": event_id,
        "key": key,
        "amount": amount,
    }


def duplicate_event_ids(events: list[dict[str, object]]) -> list[str]:
    counts: dict[str, int] = {}
    for event in events:
        event_id = str(event["event_id"])
        counts[event_id] = counts.get(event_id, 0) + 1
    return sorted(event_id for event_id, count in counts.items() if count > 1)


def non_idempotent_sink_totals(events: list[dict[str, object]]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for event in events:
        key = str(event["key"])
        totals[key] = totals.get(key, 0) + int(event["amount"])
    return totals


def idempotent_sink_totals(events: list[dict[str, object]]) -> dict[str, int]:
    totals: dict[str, int] = {}
    seen: set[str] = set()
    for event in events:
        event_id = str(event["event_id"])
        if event_id in seen:
            continue
        seen.add(event_id)
        key = str(event["key"])
        totals[key] = totals.get(key, 0) + int(event["amount"])
    return totals


def end_to_end_safe(events: list[dict[str, object]], sink_idempotent: bool) -> bool:
    duplicates = duplicate_event_ids(events)
    return not duplicates or sink_idempotent


def delivery_summary(events: list[dict[str, object]]) -> dict[str, object]:
    duplicates = duplicate_event_ids(events)
    return {
        "duplicate_event_ids": duplicates,
        "non_idempotent_totals": non_idempotent_sink_totals(events),
        "idempotent_totals": idempotent_sink_totals(events),
        "needs_sink_dedup": bool(duplicates),
    }
