"""negative_caching_patterns - cache stable misses briefly to avoid repeated origin lookups."""

from __future__ import annotations


def validate_negative_ttl(ttl: int) -> None:
    if ttl <= 0:
        raise ValueError("negative_ttl must be positive")


def negative_entry(now: int, ttl: int) -> dict[str, object]:
    validate_negative_ttl(ttl)
    return {
        "kind": "missing",
        "expires_at": now + ttl,
    }


def expired_negative_keys(cache: dict[str, object], now: int) -> list[str]:
    expired: list[str] = []
    for key, value in cache.items():
        if isinstance(value, dict) and value.get("kind") == "missing" and now >= int(value["expires_at"]):
            expired.append(key)
    return sorted(expired)


def purge_expired_negative(cache: dict[str, object], now: int) -> None:
    for key in expired_negative_keys(cache, now):
        cache.pop(key, None)


def read_with_negative_cache(
    store: dict[str, str],
    cache: dict[str, object],
    key: str,
    now: int,
    negative_ttl: int,
) -> tuple[str | None, bool]:
    validate_negative_ttl(negative_ttl)
    purge_expired_negative(cache, now)

    if key in cache:
        value = cache[key]
        if isinstance(value, dict) and value.get("kind") == "missing":
            return None, False
        return str(value), False

    if key in store:
        value = store[key]
        cache[key] = value
        return value, True

    cache[key] = negative_entry(now, negative_ttl)
    return None, True
