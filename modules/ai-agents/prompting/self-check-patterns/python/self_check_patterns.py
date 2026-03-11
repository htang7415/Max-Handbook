from __future__ import annotations


def self_check_checklist(items: list[str]) -> list[str]:
    return [item.strip() for item in items if item.strip()]


def self_check_notes(results: dict[str, bool]) -> list[str]:
    notes: list[str] = []
    for item, passed in results.items():
        if not item.strip():
            continue
        status = "ok" if passed else "fix"
        notes.append(f"{item}: {status}")
    return notes


def self_check_pass(results: dict[str, bool]) -> bool:
    cleaned = {item: passed for item, passed in results.items() if item.strip()}
    if not cleaned:
        raise ValueError("results must contain at least one non-empty item")
    return all(cleaned.values())
