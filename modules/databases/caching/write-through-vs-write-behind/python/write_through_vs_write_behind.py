"""write_through_vs_write_behind - compare immediate and buffered cache write paths."""

from __future__ import annotations


def write_through_update(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
    value: str,
) -> None:
    store[key] = value
    cache[key] = value


def write_behind_update(
    store: dict[str, str],
    cache: dict[str, str],
    pending_writes: dict[str, str],
    key: str,
    value: str,
) -> None:
    del store
    cache[key] = value
    pending_writes[key] = value


def flush_pending_writes(
    store: dict[str, str],
    pending_writes: dict[str, str],
) -> None:
    for key, value in list(pending_writes.items()):
        store[key] = value
        pending_writes.pop(key, None)


def write_view(
    store: dict[str, str],
    cache: dict[str, str],
    pending_writes: dict[str, str],
    key: str,
) -> dict[str, str | bool | None]:
    return {
        "store_value": store.get(key),
        "cache_value": cache.get(key),
        "pending_flush": key in pending_writes,
    }
