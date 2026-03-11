from __future__ import annotations


def available_prompt_budget(context_window: int, reserved_output_tokens: int) -> int:
    if context_window <= 0:
        raise ValueError("context_window must be positive")
    if reserved_output_tokens < 0:
        raise ValueError("reserved_output_tokens must be non-negative")
    if reserved_output_tokens >= context_window:
        raise ValueError("reserved_output_tokens must be smaller than context_window")
    return context_window - reserved_output_tokens


def truncation_needed(total_prompt_tokens: int, prompt_budget: int) -> bool:
    if total_prompt_tokens < 0:
        raise ValueError("total_prompt_tokens must be non-negative")
    if prompt_budget <= 0:
        raise ValueError("prompt_budget must be positive")
    return total_prompt_tokens > prompt_budget


def tokens_to_drop(total_prompt_tokens: int, prompt_budget: int) -> int:
    if total_prompt_tokens < 0:
        raise ValueError("total_prompt_tokens must be non-negative")
    if prompt_budget <= 0:
        raise ValueError("prompt_budget must be positive")
    return max(0, total_prompt_tokens - prompt_budget)


def head_tail_keep(total_prompt_tokens: int, prompt_budget: int, head_tokens: int) -> tuple[int, int]:
    if total_prompt_tokens < 0:
        raise ValueError("total_prompt_tokens must be non-negative")
    if prompt_budget <= 0:
        raise ValueError("prompt_budget must be positive")
    if head_tokens < 0:
        raise ValueError("head_tokens must be non-negative")
    if head_tokens > total_prompt_tokens:
        raise ValueError("head_tokens must not exceed total_prompt_tokens")

    kept_total = min(total_prompt_tokens, prompt_budget)
    kept_head = min(head_tokens, kept_total)
    kept_tail = kept_total - kept_head
    return kept_head, kept_tail
