from sort_limit_and_group_by_costs import (
    choose_order_plan,
    full_sort_work_units,
    hash_group_by_work_units,
    plan_cost_summary,
    top_n_sort_work_units,
)


def test_top_n_sort_cost_is_lower_than_full_sort_for_small_limits() -> None:
    assert top_n_sort_work_units(100_000, 20) < full_sort_work_units(100_000)


def test_covering_index_avoids_sort_work() -> None:
    summary = plan_cost_summary(
        row_count=100_000,
        limit=20,
        distinct_groups=500,
        has_covering_index=True,
    )

    assert choose_order_plan(100_000, 20, has_covering_index=True) == "index-order-scan"
    assert summary["sort_work"] == 0.0


def test_group_by_work_grows_with_input_rows_and_group_count() -> None:
    assert hash_group_by_work_units(100_000, 500) == 100_500
