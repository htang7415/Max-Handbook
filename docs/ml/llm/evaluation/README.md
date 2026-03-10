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
- `Consensus` asks whether repeated samples agree. This is where self-consistency and vote metrics fit.
- `Judge and preference evaluation` asks which answer is better when exact references are weak. This is where pairwise judges, judge calibration, and Bradley-Terry style models fit.
- `Retrieval and reranking` ask whether the system surfaces relevant documents early enough. This is where Recall@k, MRR, and NDCG fit.

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
```

## Canonical Modules

- Likelihood: `perplexity`
- Task scoring: `exact-match`, `answer-verification`, `pass-at-k`, `mmlu-evaluation`, `bleu-meteor`
- Consensus and sampling: `vote-metrics`
- Judge and preference: `judge-calibration`, `judge-pairwise`, `judge-agreement-matrix`, `bradley-terry-ranking`
- Retrieval and reranking: `retrieval-metrics`, `reranker-metrics`

## Supporting Guides

- Vote and minority-cluster guide (`docs/ml/llm/vote-metrics`)

## When To Use What

- Use `perplexity` for pretraining-style language modeling comparisons, not as a full product metric.
- Use `exact-match` or `answer-verification` when references are strong and deterministic.
- Use `pass@k` when multiple attempts matter, especially for code and reasoning tasks.
- Use `vote-metrics` and the vote guide when you are sampling multiple traces.
- Use judge-based methods when references are weak or style matters.
- Use retrieval metrics when answer quality depends on document ranking.
