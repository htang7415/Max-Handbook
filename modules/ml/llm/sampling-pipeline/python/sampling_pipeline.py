from __future__ import annotations

import math


def _temperature_probabilities(logits: list[float], temperature: float) -> list[float]:
    scaled = [logit / temperature for logit in logits]
    max_scaled = max(scaled)
    exps = [math.exp(value - max_scaled) for value in scaled]
    total = sum(exps)
    return [value / total for value in exps]


def sampling_pipeline_candidates(
    logits: list[float],
    temperature: float,
    top_k: int,
    top_p: float,
) -> list[int]:
    if temperature <= 0.0:
        raise ValueError("temperature must be positive")
    if top_k <= 0:
        raise ValueError("top_k must be positive")
    if not 0.0 < top_p <= 1.0:
        raise ValueError("top_p must satisfy 0 < top_p <= 1")
    if not logits:
        return []

    probabilities = _temperature_probabilities(logits, temperature)
    ranked = sorted(enumerate(probabilities), key=lambda item: item[1], reverse=True)
    top_k_ranked = ranked[: min(top_k, len(ranked))]

    top_k_total = sum(probability for _, probability in top_k_ranked)
    cumulative = 0.0
    kept: list[int] = []
    for index, probability in top_k_ranked:
        cumulative += probability / top_k_total
        kept.append(index)
        if cumulative >= top_p:
            break
    return kept
