from __future__ import annotations

import pytest

from experiment_comparison import compare_variant_scores, comparison_summary, success_delta


def test_experiment_comparison_summarizes_variant_delta() -> None:
    assert success_delta(0.72, 0.81) == pytest.approx(0.09)
    assert compare_variant_scores(
        {"success": 0.72, "latency_ms": 120.0},
        {"success": 0.81, "latency_ms": 140.0},
    ) == "candidate"
    assert comparison_summary("A", "B", 0.72, 0.81) == "B vs A: success 0.81 vs 0.72 (delta +0.09)"


def test_experiment_comparison_validation_and_tie_break() -> None:
    assert compare_variant_scores(
        {"success": 0.80, "latency_ms": 140.0},
        {"success": 0.80, "latency_ms": 120.0},
    ) == "candidate"
    with pytest.raises(ValueError):
        success_delta(-0.1, 0.8)
    with pytest.raises(ValueError):
        comparison_summary("A", "B", 0.7, 1.2)
