# NLP and LLMs

Transformers, training stages, and alignment for LLMs.
Each bullet maps to a module under `modules/ml/llm/`.

## Core Concepts

- Tokenization (`modules/ml/llm/tokenization`)
- Tokenizer comparison (`modules/ml/llm/tokenizer-comparison`)
- Embeddings (`modules/ml/llm/embeddings`)
- Positional encoding (`modules/ml/llm/positional-encoding`)
- Transformer (`modules/ml/llm/transformer`)
- Self-attention (`modules/ml/llm/self-attention`)
- Multi-head attention (`modules/ml/llm/multi-head-attention`)
- Masked attention (`modules/ml/llm/attention-causal`)

## Training Stages

- Pretraining (next-token prediction / PTX loss) (`modules/ml/llm/pretraining`)
- Supervised fine-tuning (SFT) (`modules/ml/llm/supervised-fine-tuning`)
- Alignment / preference learning (`modules/ml/llm/preference-learning`)

## Evaluation

- Perplexity (`modules/ml/llm/perplexity`)
- MMLU-style evaluation (`modules/ml/llm/mmlu-evaluation`)
- Normalized exact match (`modules/ml/llm/exact-match`)
- Answer verification (`modules/ml/llm/answer-verification`)
- Answer stability (`modules/ml/llm/answer-stability`)
- Majority vote margin (`modules/ml/llm/majority-vote-margin`)
- Vote entropy (`modules/ml/llm/vote-entropy`)
- Self-consistency voting (`modules/ml/llm/self-consistency-voting`)
- Candidate diversity (`modules/ml/llm/candidate-diversity`)
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

## Retrieval and Lexical Baselines

- BM25 ranking (`modules/ml/llm/bm25-ranking`)
- Weighted retrieval fusion (`modules/ml/llm/retrieval-fusion`)
- Reciprocal-rank fusion (`modules/ml/llm/reciprocal-rank-fusion`)

## Decoding

- Beam search (`modules/ml/llm/beam-search`)
- Top-k sampling (`modules/ml/llm/top-k-sampling`)
- Top-p sampling (`modules/ml/llm/top-p-sampling`)
- Temperature sampling (`modules/ml/llm/temperature-sampling`)
- Combined sampling pipeline (`modules/ml/llm/sampling-pipeline`)

## Alignment and Optimization

- RLHF (`modules/ml/llm/rlhf`)
- DPO (`modules/ml/llm/dpo`)
- KL regularization (`modules/ml/llm/kl-regularization`)
- PTX anchoring (`modules/ml/llm/ptx-anchoring`)

## Efficiency and Systems

- LoRA (`modules/ml/llm/lora`) / QLoRA (`modules/ml/llm/qlora`)
- KV cache sizing (`modules/ml/llm/kv-cache`)
- Prefix-cache reuse (`modules/ml/llm/prefix-cache`)
- Speculative decoding verification (`modules/ml/llm/speculative-decoding`)
- Inference head pruning (`modules/ml/llm/inference-head-pruning`)
- Sparse attention (`modules/ml/llm/sparse-attention`)
- Sparse MoE layers (top-k expert routing) (`modules/ml/llm/moe-routing`)
- FP16 / BF16 / FP8 (`modules/ml/llm/fp16-bf16-fp8`)
- INT8 / INT4 (`modules/ml/llm/int8-int4-quantization`)

See also:

- LLM evaluation guide (`docs/ml/llm/evaluation`)
- Inference serving guide (`docs/ml/llm/inference-serving`)
