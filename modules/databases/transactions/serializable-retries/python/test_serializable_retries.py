from serializable_retries import run_serializable_retry_loop, should_backoff


def test_conflicts_can_be_resolved_by_retrying_until_one_attempt_commits() -> None:
    assert run_serializable_retry_loop([True, True, False], max_retries=3) == {
        "attempts": 3,
        "retries_used": 2,
        "committed": True,
    }


def test_retry_budget_can_be_exhausted() -> None:
    assert run_serializable_retry_loop([True, True, True], max_retries=2) == {
        "attempts": 3,
        "retries_used": 2,
        "committed": False,
    }
    assert should_backoff([True, False]) is True
