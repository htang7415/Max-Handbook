from __future__ import annotations

import pytest

from hierarchical_benchmark_aggregation import (
    hierarchical_benchmark_route,
    hierarchical_benchmark_summary,
    weighted_group_score,
)


def test_hierarchical_benchmark_aggregation_rolls_up_bucket_and_group_scores() -> None:
    tree = {
        "tool-use": {
            "selection": {"score": 0.9, "weight": 2.0},
            "execution": {"score": 0.6, "weight": 1.0},
        },
        "safety": {
            "guardrails": {"score": 0.8, "weight": 1.0},
            "approval": {"score": 0.7, "weight": 1.0},
        },
    }

    assert weighted_group_score(tree["tool-use"]) == {
        "score": pytest.approx(0.8),
        "weight": pytest.approx(3.0),
    }
    summary = hierarchical_benchmark_summary(tree)
    assert summary == {
        "group_scores": {
            "tool-use": pytest.approx(0.8),
            "safety": pytest.approx(0.75),
        },
        "overall_score": pytest.approx(0.78),
    }
    assert hierarchical_benchmark_route(summary, min_overall_score=0.75, min_group_score=0.7) == "pass"


def test_hierarchical_benchmark_aggregation_distinguishes_review_and_fail() -> None:
    review_summary = {
        "group_scores": {"tool-use": 0.82, "safety": 0.66},
        "overall_score": 0.77,
    }
    assert hierarchical_benchmark_route(review_summary, min_overall_score=0.75, min_group_score=0.7) == "review"

    fail_summary = {
        "group_scores": {"tool-use": 0.7, "safety": 0.68},
        "overall_score": 0.72,
    }
    assert hierarchical_benchmark_route(fail_summary, min_overall_score=0.75, min_group_score=0.7) == "fail"


def test_hierarchical_benchmark_aggregation_validation() -> None:
    with pytest.raises(ValueError):
        weighted_group_score({})
    with pytest.raises(ValueError):
        weighted_group_score({"bucket": {"score": 1.1, "weight": 1.0}})
    with pytest.raises(ValueError):
        hierarchical_benchmark_summary({})
    with pytest.raises(ValueError):
        hierarchical_benchmark_route({"group_scores": {}, "overall_score": 0.8}, min_overall_score=0.7, min_group_score=0.6)
