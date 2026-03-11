from __future__ import annotations

import math


def normalized_route_scores(route_scores: dict[str, float]) -> list[dict[str, object]]:
    if not route_scores:
        raise ValueError("route_scores must be non-empty")

    cleaned_scores: list[dict[str, object]] = []
    total_score = 0.0
    for route_name, score in route_scores.items():
        cleaned_route = route_name.strip()
        if not cleaned_route:
            raise ValueError("route names must be non-empty")
        if score < 0.0:
            raise ValueError("route scores must be non-negative")
        cleaned_scores.append({"route": cleaned_route, "raw_score": score})
        total_score += score

    if total_score <= 0.0:
        raise ValueError("route scores must sum to a positive value")

    normalized: list[dict[str, object]] = []
    for item in cleaned_scores:
        normalized.append(
            {
                "route": item["route"],
                "raw_score": float(item["raw_score"]),
                "probability": float(item["raw_score"]) / total_score,
            }
        )

    return sorted(
        normalized,
        key=lambda item: (-float(item["probability"]), str(item["route"])),
    )


def route_entropy(route_scores: dict[str, float]) -> float:
    ranked = normalized_route_scores(route_scores)
    if len(ranked) == 1:
        return 0.0

    entropy = 0.0
    for item in ranked:
        probability = float(item["probability"])
        if probability > 0.0:
            entropy -= probability * math.log2(probability)
    return entropy / math.log2(len(ranked))


def uncertainty_route(
    route_scores: dict[str, float],
    min_top_score: float,
    min_margin: float,
    max_entropy: float,
) -> str:
    if not 0.0 <= min_top_score <= 1.0:
        raise ValueError("min_top_score must satisfy 0 <= value <= 1")
    if min_margin < 0.0:
        raise ValueError("min_margin must be non-negative")
    if not 0.0 <= max_entropy <= 1.0:
        raise ValueError("max_entropy must satisfy 0 <= value <= 1")

    ranked = normalized_route_scores(route_scores)
    top = ranked[0]
    top_raw_score = float(top["raw_score"])
    if top_raw_score < min_top_score:
        return "clarify"

    top_probability = float(top["probability"])
    second_probability = float(ranked[1]["probability"]) if len(ranked) > 1 else 0.0
    margin = top_probability - second_probability
    if margin < min_margin or route_entropy(route_scores) > max_entropy:
        return "review"
    return str(top["route"])
