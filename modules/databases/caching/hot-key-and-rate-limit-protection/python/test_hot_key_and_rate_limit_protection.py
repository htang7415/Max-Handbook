from hot_key_and_rate_limit_protection import (
    allow_request,
    hot_keys,
    protected_origin_requests,
)


def test_hot_keys_finds_repeated_cache_targets():
    requests = [
        "workspace:7:doc:42",
        "workspace:7:doc:42",
        "workspace:7:doc:42",
        "workspace:7:doc:99",
    ]

    assert hot_keys(requests, threshold=3) == ["workspace:7:doc:42"]


def test_allow_request_blocks_after_rolling_window_limit():
    state: dict[tuple[str, str], list[int]] = {}

    assert allow_request(state, "user-1", "doc:42", now=10, max_requests=2, window_seconds=30)
    assert allow_request(state, "user-1", "doc:42", now=20, max_requests=2, window_seconds=30)
    assert not allow_request(
        state,
        "user-1",
        "doc:42",
        now=25,
        max_requests=2,
        window_seconds=30,
    )
    assert allow_request(state, "user-1", "doc:42", now=45, max_requests=2, window_seconds=30)


def test_protected_origin_requests_only_throttles_hot_keys():
    allowed = protected_origin_requests(
        [
            {"actor_id": "user-1", "key": "doc:42", "now": 0},
            {"actor_id": "user-1", "key": "doc:42", "now": 1},
            {"actor_id": "user-1", "key": "doc:42", "now": 2},
            {"actor_id": "user-1", "key": "doc:42", "now": 3},
            {"actor_id": "user-1", "key": "doc:99", "now": 4},
        ],
        hot_threshold=2,
        max_requests=2,
        window_seconds=10,
    )

    assert allowed == [True, True, True, False, True]
