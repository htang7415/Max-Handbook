# LLM Evaluation

LLM evaluation mixes language-model likelihood, task scoring, and model-judge style comparisons.

## Current Anchors

- Perplexity (`modules/ml/llm/perplexity`)
- MMLU-style evaluation (`modules/ml/llm/mmlu-evaluation`)
- Normalized exact match (`modules/ml/llm/exact-match`)
- Answer verification (`modules/ml/llm/answer-verification`)
- Self-consistency voting (`modules/ml/llm/self-consistency-voting`)
- BLEU / METEOR overlap (`modules/ml/llm/bleu-meteor`)
- Pass@k (`modules/ml/llm/pass-at-k`)
- Retrieval Recall@k (`modules/ml/llm/retrieval-recall-at-k`)
- Mean reciprocal rank (`modules/ml/evaluation/mean-reciprocal-rank`)
- NDCG (`modules/ml/evaluation/ndcg`)
- Reciprocal rank for one query (`modules/ml/llm/reciprocal-rank-metric`)
- Pairwise judge rates (`modules/ml/llm/judge-pairwise`)
- Reranker metrics (`modules/ml/llm/reranker-metrics`)
- Bradley-Terry pairwise probability (`modules/ml/evaluation/bradley-terry-ranking`)

## Concepts to Cover Well

- Perplexity and token-level likelihood
- Exact match and normalized string matching
- Answer verification with multiple acceptable references
- Self-consistency voting across multiple sampled traces
- BLEU / METEOR style overlap metrics
- Pass@k for code and reasoning tasks
- Benchmark-style scoring such as MMLU variants
- Judge-based and pairwise preference evaluation
- Bradley-Terry style pairwise ranking models
- Retrieval and reranker metrics such as MRR and Recall@k
- Graded ranking metrics such as NDCG
- Query-level reciprocal rank before averaging into MRR
