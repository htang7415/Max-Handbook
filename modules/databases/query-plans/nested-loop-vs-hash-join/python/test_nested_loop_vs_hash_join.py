from nested_loop_vs_hash_join import choose_join_strategy, join_cost_summary


def test_small_outer_with_index_prefers_nested_loop() -> None:
    assert (
        choose_join_strategy(outer_rows=10, inner_rows=100_000, indexed_lookup=True)
        == "nested-loop"
    )


def test_large_inputs_without_good_probe_path_prefers_hash_join() -> None:
    summary = join_cost_summary(
        outer_rows=5_000,
        inner_rows=20_000,
        indexed_lookup=False,
    )

    assert summary["recommended_strategy"] == "hash-join"
    assert int(summary["hash_join_cost"]) < int(summary["nested_loop_cost"])
