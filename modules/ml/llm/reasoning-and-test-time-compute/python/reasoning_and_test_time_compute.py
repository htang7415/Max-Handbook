from __future__ import annotations

import math


def _validate_probability(value: float) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError("probability must satisfy 0 <= value <= 1")


def total_inference_tokens(
    prompt_tokens: int,
    reasoning_tokens: int,
    answer_tokens: int,
    samples: int = 1,
) -> int:
    values = [prompt_tokens, reasoning_tokens, answer_tokens]
    if any(value < 0 for value in values):
        raise ValueError("token counts must be non-negative")
    if samples <= 0:
        raise ValueError("samples must be positive")
    return samples * (prompt_tokens + reasoning_tokens + answer_tokens)


def test_time_compute_multiplier(
    prompt_tokens: int,
    reasoning_tokens: int,
    answer_tokens: int,
    samples: int = 1,
) -> float:
    baseline_tokens = prompt_tokens + answer_tokens
    if baseline_tokens <= 0:
        raise ValueError("prompt_tokens + answer_tokens must be positive")
    total_tokens = total_inference_tokens(
        prompt_tokens=prompt_tokens,
        reasoning_tokens=reasoning_tokens,
        answer_tokens=answer_tokens,
        samples=samples,
    )
    return total_tokens / baseline_tokens


test_time_compute_multiplier.__test__ = False


def best_of_n_success_probability(single_try_success: float, n: int) -> float:
    _validate_probability(single_try_success)
    if n <= 0:
        raise ValueError("n must be positive")
    return 1.0 - (1.0 - single_try_success) ** n


def majority_vote_success_probability(single_try_success: float, n: int) -> float:
    _validate_probability(single_try_success)
    if n <= 0:
        raise ValueError("n must be positive")
    if n % 2 == 0:
        raise ValueError("n must be odd for a strict majority")

    threshold = n // 2 + 1
    probability = 0.0
    for k in range(threshold, n + 1):
        probability += (
            math.comb(n, k)
            * (single_try_success**k)
            * ((1.0 - single_try_success) ** (n - k))
        )
    return probability
