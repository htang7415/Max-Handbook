from __future__ import annotations

import pytest

from uncertainty_aware_routing import (
    normalized_route_scores,
    route_entropy,
    uncertainty_route,
)


def test_uncertainty_aware_routing_normalizes_scores_and_selects_clear_winner() -> None:
    route_scores = {"search-docs": 0.8, "email-agent": 0.15, "calendar-agent": 0.05}
    ranked = normalized_route_scores(route_scores)

    assert ranked == [
        {"route": "search-docs", "raw_score": pytest.approx(0.8), "probability": pytest.approx(0.8)},
        {"route": "email-agent", "raw_score": pytest.approx(0.15), "probability": pytest.approx(0.15)},
        {"route": "calendar-agent", "raw_score": pytest.approx(0.05), "probability": pytest.approx(0.05)},
    ]
    assert route_entropy(route_scores) == pytest.approx(0.5578578164, rel=1e-6)
    assert uncertainty_route(route_scores, min_top_score=0.6, min_margin=0.15, max_entropy=0.9) == "search-docs"


def test_uncertainty_aware_routing_distinguishes_clarify_and_review() -> None:
    assert (
        uncertainty_route(
            {"search-docs": 0.4, "email-agent": 0.35, "calendar-agent": 0.25},
            min_top_score=0.6,
            min_margin=0.15,
            max_entropy=0.9,
        )
        == "clarify"
    )
    assert (
        uncertainty_route(
            {"search-docs": 0.8, "email-agent": 0.75, "calendar-agent": 0.05},
            min_top_score=0.6,
            min_margin=0.15,
            max_entropy=0.9,
        )
        == "review"
    )


def test_uncertainty_aware_routing_validation() -> None:
    with pytest.raises(ValueError):
        normalized_route_scores({})
    with pytest.raises(ValueError):
        normalized_route_scores({"search-docs": -0.1})
    with pytest.raises(ValueError):
        uncertainty_route({"search-docs": 1.0}, min_top_score=1.1, min_margin=0.1, max_entropy=0.8)
