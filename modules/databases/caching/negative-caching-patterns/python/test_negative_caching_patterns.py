from negative_caching_patterns import (
    expired_negative_keys,
    purge_expired_negative,
    read_with_negative_cache,
)
import pytest


def test_repeated_missing_key_hits_negative_cache_instead_of_origin():
    store = {"doc:1": "alpha"}
    cache: dict[str, object] = {}

    assert read_with_negative_cache(store, cache, "doc:404", now=100, negative_ttl=30) == (None, True)
    assert read_with_negative_cache(store, cache, "doc:404", now=110, negative_ttl=30) == (None, False)


def test_negative_entries_expire_and_allow_recheck():
    store: dict[str, str] = {}
    cache: dict[str, object] = {}
    read_with_negative_cache(store, cache, "doc:404", now=100, negative_ttl=10)

    assert expired_negative_keys(cache, now=111) == ["doc:404"]
    purge_expired_negative(cache, now=111)
    assert read_with_negative_cache(store, cache, "doc:404", now=111, negative_ttl=10) == (None, True)


def test_negative_ttl_must_be_positive():
    with pytest.raises(ValueError, match="negative_ttl"):
        read_with_negative_cache({}, {}, "doc:404", now=100, negative_ttl=0)
