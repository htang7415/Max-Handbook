"""semantic_cache_hit_rate_analysis - measure whether semantic caching is paying off."""

from __future__ import annotations


def validate_event(event: dict[str, object]) -> None:
    if not isinstance(event.get("hit"), bool):
        raise ValueError("event['hit'] must be a bool")


def hit_rate(events: list[dict[str, object]]) -> float:
    if not events:
        return 0.0
    hits = 0
    for event in events:
        validate_event(event)
        if event["hit"] is True:
            hits += 1
    return hits / len(events)


def scoped_hit_rates(
    events: list[dict[str, object]],
    scope_field: str,
) -> dict[object, float]:
    grouped: dict[object, list[dict[str, object]]] = {}
    for event in events:
        validate_event(event)
        grouped.setdefault(event[scope_field], []).append(event)
    return {
        scope: hit_rate(group_events)
        for scope, group_events in grouped.items()
    }


def latency_saved_ms(
    events: list[dict[str, object]],
    hit_latency_ms: int,
    miss_latency_ms: int,
) -> int:
    if hit_latency_ms < 0:
        raise ValueError("hit_latency_ms must be non-negative")
    if miss_latency_ms < 0:
        raise ValueError("miss_latency_ms must be non-negative")
    baseline = len(events) * miss_latency_ms
    actual = 0
    for event in events:
        validate_event(event)
        actual += hit_latency_ms if event["hit"] is True else miss_latency_ms
    return baseline - actual


def savings_summary(
    events: list[dict[str, object]],
    hit_latency_ms: int,
    miss_latency_ms: int,
) -> dict[str, float | int]:
    return {
        "request_count": len(events),
        "hit_rate": hit_rate(events),
        "latency_saved_ms": latency_saved_ms(events, hit_latency_ms, miss_latency_ms),
    }
