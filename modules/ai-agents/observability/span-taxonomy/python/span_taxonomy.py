from __future__ import annotations


def span_kind(span_name: str) -> str:
    lowered = span_name.strip().lower()
    if not lowered:
        return "unknown"
    if "tool" in lowered:
        return "tool"
    if "guardrail" in lowered or "policy" in lowered:
        return "guardrail"
    if lowered in {"plan", "route", "handoff", "workflow", "state"} or "plan" in lowered:
        return "workflow"
    if lowered in {"model", "generate", "decode"} or "model" in lowered:
        return "model"
    return "unknown"


def label_spans(span_names: list[str]) -> dict[str, str]:
    return {
        span_name: span_kind(span_name)
        for span_name in span_names
        if span_name.strip()
    }


def span_kind_counts(span_names: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for kind in label_spans(span_names).values():
        counts[kind] = counts.get(kind, 0) + 1
    return counts
