# LLM Evaluation

LLM evaluation asks five different questions:
- does the model assign high probability to text?
- does it produce a correct answer?
- does it stay consistent across samples?
- does a judge or preference signal prefer it?
- does retrieval surface the right context?

## Purpose

Use this page to understand the main evaluation modes for modern LLM systems without getting lost in every metric variant.

## First Principles

- `Likelihood` asks whether the model predicts tokens well. This is where perplexity fits.
- `Task scoring` asks whether the final answer is correct against references. This is where exact match, answer verification, BLEU/METEOR, pass@k, and MMLU-style scoring fit.
- `Reasoning quality` asks whether extra inference compute actually buys better answers per unit cost.
- `Consensus` asks whether repeated samples agree. This is where self-consistency and vote metrics fit.
- `Judge and preference evaluation` asks which answer is better when exact references are weak. This is where judge evaluation methods and Bradley-Terry style models fit.
- `Multimodal evaluation` asks whether the answer is correct and whether the required modalities were actually present or used.
- `Retrieval and reranking` ask whether the system surfaces relevant documents early enough. This is where Recall@k, MRR, and NDCG fit.
- `Agent and workflow evaluation` asks whether model calls, tool calls, guardrails, and handoffs succeeded as a trace, not only as a final answer.

## Frontier Lab Lessons

- OpenAI's eval platform guidance emphasizes datasets, criteria-level results, external-model comparisons, usage accounting, and dashboard reports; product LLM evals should preserve both quality and cost evidence.
- OpenAI and Anthropic both treat trace or transcript grading as necessary once model calls are embedded in tools, memory, or handoffs.
- DeepMind's frontier-safety approach treats capability evals as early-warning systems, so high-capability LLM evals should include risk-triggering cases, not only benchmark averages.

## Core Math

- Perplexity:
  $$
  \mathrm{PPL} = \exp\left(-\frac{1}{N}\sum_{t=1}^{N}\log p(x_t \mid x_{<t})\right)
  $$
- Exact match:
  $$
  \mathrm{EM} = \mathbf{1}[\mathrm{normalize}(\hat{y}) = \mathrm{normalize}(y)]
  $$
- Pass@k:
  $$
  \mathrm{Pass@k} = 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}
  $$
  where `n` is the number of samples and `c` is the number of correct samples.
- Reciprocal rank:
  $$
  \mathrm{RR} = \frac{1}{\mathrm{rank\ of\ first\ relevant\ item}}
  $$
- Bradley-Terry pairwise preference:
  $$
  P(i \succ j) = \frac{e^{s_i}}{e^{s_i} + e^{s_j}}
  $$

## Minimal Code Mental Model

```python
score = exact_match(normalize(prediction), normalize(reference))
votes = count_normalized_answers(sample_many(model, prompt, k=8))
retrieval = reciprocal_rank(ranked_docs, relevant_doc_ids)
preference = judge_pairwise(answer_a, answer_b)
trace_score = grade_trace(model_calls, tool_calls, guardrail_events)
```

## Canonical Modules

- Likelihood: `perplexity`
- Task scoring: `exact-match`, `answer-verification`, `pass-at-k`, `mmlu-evaluation`, `bleu-meteor`
- Reasoning quality: `reasoning-evaluation`
- Consensus and sampling: `vote-metrics`
- Judge and preference: `judge-evaluation-methods`, `bradley-terry-ranking`
- Multimodal evaluation: `multimodal-evaluation`
- Retrieval and reranking: `retrieval-metrics`, `reranker-metrics`

## Supporting Guides

- Vote and minority-cluster guide (`docs/ml/llm/vote-metrics`)

## References

- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI Agent Evals](https://developers.openai.com/api/docs/guides/agent-evals)
- [Anthropic Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Google DeepMind Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)

## When To Use What

- Use `perplexity` for pretraining-style language modeling comparisons, not as a full product metric.
- Use `exact-match` or `answer-verification` when references are strong and deterministic.
- Use `pass@k` when multiple attempts matter, especially for code and reasoning tasks.
- Use `reasoning-evaluation` when token cost and answer quality need to be compared together.
- Use `vote-metrics` and the vote guide when you are sampling multiple traces.
- Use judge-based methods when references are weak or style matters.
- Use `multimodal-evaluation` when image, audio, or video inputs are part of the task definition.
- Use retrieval metrics when answer quality depends on document ranking.
- Switch to `docs/ai-agents/evaluation` when the unit being graded is an end-to-end workflow trace with tools, memory, handoffs, or guardrails.
