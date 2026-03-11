from __future__ import annotations


def categorize_failure(message: str) -> str:
    lowered = message.strip().lower()
    if not lowered:
        return "unknown"
    if "tool" in lowered or "timeout" in lowered or "rate limit" in lowered:
        return "tool"
    if "policy" in lowered or "guardrail" in lowered or "blocked" in lowered:
        return "policy"
    if "plan" in lowered or "workflow" in lowered or "handoff" in lowered:
        return "workflow"
    if "model" in lowered or "halluc" in lowered:
        return "model"
    return "unknown"


def failure_category_counts(messages: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for message in messages:
        category = categorize_failure(message)
        counts[category] = counts.get(category, 0) + 1
    return counts


def top_failure_category(messages: list[str]) -> str | None:
    counts = failure_category_counts(messages)
    if not counts:
        return None
    return max(counts.items(), key=lambda item: (item[1], item[0]))[0]
