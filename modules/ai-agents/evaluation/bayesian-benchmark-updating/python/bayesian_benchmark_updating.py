from __future__ import annotations


def updated_beta_posterior(
    prior_alpha: float,
    prior_beta: float,
    successes: int,
    failures: int,
) -> dict[str, float]:
    if prior_alpha <= 0.0 or prior_beta <= 0.0:
        raise ValueError("prior_alpha and prior_beta must be positive")
    if successes < 0 or failures < 0:
        raise ValueError("successes and failures must be non-negative")
    return {
        "alpha": prior_alpha + successes,
        "beta": prior_beta + failures,
    }


def posterior_benchmark_summary(alpha: float, beta: float) -> dict[str, float]:
    if alpha <= 0.0 or beta <= 0.0:
        raise ValueError("alpha and beta must be positive")
    total = alpha + beta
    posterior_mean = alpha / total
    posterior_variance = alpha * beta / (total * total * (total + 1.0))
    return {
        "posterior_mean": posterior_mean,
        "posterior_variance": posterior_variance,
        "effective_sample_size": total,
    }


def benchmark_belief_route(
    posterior_mean: float,
    posterior_variance: float,
    min_mean: float,
    max_variance: float,
) -> str:
    if not 0.0 <= posterior_mean <= 1.0:
        raise ValueError("posterior_mean must satisfy 0 <= value <= 1")
    if not 0.0 <= posterior_variance <= 1.0:
        raise ValueError("posterior_variance must satisfy 0 <= value <= 1")
    if not 0.0 <= min_mean <= 1.0:
        raise ValueError("min_mean must satisfy 0 <= value <= 1")
    if not 0.0 <= max_variance <= 1.0:
        raise ValueError("max_variance must satisfy 0 <= value <= 1")

    if posterior_mean < min_mean:
        return "fail"
    if posterior_variance > max_variance:
        return "review"
    return "pass"
