from cache_stampede_mitigation import cache_entry, finish_refresh, request_action
import pytest


def test_single_flight_refresh_serves_stale_to_followers():
    cache = {"doc:42": cache_entry("old", expires_at=100, stale_until=130)}
    inflight: set[str] = set()

    assert request_action(cache, inflight, "doc:42", now=110) == "refresh"
    assert request_action(cache, inflight, "doc:42", now=111) == "serve-stale"

    finish_refresh(cache, inflight, "doc:42", "new", now=112, ttl=30, stale_window=60)

    assert request_action(cache, inflight, "doc:42", now=113) == "hit"
    assert cache["doc:42"]["value"] == "new"


def test_cold_miss_forces_wait_instead_of_duplicate_origin_loads():
    cache: dict[str, dict[str, object]] = {}
    inflight: set[str] = set()

    assert request_action(cache, inflight, "doc:99", now=10) == "refresh"
    assert request_action(cache, inflight, "doc:99", now=11) == "wait"

    finish_refresh(cache, inflight, "doc:99", "filled", now=12, ttl=20, stale_window=40)

    assert request_action(cache, inflight, "doc:99", now=13) == "hit"


def test_invalid_timing_windows_are_rejected() -> None:
    with pytest.raises(ValueError, match="stale_until"):
        cache_entry("bad", expires_at=20, stale_until=10)

    with pytest.raises(ValueError, match="ttl"):
        finish_refresh({}, set(), "doc:1", "x", now=10, ttl=0, stale_window=10)
