import pytest

from token_budgeting import budget_token_segments


def test_budget_token_segments_truncates_later_segments_when_budget_runs_out() -> None:
    allocated, dropped = budget_token_segments([50, 30, 40], max_tokens=100)

    assert allocated == [50, 30, 20]
    assert dropped == 20


def test_budget_token_segments_keeps_all_segments_when_budget_is_large_enough() -> None:
    allocated, dropped = budget_token_segments([10, 15, 5], max_tokens=40)

    assert allocated == [10, 15, 5]
    assert dropped == 0


def test_budget_token_segments_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        budget_token_segments([10, -2], max_tokens=20)
