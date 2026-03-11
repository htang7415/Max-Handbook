from __future__ import annotations


SEPARATOR = " | "


def compact_memories(items: list[str], max_items: int) -> str:
    if max_items <= 0:
        raise ValueError("max_items must be positive")
    cleaned = [item.strip() for item in items if item.strip()]
    return SEPARATOR.join(cleaned[-max_items:])


def append_compacted_summary(summary: str, new_item: str) -> str:
    base_items = [item.strip() for item in summary.split(SEPARATOR) if item.strip()]
    new_cleaned = new_item.strip()
    if new_cleaned:
        base_items.append(new_cleaned)
    return SEPARATOR.join(base_items)


def compacted_item_count(summary: str) -> int:
    return len([item for item in summary.split(SEPARATOR) if item.strip()])
