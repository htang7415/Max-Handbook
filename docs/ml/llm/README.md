# NLP and LLMs

This section is about how modern language models represent text, train, decode, align, and serve.

## Purpose

Use this page to keep the LLM stack in the right order:
- tokenization and representations
- attention and transformer structure
- training stages
- evaluation
- decoding and inference systems

## First Principles

- Tokenization defines the units the model sees.
- Attention lets each token condition on earlier context.
- The transformer stacks attention and feed-forward blocks into a scalable sequence model.
- Training moves from pretraining to task adaptation and then often to alignment.
- Good LLM systems are not just good models; they also need good decoding and serving behavior.

## Core Math

- The whole LLM stack mostly rests on three equations:
  $$
  \mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V,
  \quad
  -\sum_t \log p(x_t \mid x_{<t}),
  \quad
  \text{preference objective}
  $$
- The details live in the section guides and canonical modules below.

## Minimal Code Mental Model

```python
tokens = tokenizer(text)
hidden = transformer(tokens)
next_token = decode(hidden[-1], strategy="top_p")
```

## Canonical Modules

- Tokenization and representations: `tokenization`, `tokenizer-comparison`, `embeddings`, `positional-encoding`
- Transformer core: `self-attention`, `multi-head-attention`, `attention-causal`, `transformer`
- Training stages: `pretraining`, `supervised-fine-tuning`, `preference-learning`
- Evaluation: `docs/ml/llm/evaluation`
- Decoding: `decoding-methods`
- Retrieval and lexical baselines: `bm25-ranking`, `retrieval-fusion`, `reciprocal-rank-fusion`
- Alignment and optimization: `rlhf`, `dpo`, `kl-regularization`, `ptx-anchoring`
- Efficiency and systems: `lora`, `qlora`, `kv-cache`, `prefix-cache`, `speculative-decoding`, `qk-clip`

## Supporting Guides

- Tokenization guide (`docs/ml/llm/tokenization`)
- Alignment guide (`docs/ml/llm/alignment`)
- LLM evaluation guide (`docs/ml/llm/evaluation`)
- Inference serving guide (`docs/ml/llm/inference-serving`)

## When To Use What

- Start with tokenization, embeddings, and attention before jumping to alignment or serving.
- Use the evaluation guide before choosing metrics module by module.
- Use decoding methods when generation behavior is the issue.
- Use serving and systems topics when latency, memory, or throughput becomes the bottleneck.
- Treat this page as the stack overview; use the leaf guides for the real detail.
