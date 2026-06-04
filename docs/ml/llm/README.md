# NLP and LLMs

This section is about how modern language models represent text, train, decode, align, and serve.

## Purpose

Use this page as the engineer's map for LLM systems: interface, model core, adaptation, evaluation, serving, and safety.

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

| Layer | Engineer's Question | Core Knowledge |
| --- | --- | --- |
| Interface | What text enters and what contract must come out? | `token-representation-methods`, `rope-and-position-scaling`, structured outputs |
| Model core | How does the model move information across tokens? | `attention-mechanisms`, `transformer`, `grouped-query-and-multi-query-attention` |
| Training and adaptation | What changed the model behavior? | `pretraining`, `alignment-methods`, preference learning, `parameter-efficient-fine-tuning` |
| Reasoning and multimodal | When does extra compute or extra modality help? | `reasoning-and-test-time-compute`, `multimodal-llms`, verification and answer stability |
| Evaluation | What evidence says the system is better? | likelihood, task scoring, judges, retrieval metrics, slice checks, trace-aware checks |
| Decoding and retrieval | How is output shaped and grounded? | `decoding-methods`, `bm25-ranking`, `retrieval-fusion-methods`, `cross-encoder-vs-bi-encoder` |
| Serving | What limits latency, memory, throughput, and cost? | `long-context-and-caching`, `context-budgeting-and-truncation`, `precision-and-quantization`, `kv-cache`, `prefix-cache`, `speculative-decoding`, `flashattention-and-io-aware-attention`, `qk-clip` |

## Supporting Guides

| Guide | What To Learn | Engineering Output |
| --- | --- | --- |
| Tokenization | Tokens, subwords, vocabulary, and representation boundaries. | Stable input accounting and context budgeting. |
| Reasoning | Test-time compute, verification, answer stability, and reasoning evals. | Hard-task policy with cost and quality evidence. |
| Long context | Truncation, caching, positional limits, and long-context degradation. | Context policy that fails predictably. |
| Multimodal | Image, audio, video, and token-like cross-modal representations. | Input contract for mixed-modality tasks. |
| Alignment | SFT, preference learning, RLHF/RLAIF, DPO, and safety behavior. | Behavior-change record and policy eval set. |
| LLM evaluation | Likelihood, task metrics, judges, retrieval metrics, and workflow traces. | Release gate with baseline and regression cases. |
| Inference serving | Batching, KV cache, quantization, latency, throughput, and cost. | Capacity plan and rollback threshold. |

## Engineering Checklist

| Area | Check Before Shipping |
| --- | --- |
| Interface | Tokenizer, context budget, output schema, refusal boundary. |
| Quality | Task metric, judge rubric, retrieval metric, slices, regression set. |
| Context | Truncation rule, cache strategy, citation policy, degradation check. |
| Serving | Prefill latency, decode latency, KV-cache memory, batching, quantization, cost. |
| Safety | Alignment objective, policy test cases, red-team cases, rollback gate. |
| Iteration | Fixed baseline, eval report, release threshold, production monitoring signal. |

## Lab Signals

| Source | Handbook Lesson |
| --- | --- |
| OpenAI | Treat reasoning effort, structured output, and eval datasets as engineering controls. |
| Anthropic | Define evals early; keep transcripts, graders, and failure labels inspectable. |
| DeepMind | Pair generation with automated evaluators when optimizing code, algorithms, or system behavior. |
| Hugging Face | Ground the theory in implementation: generation APIs, KV cache choices, evaluation metrics, and TRL post-training. |

## References

- [OpenAI Reasoning Models](https://developers.openai.com/api/docs/guides/reasoning)
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [Anthropic Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Google DeepMind AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [Hugging Face KV Cache Strategies](https://huggingface.co/docs/transformers/en/kv_cache)
- [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/choosing_a_metric)
- [Hugging Face TRL](https://huggingface.co/docs/trl)
