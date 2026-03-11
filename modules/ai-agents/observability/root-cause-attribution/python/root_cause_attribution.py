from __future__ import annotations


def attributed_failure_counts(spans: list[dict[str, object]]) -> dict[str, int]:
    if not spans:
        raise ValueError("spans must be non-empty")

    counts = {"model": 0, "tool": 0, "workflow": 0, "unknown": 0}
    for span in spans:
        status = str(span.get("status", "")).strip().lower()
        if status in {"", "ok"}:
            continue
        kind = str(span.get("kind", "")).strip().lower()
        if kind in counts:
            counts[kind] += 1
        else:
            counts["unknown"] += 1

    return {name: count for name, count in counts.items() if count > 0}


def dominant_failure_source(counts: dict[str, int]) -> str | None:
    if not counts:
        return None
    cleaned = {name.strip(): int(value) for name, value in counts.items() if name.strip() and int(value) > 0}
    if not cleaned:
        return None
    return sorted(cleaned.items(), key=lambda item: (-item[1], item[0]))[0][0]


def attribution_route(counts: dict[str, int], min_share: float) -> str:
    if not 0.0 <= min_share <= 1.0:
        raise ValueError("min_share must satisfy 0 <= value <= 1")
    dominant = dominant_failure_source(counts)
    if dominant is None:
        return "no-failures"

    cleaned = {name.strip(): int(value) for name, value in counts.items() if name.strip() and int(value) > 0}
    total = sum(cleaned.values())
    if total <= 0:
        return "no-failures"
    dominant_share = cleaned[dominant] / total
    if dominant_share >= min_share:
        return "targeted-fix"
    return "broad-review"
