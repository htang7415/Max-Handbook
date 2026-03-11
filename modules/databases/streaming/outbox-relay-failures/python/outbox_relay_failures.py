"""outbox_relay_failures - a relay crash after publish can duplicate delivery on retry."""

from __future__ import annotations


def pending_ids(outbox_ids: list[int], marked_ids: set[int]) -> list[int]:
    return [event_id for event_id in outbox_ids if event_id not in marked_ids]


def duplicate_published_ids(published_ids: list[int]) -> list[int]:
    counts: dict[int, int] = {}
    for event_id in published_ids:
        counts[event_id] = counts.get(event_id, 0) + 1
    return sorted(event_id for event_id, count in counts.items() if count > 1)


def relay_once(
    outbox_ids: list[int],
    published_ids: list[int],
    marked_ids: set[int],
    fail_after_publish_event_id: int | None = None,
) -> None:
    for event_id in pending_ids(outbox_ids, marked_ids):
        published_ids.append(event_id)
        if fail_after_publish_event_id == event_id:
            return
        marked_ids.add(event_id)


def relay_summary(
    outbox_ids: list[int],
    first_failure_event_id: int | None = None,
) -> dict[str, object]:
    published_ids: list[int] = []
    marked_ids: set[int] = set()
    relay_once(outbox_ids, published_ids, marked_ids, fail_after_publish_event_id=first_failure_event_id)
    relay_once(outbox_ids, published_ids, marked_ids)
    return {
        "published_ids": published_ids,
        "duplicate_published_ids": duplicate_published_ids(published_ids),
        "marked_ids": sorted(marked_ids),
        "pending_ids": pending_ids(outbox_ids, marked_ids),
    }
