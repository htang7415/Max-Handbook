from __future__ import annotations

import pytest

from pareto_front_benchmark_comparisons import dominates, pareto_front, pareto_route


def test_pareto_front_benchmark_comparisons_identify_non_dominated_variants() -> None:
    variants = {
        "candidate-a": {"success": 0.90, "cost": 3.0, "latency": 400.0},
        "candidate-b": {"success": 0.88, "cost": 2.0, "latency": 300.0},
        "candidate-c": {"success": 0.86, "cost": 2.5, "latency": 500.0},
        "candidate-d": {"success": 0.90, "cost": 4.0, "latency": 450.0},
    }

    assert dominates(
        variants["candidate-a"],
        variants["candidate-d"],
        maximize_metrics=["success"],
        minimize_metrics=["cost", "latency"],
    ) is True
    assert pareto_front(
        variants,
        maximize_metrics=["success"],
        minimize_metrics=["cost", "latency"],
    ) == ["candidate-a", "candidate-b"]
    assert pareto_route(
        "candidate-b",
        variants,
        maximize_metrics=["success"],
        minimize_metrics=["cost", "latency"],
    ) == "frontier"


def test_pareto_front_benchmark_comparisons_flag_dominated_candidates() -> None:
    variants = {
        "candidate-a": {"success": 0.90, "cost": 3.0, "latency": 400.0},
        "candidate-b": {"success": 0.88, "cost": 2.0, "latency": 300.0},
        "candidate-c": {"success": 0.86, "cost": 2.5, "latency": 500.0},
    }
    assert (
        pareto_route(
            "candidate-c",
            variants,
            maximize_metrics=["success"],
            minimize_metrics=["cost", "latency"],
        )
        == "dominated"
    )


def test_pareto_front_benchmark_comparisons_validation() -> None:
    with pytest.raises(ValueError):
        dominates({"success": 0.9}, {"success": 0.8}, maximize_metrics=[], minimize_metrics=[])
    with pytest.raises(ValueError):
        pareto_front({}, maximize_metrics=["success"], minimize_metrics=["cost"])
    with pytest.raises(ValueError):
        pareto_route("missing", {"candidate-a": {"success": 0.9}}, maximize_metrics=["success"], minimize_metrics=[])
