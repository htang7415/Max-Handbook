# LLM Evaluation

LLM evaluation mixes language-model likelihood, task scoring, and model-judge style comparisons.

## Current Anchors

- Perplexity (`modules/ml/llm/perplexity`)
- MMLU-style evaluation (`modules/ml/llm/mmlu-evaluation`)
- Normalized exact match (`modules/ml/llm/exact-match`)
- Answer verification (`modules/ml/llm/answer-verification`)
- Self-consistency voting (`modules/ml/llm/self-consistency-voting`)
- Judge calibration (`modules/ml/llm/judge-calibration`)
- Consensus disagreement rate (`modules/ml/llm/consensus-disagreement-rate`)
- BLEU / METEOR overlap (`modules/ml/llm/bleu-meteor`)
- Pass@k (`modules/ml/llm/pass-at-k`)
- Retrieval Recall@k (`modules/ml/llm/retrieval-recall-at-k`)
- Retrieval Precision@k (`modules/ml/llm/retrieval-precision-at-k`)
- Retrieval F1@k (`modules/ml/llm/retrieval-f1-at-k`)
- Retrieval HitRate@k (`modules/ml/llm/retrieval-hit-rate`)
- Rerank gain (`modules/ml/llm/rerank-gain`)
- Rerank disagreement rate (`modules/ml/llm/rerank-disagreement-rate`)
- Mean reciprocal rank (`modules/ml/evaluation/mean-reciprocal-rank`)
- NDCG (`modules/ml/evaluation/ndcg`)
- Reciprocal rank for one query (`modules/ml/llm/reciprocal-rank-metric`)
- Pairwise judge rates (`modules/ml/llm/judge-pairwise`)
- Judge agreement matrix (`modules/ml/llm/judge-agreement-matrix`)
- Reranker metrics (`modules/ml/llm/reranker-metrics`)
- Bradley-Terry pairwise probability (`modules/ml/evaluation/bradley-terry-ranking`)

## Concepts to Cover Well

- Perplexity and token-level likelihood
- Exact match and normalized string matching
- Answer verification with multiple acceptable references
- Answer stability across repeated decoding runs
- Majority-vote margin between the top two normalized answers
- Vote entropy over normalized answer counts
- Vote concentration of the most common normalized answer
- Top vote share for the most common normalized answer
- Runner-up vote share for the second-most common normalized answer
- Answer uniqueness rate across normalized sampled answers
- Answer repeat rate as the complement of uniqueness
- Answer mode count for the largest normalized vote block
- Answer frequency tables for direct vote inspection
- Self-consistency voting across multiple sampled traces
- Candidate diversity across multiple sampled candidates
- Judge confidence aligned with correctness
- Consensus spread across sampled answers
- BLEU / METEOR style overlap metrics
- Pass@k for code and reasoning tasks
- Benchmark-style scoring such as MMLU variants
- Judge-based and pairwise preference evaluation
- Judge agreement tables before chance-corrected agreement metrics
- Bradley-Terry style pairwise ranking models
- Retrieval and reranker metrics such as MRR and Recall@k
- Retrieval precision when early purity matters more than coverage
- Retrieval F1 when precision and recall must be balanced
- Retrieval hit rate when any successful retrieval is enough
- Rerank gain relative to a baseline ranking
- Rerank disagreement as an ordering-change summary
- Graded ranking metrics such as NDCG
- Query-level reciprocal rank before averaging into MRR
