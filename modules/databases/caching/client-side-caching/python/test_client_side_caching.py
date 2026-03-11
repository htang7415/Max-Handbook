from client_side_caching import (
    apply_invalidations,
    client_read,
    server_update,
    stale_client_keys,
)


def test_client_cache_can_serve_stale_data_when_invalidation_is_missed() -> None:
    server = {"doc:1": ("v1", 1)}
    client_cache: dict[str, tuple[str, int]] = {}
    invalidations: list[str] = []

    assert client_read(server, client_cache, "doc:1") == "v1"

    server_update(server, invalidations, "doc:1", "v2")

    assert client_read(server, client_cache, "doc:1") == "v1"
    assert stale_client_keys(server, client_cache) == ["doc:1"]


def test_invalidation_clears_local_copy_and_next_read_fetches_fresh_value() -> None:
    server = {"doc:1": ("v1", 1)}
    client_cache: dict[str, tuple[str, int]] = {}
    invalidations: list[str] = []

    assert client_read(server, client_cache, "doc:1") == "v1"
    server_update(server, invalidations, "doc:1", "v2")
    apply_invalidations(client_cache, invalidations)

    assert client_read(server, client_cache, "doc:1") == "v2"
    assert stale_client_keys(server, client_cache) == []
