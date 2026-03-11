# Multimodal LLMs

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand how modern LLMs handle text, images, audio, and
video inside one shared context.

## First Principles

- Multimodal models still operate on token-like sequences after modality encoders do their work.
- Different modalities compete for the same context budget.
- A multimodal stack must keep track of where each modality sits inside the fused sequence.
- The simplest fusion pattern is to concatenate modality embeddings into one ordered stream.

## Core Math

Total multimodal token budget:

$$
T_{\text{total}} = T_{\text{text}} + T_{\text{image}} + T_{\text{audio}} + T_{\text{video}}
$$

Context fit condition:

$$
T_{\text{total}} \le W
$$

Concatenated sequence:

$$
X = [X_{\text{text}}; X_{\text{image}}; X_{\text{audio}}; X_{\text{video}}]
$$

- $T_{\text{text}}, T_{\text{image}}, T_{\text{audio}}, T_{\text{video}}$ -- token counts contributed by each modality
- $W$ -- context window
- $X$ -- fused embedding sequence after modality-specific encoders

## From Math To Code

- Count each modality's token contribution first.
- Check whether the combined sequence fits inside the context window.
- Compute offsets so you know where each modality segment begins and ends.
- Concatenate modality embeddings only after their hidden dimensions agree.

## Minimal Code Mental Model

```python
total = multimodal_token_budget(text_tokens=1200, image_tokens=576, audio_tokens=800)
fits = fits_context_window(total_tokens=total, context_window=8192)
offsets = modality_offsets([1200, 576, 800])
sequence = concatenate_modal_embeddings([text_embeddings, image_embeddings, audio_embeddings])
```

## Functions

```python
def multimodal_token_budget(
    text_tokens: int,
    image_tokens: int = 0,
    audio_tokens: int = 0,
    video_tokens: int = 0,
) -> int:
def fits_context_window(total_tokens: int, context_window: int) -> bool:
def modality_offsets(lengths: list[int]) -> list[tuple[int, int]]:
def concatenate_modal_embeddings(modalities: list[list[list[float]]]) -> list[list[float]]:
```

## When To Use What

- Use `multimodal_token_budget` when prompt size is the first system constraint.
- Use `fits_context_window` before choosing a model or pre-processing strategy.
- Use `modality_offsets` when debugging modality packing or attention masks.
- Use `concatenate_modal_embeddings` to understand the simplest fused multimodal sequence.

## Run tests

```bash
pytest modules/ml/llm/multimodal-llms/python -q
```
