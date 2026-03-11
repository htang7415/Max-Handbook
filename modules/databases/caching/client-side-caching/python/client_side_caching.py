"""client_side_caching - local cache entries must be invalidated after server writes."""

from __future__ import annotations


def client_read(
    server: dict[str, tuple[str, int]],
    client_cache: dict[str, tuple[str, int]],
    key: str,
) -> str | None:
    cached = client_cache.get(key)
    if cached is not None:
        return cached[0]
    current = server.get(key)
    if current is None:
        return None
    client_cache[key] = current
    return current[0]


def server_update(
    server: dict[str, tuple[str, int]],
    invalidations: list[str],
    key: str,
    value: str,
) -> None:
    current_version = 0 if key not in server else int(server[key][1])
    server[key] = (value, current_version + 1)
    invalidations.append(key)


def apply_invalidations(
    client_cache: dict[str, tuple[str, int]],
    invalidations: list[str],
) -> None:
    for key in list(invalidations):
        client_cache.pop(key, None)
        invalidations.remove(key)


def stale_client_keys(
    server: dict[str, tuple[str, int]],
    client_cache: dict[str, tuple[str, int]],
) -> list[str]:
    stale: list[str] = []
    for key, cached in client_cache.items():
        current = server.get(key)
        if current is None or current[1] != cached[1]:
            stale.append(key)
    return sorted(stale)
