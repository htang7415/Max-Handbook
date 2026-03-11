from __future__ import annotations

import pytest

from posterior_routing import (
    beta_posterior_mean,
    posterior_route,
    posterior_route_scores,
)


def test_posterior_routing_scores_routes_from_success_failure_evidence() -> None:
    route_outcomes = {
        "search-docs": {"successes": 8, "failures": 2},
        "email-agent": {"successes": 5, "failures": 5},
        "calendar-agent": {"successes": 1, "failures": 1},
    }

    assert beta_posterior_mean(8, 2) == pytest.approx(0.75)
    assert posterior_route_scores(route_outcomes) == [
        {
            "route": "search-docs",
            "posterior_mean": pytest.approx(0.75),
            "posterior_variance": pytest.approx(0.0144230769),
        },
        {
            "route": "email-agent",
            "posterior_mean": pytest.approx(0.5),
            "posterior_variance": pytest.approx(0.0192307692),
        },
        {
            "route": "calendar-agent",
            "posterior_mean": pytest.approx(0.5),
            "posterior_variance": pytest.approx(0.05),
        },
    ]
    assert posterior_route(route_outcomes, min_mean=0.7, min_margin=0.1, max_variance=0.02) == "search-docs"


def test_posterior_routing_distinguishes_clarify_and_review() -> None:
    assert (
        posterior_route(
            {
                "route-a": {"successes": 1, "failures": 1},
                "route-b": {"successes": 0, "failures": 1},
            },
            min_mean=0.7,
            min_margin=0.1,
            max_variance=0.1,
        )
        == "clarify"
    )
    assert (
        posterior_route(
            {
                "route-a": {"successes": 6, "failures": 2},
                "route-b": {"successes": 5, "failures": 2},
            },
            min_mean=0.6,
            min_margin=0.1,
            max_variance=0.03,
        )
        == "review"
    )


def test_posterior_routing_validation() -> None:
    with pytest.raises(ValueError):
        beta_posterior_mean(-1, 2)
    with pytest.raises(ValueError):
        posterior_route_scores({}, alpha=1.0, beta=1.0)
    with pytest.raises(ValueError):
        posterior_route({"route-a": {"successes": 1, "failures": 0}}, min_mean=1.1)
