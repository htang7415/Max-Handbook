from __future__ import annotations

import pytest

from bayesian_benchmark_updating import (
    benchmark_belief_route,
    posterior_benchmark_summary,
    updated_beta_posterior,
)


def test_bayesian_benchmark_updating_updates_posterior_and_summary() -> None:
    posterior = updated_beta_posterior(prior_alpha=2.0, prior_beta=2.0, successes=18, failures=2)

    assert posterior == {"alpha": pytest.approx(20.0), "beta": pytest.approx(4.0)}
    summary = posterior_benchmark_summary(posterior["alpha"], posterior["beta"])
    assert summary == {
        "posterior_mean": pytest.approx(0.8333333333),
        "posterior_variance": pytest.approx(0.0055555556),
        "effective_sample_size": pytest.approx(24.0),
    }
    assert benchmark_belief_route(summary["posterior_mean"], summary["posterior_variance"], min_mean=0.8, max_variance=0.01) == "pass"


def test_bayesian_benchmark_updating_distinguishes_fail_and_review() -> None:
    fail_summary = posterior_benchmark_summary(4.0, 4.0)
    assert benchmark_belief_route(fail_summary["posterior_mean"], fail_summary["posterior_variance"], min_mean=0.7, max_variance=0.04) == "fail"

    review_summary = posterior_benchmark_summary(8.0, 1.0)
    assert benchmark_belief_route(review_summary["posterior_mean"], review_summary["posterior_variance"], min_mean=0.7, max_variance=0.009) == "review"


def test_bayesian_benchmark_updating_validation() -> None:
    with pytest.raises(ValueError):
        updated_beta_posterior(0.0, 1.0, successes=1, failures=0)
    with pytest.raises(ValueError):
        updated_beta_posterior(1.0, 1.0, successes=-1, failures=0)
    with pytest.raises(ValueError):
        posterior_benchmark_summary(0.0, 1.0)
    with pytest.raises(ValueError):
        benchmark_belief_route(1.1, 0.01, min_mean=0.8, max_variance=0.1)
