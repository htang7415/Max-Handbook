# Multimodal LLMs

Modern LLMs often consume more than text, but the core systems question is still how those inputs fit into one sequence budget.

## Purpose

Use this page to understand:
- how text, image, audio, and video inputs enter one model
- why modality tokens compete for the same context budget
- what the simplest multimodal fusion picture looks like

## First Principles

- Each modality is usually converted into token-like embeddings before the shared transformer stack.
- Modalities share the same context window, so one modality can crowd out another.
- The simplest fused input is one ordered sequence made from multiple modality segments.
- Multimodal quality depends on both representation quality and prompt budgeting.

## Core Math

- Total multimodal token budget:
  $$
  T_{\text{text}} + T_{\text{image}} + T_{\text{audio}} + T_{\text{video}}
  $$
- Context fit condition:
  $$
  T_{\text{total}} \le W
  $$
  where `W` is the context window.

## Minimal Code Mental Model

```python
total = multimodal_token_budget(text_tokens=1200, image_tokens=576, audio_tokens=800)
fits = fits_context_window(total_tokens=total, context_window=8192)
offsets = modality_offsets([1200, 576, 800])
```

## Canonical Modules

- Main multimodal mental model: `multimodal-llms`
- Shared token front end: `token-representation-methods`
- Vision background when image features are unclear: `docs/ml/computer-vision`

## When To Use What

- Start with `multimodal-llms` when the core question is how multiple modalities fit into one model input.
- Use `token-representation-methods` when tokenization, embeddings, or positional structure are still unclear.
- Use the computer-vision section only when you need extra image-specific intuition beyond the multimodal LLM flow.
