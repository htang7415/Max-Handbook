"""long_context_vs_retrieval_tradeoffs - compare token load and fit for long context versus retrieval."""

from __future__ import annotations


def validate_inputs(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> None:
    if source_tokens < 0:
        raise ValueError("source_tokens must be non-negative")
    if relevant_tokens < 0:
        raise ValueError("relevant_tokens must be non-negative")
    if relevant_tokens > source_tokens:
        raise ValueError("relevant_tokens cannot exceed source_tokens")
    if model_window <= 0:
        raise ValueError("model_window must be positive")
    if top_k < 0:
        raise ValueError("top_k must be non-negative")
    if avg_chunk_tokens < 0:
        raise ValueError("avg_chunk_tokens must be non-negative")
    if prompt_overhead < 0:
        raise ValueError("prompt_overhead must be non-negative")


def long_context_token_load(source_tokens: int, prompt_overhead: int = 0) -> int:
    if source_tokens < 0:
        raise ValueError("source_tokens must be non-negative")
    if prompt_overhead < 0:
        raise ValueError("prompt_overhead must be non-negative")
    return source_tokens + prompt_overhead


def retrieval_token_load(
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> int:
    if top_k < 0:
        raise ValueError("top_k must be non-negative")
    if avg_chunk_tokens < 0:
        raise ValueError("avg_chunk_tokens must be non-negative")
    if prompt_overhead < 0:
        raise ValueError("prompt_overhead must be non-negative")
    return top_k * avg_chunk_tokens + prompt_overhead


def fits_context_window(total_tokens: int, model_window: int) -> bool:
    if total_tokens < 0:
        raise ValueError("total_tokens must be non-negative")
    if model_window <= 0:
        raise ValueError("model_window must be positive")
    return total_tokens <= model_window


def choose_strategy(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> str:
    validate_inputs(
        source_tokens,
        relevant_tokens,
        model_window,
        top_k,
        avg_chunk_tokens,
        prompt_overhead,
    )
    long_load = long_context_token_load(source_tokens, prompt_overhead)
    retrieval_load = retrieval_token_load(top_k, avg_chunk_tokens, prompt_overhead)
    relevant_fraction = 0.0 if source_tokens == 0 else relevant_tokens / source_tokens
    long_fits = fits_context_window(long_load, model_window)
    retrieval_fits = fits_context_window(retrieval_load, model_window)

    if not long_fits and not retrieval_fits:
        return "reduce-context"
    if not long_fits:
        return "retrieval"
    if not retrieval_fits:
        return "long-context"
    if relevant_fraction >= 0.7:
        return "long-context"
    return "retrieval"


def strategy_summary(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> dict[str, int | float | str | bool]:
    validate_inputs(
        source_tokens,
        relevant_tokens,
        model_window,
        top_k,
        avg_chunk_tokens,
        prompt_overhead,
    )
    long_load = long_context_token_load(source_tokens, prompt_overhead)
    retrieval_load = retrieval_token_load(top_k, avg_chunk_tokens, prompt_overhead)
    return {
        "long_context_tokens": long_load,
        "retrieval_tokens": retrieval_load,
        "fits_long_context": fits_context_window(long_load, model_window),
        "fits_retrieval": fits_context_window(retrieval_load, model_window),
        "relevant_fraction": 0.0 if source_tokens == 0 else relevant_tokens / source_tokens,
        "choice": choose_strategy(
            source_tokens,
            relevant_tokens,
            model_window,
            top_k,
            avg_chunk_tokens,
            prompt_overhead,
        ),
    }
