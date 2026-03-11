import pytest

from low_cardinality_index_tradeoffs import recommended_path, tradeoff_summary


def test_rare_predicate_prefers_index_scan() -> None:
    summary = tradeoff_summary(total_rows=1_000_000, match_fraction=0.001)

    assert summary["recommended_path"] == "index-scan"
    assert int(summary["index_scan_cost"]) < int(summary["seq_scan_cost"])


def test_dense_predicate_prefers_seq_scan() -> None:
    assert recommended_path(total_rows=1_000_000, match_fraction=0.5) == "seq-scan"


def test_invalid_fraction_is_rejected() -> None:
    with pytest.raises(ValueError, match="match_fraction"):
        recommended_path(total_rows=10, match_fraction=1.2)
