from outbox_relay_failures import relay_summary


def test_crash_after_publish_replays_the_same_event_on_retry() -> None:
    assert relay_summary([1, 2], first_failure_event_id=1) == {
        "published_ids": [1, 1, 2],
        "duplicate_published_ids": [1],
        "marked_ids": [1, 2],
        "pending_ids": [],
    }


def test_no_failure_marks_each_event_once() -> None:
    assert relay_summary([1, 2], first_failure_event_id=None) == {
        "published_ids": [1, 2],
        "duplicate_published_ids": [],
        "marked_ids": [1, 2],
        "pending_ids": [],
    }
