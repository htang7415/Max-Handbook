from __future__ import annotations


def multimodal_token_budget(
    text_tokens: int,
    image_tokens: int = 0,
    audio_tokens: int = 0,
    video_tokens: int = 0,
) -> int:
    values = [text_tokens, image_tokens, audio_tokens, video_tokens]
    if any(value < 0 for value in values):
        raise ValueError("token counts must be non-negative")
    return sum(values)


def fits_context_window(total_tokens: int, context_window: int) -> bool:
    if total_tokens < 0:
        raise ValueError("total_tokens must be non-negative")
    if context_window <= 0:
        raise ValueError("context_window must be positive")
    return total_tokens <= context_window


def modality_offsets(lengths: list[int]) -> list[tuple[int, int]]:
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    offsets: list[tuple[int, int]] = []
    start = 0
    for length in lengths:
        end = start + length
        offsets.append((start, end))
        start = end
    return offsets


def concatenate_modal_embeddings(modalities: list[list[list[float]]]) -> list[list[float]]:
    flattened: list[list[float]] = []
    target_dim: int | None = None

    for modality in modalities:
        for embedding in modality:
            if target_dim is None:
                target_dim = len(embedding)
            elif len(embedding) != target_dim:
                raise ValueError("all embeddings must share the same hidden dimension")
            flattened.append(list(embedding))

    return flattened
