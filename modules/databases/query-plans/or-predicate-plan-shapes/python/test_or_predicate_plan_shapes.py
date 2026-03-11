import pytest

from or_predicate_plan_shapes import or_plan_summary, recommended_path


def test_narrow_or_predicates_can_prefer_index_union() -> None:
    summary = or_plan_summary(
        total_rows=1_000_000,
        left_selectivity=0.002,
        right_selectivity=0.003,
        overlap_selectivity=0.0001,
    )

    assert summary["recommended_path"] == "index-union"
    assert int(summary["index_union_cost"]) < int(summary["seq_scan_cost"])


def test_broad_or_predicates_can_fall_back_to_seq_scan() -> None:
    assert (
        recommended_path(
            total_rows=1_000,
            left_selectivity=0.4,
            right_selectivity=0.5,
            overlap_selectivity=0.1,
        )
        == "seq-scan"
    )


def test_invalid_selectivity_is_rejected() -> None:
    with pytest.raises(ValueError, match="selectivity"):
        recommended_path(100, -0.1, 0.2, 0.0)


def test_invalid_overlap_is_rejected() -> None:
    with pytest.raises(ValueError, match="overlap_selectivity"):
        recommended_path(100, 0.1, 0.2, 0.3)
