from __future__ import annotations

import pytest

from long_context_and_caching import (
    cache_hit_rate,
    context_utilization,
    effective_prefix_tokens,
    prompt_cache_saved_tokens,
    quadratic_attention_pairs,
)


def test_long_context_helpers_capture_scaling_and_cache_reuse() -> None:
    assert quadratic_attention_pairs(1024) == 1024 * 1024
    assert context_utilization(64_000, 128_000) == pytest.approx(0.5)
    assert effective_prefix_tokens(64_000, 48_000) == 16_000
    assert prompt_cache_saved_tokens(48_000, 10) == 432_000
    assert cache_hit_rate(48_000, 64_000) == pytest.approx(0.75)


def test_validation_rejects_invalid_context_inputs() -> None:
    with pytest.raises(ValueError):
        quadratic_attention_pairs(0)
    with pytest.raises(ValueError):
        context_utilization(1, 0)
    with pytest.raises(ValueError):
        effective_prefix_tokens(10, 11)
    with pytest.raises(ValueError):
        prompt_cache_saved_tokens(100, 0)
    with pytest.raises(ValueError):
        cache_hit_rate(9, 8)
