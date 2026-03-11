from __future__ import annotations


def _validate_beta_prior(alpha: float, beta: float) -> None:
    if alpha <= 0.0 or beta <= 0.0:
        raise ValueError("alpha and beta must be positive")


def _posterior_variance(successes: int, failures: int, alpha: float, beta: float) -> float:
    posterior_alpha = successes + alpha
    posterior_beta = failures + beta
    total = posterior_alpha + posterior_beta
    return posterior_alpha * posterior_beta / (total * total * (total + 1.0))


def beta_posterior_mean(successes: int, failures: int, alpha: float = 1.0, beta: float = 1.0) -> float:
    if successes < 0 or failures < 0:
        raise ValueError("successes and failures must be non-negative")
    _validate_beta_prior(alpha, beta)

    posterior_alpha = successes + alpha
    posterior_beta = failures + beta
    return posterior_alpha / (posterior_alpha + posterior_beta)


def posterior_route_scores(
    route_to_outcomes: dict[str, dict[str, int]],
    alpha: float = 1.0,
    beta: float = 1.0,
) -> list[dict[str, object]]:
    if not route_to_outcomes:
        raise ValueError("route_to_outcomes must be non-empty")
    _validate_beta_prior(alpha, beta)

    ranked: list[dict[str, object]] = []
    for route_name, outcomes in route_to_outcomes.items():
        cleaned_route = route_name.strip()
        if not cleaned_route:
            raise ValueError("route names must be non-empty")

        successes = int(outcomes.get("successes", 0))
        failures = int(outcomes.get("failures", 0))
        if successes < 0 or failures < 0:
            raise ValueError("successes and failures must be non-negative")

        ranked.append(
            {
                "route": cleaned_route,
                "posterior_mean": beta_posterior_mean(successes, failures, alpha=alpha, beta=beta),
                "posterior_variance": _posterior_variance(successes, failures, alpha=alpha, beta=beta),
            }
        )

    return sorted(
        ranked,
        key=lambda item: (-float(item["posterior_mean"]), float(item["posterior_variance"]), str(item["route"])),
    )


def posterior_route(
    route_to_outcomes: dict[str, dict[str, int]],
    min_mean: float,
    min_margin: float = 0.0,
    max_variance: float = 1.0,
    alpha: float = 1.0,
    beta: float = 1.0,
) -> str:
    if not 0.0 <= min_mean <= 1.0:
        raise ValueError("min_mean must satisfy 0 <= value <= 1")
    if min_margin < 0.0:
        raise ValueError("min_margin must be non-negative")
    if not 0.0 <= max_variance <= 1.0:
        raise ValueError("max_variance must satisfy 0 <= value <= 1")

    ranked = posterior_route_scores(route_to_outcomes, alpha=alpha, beta=beta)
    top = ranked[0]
    if float(top["posterior_mean"]) < min_mean:
        return "clarify"
    if float(top["posterior_variance"]) > max_variance:
        return "review"

    second_mean = float(ranked[1]["posterior_mean"]) if len(ranked) > 1 else 0.0
    if float(top["posterior_mean"]) - second_mean < min_margin:
        return "review"
    return str(top["route"])
