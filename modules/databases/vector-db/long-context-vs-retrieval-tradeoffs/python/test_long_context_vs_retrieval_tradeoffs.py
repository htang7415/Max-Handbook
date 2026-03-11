from long_context_vs_retrieval_tradeoffs import (
    choose_strategy,
    fits_context_window,
    retrieval_token_load,
    strategy_summary,
)
import pytest


def test_large_source_with_small_relevant_slice_favors_retrieval():
    assert not fits_context_window(200_000, 128_000)
    assert choose_strategy(
        source_tokens=200_000,
        relevant_tokens=1_000,
        model_window=128_000,
        top_k=5,
        avg_chunk_tokens=200,
    ) == "retrieval"


def test_small_source_with_high_relevant_fraction_can_use_long_context():
    summary = strategy_summary(
        source_tokens=8_000,
        relevant_tokens=6_000,
        model_window=32_000,
        top_k=5,
        avg_chunk_tokens=300,
    )

    assert retrieval_token_load(5, 300) == 1_500
    assert summary["choice"] == "long-context"
    assert summary["fits_long_context"] is True
    assert summary["fits_retrieval"] is True


def test_neither_strategy_fitting_context_requires_reducing_tokens():
    assert (
        choose_strategy(
            source_tokens=300_000,
            relevant_tokens=40_000,
            model_window=8_000,
            top_k=20,
            avg_chunk_tokens=500,
        )
        == "reduce-context"
    )


def test_relevant_tokens_cannot_exceed_source_tokens():
    with pytest.raises(ValueError, match="relevant_tokens"):
        strategy_summary(
            source_tokens=1_000,
            relevant_tokens=1_200,
            model_window=8_000,
            top_k=5,
            avg_chunk_tokens=200,
        )
