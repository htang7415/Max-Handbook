"""key_value_patterns - predictable key lookups are cheap, secondary queries are not."""

from __future__ import annotations


def put_value(store: dict[str, object], key: str, value: object) -> None:
    store[key] = value


def get_value(store: dict[str, object], key: str) -> object | None:
    return store.get(key)


def user_session_keys(store: dict[str, object], user_id: int) -> list[str]:
    matches: list[str] = []
    for key, value in store.items():
        if not key.startswith("session:"):
            continue
        if not isinstance(value, dict):
            continue
        if int(value.get("user_id", -1)) == user_id:
            matches.append(key)
    return sorted(matches)


def access_summary(
    store: dict[str, object],
    key: str,
    user_id: int,
) -> dict[str, object]:
    return {
        "point_lookup_found": key in store,
        "matching_session_keys": user_session_keys(store, user_id),
        "needs_scan_for_secondary_query": True,
    }
