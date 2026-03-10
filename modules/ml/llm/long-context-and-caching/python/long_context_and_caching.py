from __future__ import annotations


def quadratic_attention_pairs(sequence_length: int) -> int:
    if sequence_length <= 0:
        raise ValueError("sequence_length must be positive")
    return sequence_length * sequence_length


def context_utilization(total_tokens: int, context_window: int) -> float:
    if total_tokens < 0:
        raise ValueError("total_tokens must be non-negative")
    if context_window <= 0:
        raise ValueError("context_window must be positive")
    return total_tokens / context_window


def effective_prefix_tokens(total_prompt_tokens: int, cached_prefix_tokens: int) -> int:
    if total_prompt_tokens < 0 or cached_prefix_tokens < 0:
        raise ValueError("token counts must be non-negative")
    if cached_prefix_tokens > total_prompt_tokens:
        raise ValueError("cached_prefix_tokens must not exceed total_prompt_tokens")
    return total_prompt_tokens - cached_prefix_tokens


def prompt_cache_saved_tokens(shared_prefix_tokens: int, repeated_requests: int) -> int:
    if shared_prefix_tokens < 0:
        raise ValueError("shared_prefix_tokens must be non-negative")
    if repeated_requests <= 0:
        raise ValueError("repeated_requests must be positive")
    return shared_prefix_tokens * max(0, repeated_requests - 1)


def cache_hit_rate(cached_prefix_tokens: int, total_prompt_tokens: int) -> float:
    if cached_prefix_tokens < 0:
        raise ValueError("cached_prefix_tokens must be non-negative")
    if total_prompt_tokens <= 0:
        raise ValueError("total_prompt_tokens must be positive")
    if cached_prefix_tokens > total_prompt_tokens:
        raise ValueError("cached_prefix_tokens must not exceed total_prompt_tokens")
    return cached_prefix_tokens / total_prompt_tokens
