from __future__ import annotations


def decompose_goal(goal: str, verbs: list[str]) -> list[str]:
    cleaned_goal = goal.strip()
    if not cleaned_goal:
        raise ValueError("goal must be non-empty")
    parts = [f"{verb.strip()} {cleaned_goal}".strip() for verb in verbs if verb.strip()]
    return [part for part in parts if part]


def numbered_checkpoints(items: list[str]) -> list[dict[str, object]]:
    checkpoints: list[dict[str, object]] = []
    for index, item in enumerate(items, start=1):
        cleaned = item.strip()
        if not cleaned:
            continue
        checkpoints.append({"id": index, "text": cleaned, "done": False})
    return checkpoints


def decomposition_is_actionable(items: list[dict[str, object]], min_count: int) -> bool:
    if min_count <= 0:
        raise ValueError("min_count must be positive")
    return len(items) >= min_count and all(str(item.get("text", "")).strip() for item in items)
