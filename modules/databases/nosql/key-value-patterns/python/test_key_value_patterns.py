from key_value_patterns import access_summary, get_value, put_value, user_session_keys


def test_point_lookup_returns_value_by_exact_key() -> None:
    store: dict[str, object] = {}
    put_value(store, "session:s1", {"user_id": 42})

    assert get_value(store, "session:s1") == {"user_id": 42}


def test_secondary_lookup_requires_scanning_session_values() -> None:
    store: dict[str, object] = {
        "session:s1": {"user_id": 42},
        "session:s2": {"user_id": 42},
        "session:s3": {"user_id": 7},
    }

    assert user_session_keys(store, 42) == ["session:s1", "session:s2"]
    assert access_summary(store, "session:s1", 42)["needs_scan_for_secondary_query"] is True
