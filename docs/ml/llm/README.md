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
- The rest of the page maps those equations to interfaces, evaluation, serving, and safety checks.

## Minimal Code Mental Model

```python
tokens = tokenizer(text)
hidden = transformer(tokens)
next_token = decode(hidden[-1], strategy="top_p")
```

## Engineering Stack

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

## Engineering Checklist

- Interface: tokenizer, context budget, output schema, and refusal boundary.
- Quality: task metric, judge rubric, retrieval metric, slices, and regression set.
- Context: truncation rule, cache strategy, citation policy, and long-context degradation check.
- Serving: prefill latency, decode latency, KV-cache memory, batching, quantization, and cost.
- Safety: alignment objective, policy test cases, red-team cases, and rollback gate.
- Iteration: fixed baseline, eval report, release threshold, and production monitoring signal.

## Lab Signals

- OpenAI: reason with explicit effort, return structured outputs, and evaluate with datasets and graders.
- Anthropic: write evals before prompt fixes become folklore; keep transcripts and failure labels inspectable.
- DeepMind: pair generation with automated evaluators when optimizing algorithms or system behavior.
- Hugging Face: keep implementation concrete through Transformers generation, KV cache choices, Evaluate metrics, and TRL post-training.

## References

- [OpenAI Reasoning Models](https://developers.openai.com/api/docs/guides/reasoning)
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [Anthropic Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Google DeepMind AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [Hugging Face KV Cache Strategies](https://huggingface.co/docs/transformers/en/kv_cache)
- [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/choosing_a_metric)
- [Hugging Face TRL](https://huggingface.co/docs/trl)
