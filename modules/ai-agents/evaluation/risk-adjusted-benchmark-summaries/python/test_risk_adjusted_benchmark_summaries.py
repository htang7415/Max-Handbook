from __future__ import annotations

import pytest

from risk_adjusted_benchmark_summaries import (
    benchmark_risk_summary,
    risk_adjusted_route,
    risk_adjusted_score,
)


def test_risk_adjusted_benchmark_summaries_score_and_route_candidates() -> None:
    baseline = benchmark_risk_summary("baseline", 0.85, 0.05, 2.0)
    candidate = benchmark_risk_summary("candidate", 0.88, 0.02, 2.0)

    assert baseline["risk_adjusted_score"] == pytest.approx(0.75)
    assert risk_adjusted_score(0.88, 0.02, 2.0) == pytest.approx(0.84)
    assert candidate == {
        "name": "candidate",
        "success_rate": pytest.approx(0.88),
        "high_risk_failure_rate": pytest.approx(0.02),
        "risk_penalty": pytest.approx(2.0),
        "risk_adjusted_score": pytest.approx(0.84),
    }
    assert risk_adjusted_route(candidate["risk_adjusted_score"], baseline["risk_adjusted_score"], min_score=0.7, max_drop=0.05) == "pass"


def test_risk_adjusted_benchmark_summaries_distinguish_review_and_fail() -> None:
    assert risk_adjusted_route(candidate_score=0.72, baseline_score=0.80, min_score=0.7, max_drop=0.05) == "review"
    assert risk_adjusted_route(candidate_score=0.62, baseline_score=0.80, min_score=0.7, max_drop=0.05) == "fail"


def test_risk_adjusted_benchmark_summaries_validation() -> None:
    with pytest.raises(ValueError):
        risk_adjusted_score(1.1, 0.02, 2.0)
    with pytest.raises(ValueError):
        risk_adjusted_score(0.8, 0.02, -1.0)
    with pytest.raises(ValueError):
        benchmark_risk_summary(" ", 0.8, 0.02, 2.0)
    with pytest.raises(ValueError):
        risk_adjusted_route(candidate_score=0.8, baseline_score=0.9, min_score=0.7, max_drop=-0.1)
