import pytest

from index_merge_vs_composite_indexes import recommended_strategy, strategy_summary


def test_rare_combined_filter_prefers_composite_index() -> None:
    summary = strategy_summary(
        total_rows=1_000_000,
        left_selectivity=0.01,
        right_selectivity=0.02,
        overlap_selectivity=0.0005,
    )

    assert summary["recommended_strategy"] == "composite-index"
    assert int(summary["composite_index_cost"]) < int(summary["index_merge_cost"])


def test_broad_predicates_can_make_seq_scan_cheaper() -> None:
    assert (
        recommended_strategy(
            total_rows=1_000,
            left_selectivity=0.7,
            right_selectivity=0.8,
            overlap_selectivity=0.7,
        )
        == "seq-scan"
    )


def test_invalid_selectivity_is_rejected() -> None:
    with pytest.raises(ValueError, match="selectivity"):
        recommended_strategy(100, 1.2, 0.1, 0.05)


def test_invalid_overlap_is_rejected() -> None:
    with pytest.raises(ValueError, match="overlap_selectivity"):
        recommended_strategy(100, 0.1, 0.2, 0.3)
