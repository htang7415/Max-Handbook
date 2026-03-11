from write_through_vs_write_behind import (
    flush_pending_writes,
    write_behind_update,
    write_through_update,
    write_view,
)


def test_write_through_updates_store_and_cache_immediately() -> None:
    store = {"profile:1": "old"}
    cache: dict[str, str] = {}
    pending: dict[str, str] = {}

    write_through_update(store, cache, "profile:1", "new")

    assert write_view(store, cache, pending, "profile:1") == {
        "store_value": "new",
        "cache_value": "new",
        "pending_flush": False,
    }


def test_write_behind_leaves_store_stale_until_flush() -> None:
    store = {"profile:1": "old"}
    cache: dict[str, str] = {}
    pending: dict[str, str] = {}

    write_behind_update(store, cache, pending, "profile:1", "new")

    assert write_view(store, cache, pending, "profile:1") == {
        "store_value": "old",
        "cache_value": "new",
        "pending_flush": True,
    }

    flush_pending_writes(store, pending)

    assert write_view(store, cache, pending, "profile:1") == {
        "store_value": "new",
        "cache_value": "new",
        "pending_flush": False,
    }
