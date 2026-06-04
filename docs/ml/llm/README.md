# NLP and LLMs

This section is about how modern language models represent text, train, decode, align, and serve.

## Purpose

Use this page to keep the LLM stack in the right order:
- tokenization and representations
- attention and transformer structure
- training stages
- reasoning and test-time compute
- multimodal inputs
- evaluation
- decoding and inference systems

## First Principles

- Tokenization defines the units the model sees.
- Attention lets each token condition on earlier context.
- The transformer stacks attention and feed-forward blocks into a scalable sequence model.
- Training moves from pretraining to task adaptation and then often to alignment.
- Reasoning models trade extra inference compute for better answers on harder tasks.
- Modern LLMs often consume images, audio, or video by turning them into token-like embeddings.
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

- Tokenization and representations: `token-representation-methods`, `rope-and-position-scaling`
- Transformer core: `attention-mechanisms`, `transformer`, `grouped-query-and-multi-query-attention`
- Training stages: `pretraining`, `alignment-methods`
- Reasoning: `reasoning-and-test-time-compute`
- Multimodal inputs: `multimodal-llms`
- Evaluation: likelihood, task scoring, judges, retrieval metrics, and trace-aware checks
- Decoding: `decoding-methods`
- Retrieval and lexical baselines: `bm25-ranking`, `retrieval-fusion-methods`, `cross-encoder-vs-bi-encoder`
- Efficiency and systems: `long-context-and-caching`, `context-budgeting-and-truncation`, `parameter-efficient-fine-tuning`, `precision-and-quantization`, `kv-cache`, `prefix-cache`, `speculative-decoding`, `flashattention-and-io-aware-attention`, `qk-clip`

## Supporting Guides

- Tokenization: tokens, subwords, vocabulary, and representation boundaries.
- Reasoning: test-time compute, verification, answer stability, and reasoning evals.
- Long context: context budgeting, truncation, caching, and positional limits.
- Multimodal: image, audio, video, and token-like cross-modal representations.
- Alignment: SFT, preference learning, RLHF/RLAIF, DPO, and safety behavior.
- LLM evaluation: likelihood, task metrics, judges, retrieval metrics, and workflow traces.
- Inference serving: batching, KV cache, quantization, latency, throughput, and cost.

## When To Use What

- Start with token-representation methods and attention before jumping to alignment or serving.
- Use `rope-and-position-scaling` when the long-context question is positional extrapolation rather than cache reuse.
- Use `reasoning-and-test-time-compute` before tuning sampling-heavy reasoning workflows.
- Use `multimodal-llms` when the system has to mix text with images, audio, or video.
- Use the evaluation guide before choosing metrics module by module.
- Use decoding methods when generation behavior is the issue.
- Use `cross-encoder-vs-bi-encoder` when choosing between first-stage dense retrieval and second-stage reranking.
- Use `grouped-query-and-multi-query-attention` when KV cache size or memory bandwidth is the main inference constraint.
- Use `flashattention-and-io-aware-attention` when the attention kernel itself is the serving or training bottleneck.
- Use serving and systems topics when latency, memory, or throughput becomes the bottleneck.
- If the model must call APIs, browse interfaces, or use MCP-style tool servers, switch to agent tool use.
- Treat this page as the stack overview; use the leaf guides for the real detail.
