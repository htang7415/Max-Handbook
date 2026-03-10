from __future__ import annotations

import math


def temperature_scaled_logits(logits: list[float], temperature: float) -> list[float]:
    if temperature <= 0.0:
        raise ValueError("temperature must be positive")
    return [logit / temperature for logit in logits]


def greedy_choice(scores: list[float]) -> int:
    if not scores:
        raise ValueError("scores must be non-empty")
    return max(range(len(scores)), key=lambda index: scores[index])


def temperature_probabilities(logits: list[float], temperature: float) -> list[float]:
    if not logits:
        return []

    scaled = temperature_scaled_logits(logits, temperature)
    max_scaled = max(scaled)
    exps = [math.exp(value - max_scaled) for value in scaled]
    total = sum(exps)
    return [value / total for value in exps]


def top_k_filter(probabilities: list[float], k: int) -> list[int]:
    if k <= 0:
        raise ValueError("k must be positive")
    if not probabilities:
        return []
    if any(probability < 0.0 for probability in probabilities):
        raise ValueError("probabilities must be non-negative")

    ranked = sorted(enumerate(probabilities), key=lambda item: item[1], reverse=True)
    return [index for index, _ in ranked[: min(k, len(ranked))]]


def top_p_filter(probabilities: list[float], p: float) -> list[int]:
    if not 0.0 < p <= 1.0:
        raise ValueError("p must satisfy 0 < p <= 1")
    if not probabilities:
        return []
    if any(probability < 0.0 for probability in probabilities):
        raise ValueError("probabilities must be non-negative")

    total = sum(probabilities)
    if total <= 0.0:
        raise ValueError("probabilities must sum to a positive value")

    normalized = [probability / total for probability in probabilities]
    ranked = sorted(enumerate(normalized), key=lambda item: item[1], reverse=True)

    kept: list[int] = []
    cumulative = 0.0
    for index, probability in ranked:
        kept.append(index)
        cumulative += probability
        if cumulative >= p:
            break
    return kept


def sampling_pipeline_candidates(
    logits: list[float],
    temperature: float,
    top_k: int,
    top_p: float,
) -> list[int]:
    probabilities = temperature_probabilities(logits, temperature)
    if not probabilities:
        return []

    top_k_indices = top_k_filter(probabilities, top_k)
    top_k_probabilities = [probabilities[index] for index in top_k_indices]
    kept_relative = top_p_filter(top_k_probabilities, top_p)
    return [top_k_indices[index] for index in kept_relative]


def beam_search_step(
    beams: list[tuple[list[int], float]],
    next_token_log_probs: list[list[float]],
    beam_width: int,
) -> list[tuple[list[int], float]]:
    if len(beams) != len(next_token_log_probs):
        raise ValueError("beams and next_token_log_probs must have the same length")
    if beam_width <= 0:
        raise ValueError("beam_width must be positive")
    if not beams:
        return []

    candidates: list[tuple[list[int], float]] = []
    for (tokens, score), token_scores in zip(beams, next_token_log_probs):
        for token_id, token_log_prob in enumerate(token_scores):
            candidates.append((tokens + [token_id], score + token_log_prob))

    candidates.sort(key=lambda item: item[1], reverse=True)
    return candidates[:beam_width]
