import pytest

from join_selectivity_mistakes import filtered_rows, plan_outcome


def test_underestimated_selectivity_can_pick_nested_loop_when_hash_join_is_better() -> None:
    summary = plan_outcome(
        base_outer_rows=1_000,
        estimated_selectivity=0.005,
        actual_selectivity=0.5,
        inner_rows=10_000,
        nested_loop_outer_threshold=10,
    )

    assert summary == {
        "estimated_outer_rows": 5,
        "actual_outer_rows": 500,
        "chosen_strategy": "nested-loop",
        "estimated_work": 50_000,
        "actual_work": 5_000_000,
        "better_actual_strategy": "hash-join",
    }


def test_accurate_estimate_switches_to_hash_join() -> None:
    summary = plan_outcome(
        base_outer_rows=1_000,
        estimated_selectivity=0.5,
        actual_selectivity=0.5,
        inner_rows=10_000,
        nested_loop_outer_threshold=10,
    )

    assert summary["chosen_strategy"] == "hash-join"
    assert summary["actual_work"] == 10_500
    assert summary["better_actual_strategy"] == "hash-join"


def test_invalid_selectivity_is_rejected() -> None:
    with pytest.raises(ValueError):
        filtered_rows(100, 1.2)
