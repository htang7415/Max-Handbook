from __future__ import annotations

import pytest

from multimodal_llms import (
    concatenate_modal_embeddings,
    fits_context_window,
    modality_offsets,
    multimodal_token_budget,
)


def test_multimodal_budget_and_offsets_capture_fused_sequence_shape() -> None:
    total = multimodal_token_budget(text_tokens=1200, image_tokens=576, audio_tokens=800)
    assert total == 2576
    assert fits_context_window(total_tokens=total, context_window=8192) is True
    assert modality_offsets([1200, 576, 800]) == [(0, 1200), (1200, 1776), (1776, 2576)]


def test_concatenate_modal_embeddings_flattens_modalities_in_order() -> None:
    text = [[1.0, 0.0], [0.5, 0.5]]
    image = [[2.0, 2.0]]
    audio = [[3.0, 1.0]]
    assert concatenate_modal_embeddings([text, image, audio]) == [
        [1.0, 0.0],
        [0.5, 0.5],
        [2.0, 2.0],
        [3.0, 1.0],
    ]


def test_multimodal_validation_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        multimodal_token_budget(text_tokens=-1)
    with pytest.raises(ValueError):
        fits_context_window(total_tokens=1, context_window=0)
    with pytest.raises(ValueError):
        modality_offsets([1, -1])
    with pytest.raises(ValueError):
        concatenate_modal_embeddings([[[1.0, 0.0]], [[1.0, 0.0, 0.0]]])
