# ML Coverage Roadmap

Goal: make the ML track feel complete against a broad problem-bank style curriculum without mirroring hundreds of narrow one-off problems.
This roadmap is driven by the live Deep-ML title list captured in `artifacts/deepml/problem_titles.md`.

## First Principle

- Fill docs gaps before adding lots of new modules.
- Add new modules only for canonical concepts not already represented.
- Prefer one module that teaches a family over several tiny variants.

## Added in This Pass

Docs added:

- `docs/ml/README.md`
- `docs/ml/fundamentals/prob/README.md`
- `docs/ml/fundamentals/stats/README.md`
- `docs/ml/data/preprocessing/README.md`
- `docs/ml/models/linear/README.md`
- `docs/ml/models/trees/README.md`
- `docs/ml/evaluation/calibration/README.md`
- `docs/ml/llm/evaluation/README.md`
- `docs/ml/llm/inference-serving/README.md`
- `docs/ml/systems/gpu/README.md`
- `docs/ml/systems/distributed/README.md`

Modules added:

- `modules/ml/evaluation/expected-calibration-error`
- `modules/ml/data/imputation`
- `modules/ml/models/gaussian-mixture-model-em`
- `modules/ml/llm/perplexity`
- `modules/ml/llm/kv-cache`
- `modules/ml/systems/roofline-analysis`
- `modules/ml/data/smote`
- `modules/ml/models/gradient-boosting`
- `modules/ml/llm/speculative-decoding`
- `modules/ml/llm/prefix-cache`
- `modules/ml/systems/continuous-batching`
- `modules/ml/models/isolation-forest`
- `modules/ml/models/kernel-pca`
- `modules/ml/models/xgboost-objective`
- `modules/ml/llm/mmlu-evaluation`
- `modules/ml/llm/pass-at-k`
- `modules/ml/systems/context-parallelism`
- `modules/ml/systems/tensor-parallelism`
- `modules/ml/systems/prefix-cache-metrics`
- `modules/ml/generative/ddpm-sampling`
- `modules/ml/data/outlier-detection`
- `modules/ml/systems/expert-parallelism`
- `modules/ml/systems/chunked-prefill`
- `modules/ml/evaluation/confidence-intervals`
- `modules/ml/llm/exact-match`
- `modules/ml/llm/judge-pairwise`
- `modules/ml/models/lle`
- `modules/ml/models/tsne-gradient`
- `modules/ml/models/bic-aic`
- `modules/ml/llm/bleu-meteor`
- `modules/ml/generative/ddim-sampling`
- `modules/ml/data/tf-idf`
- `modules/ml/llm/bm25-ranking`
- `modules/ml/reinforcement-learning/monte-carlo-tree-search`
- `modules/ml/reinforcement-learning/first-visit-monte-carlo-prediction`
- `modules/ml/reinforcement-learning/n-step-td-prediction`
- `modules/ml/data/feature-scaling`
- `modules/ml/llm/beam-search`
- `modules/ml/llm/top-p-sampling`
- `modules/ml/llm/temperature-sampling`
- `modules/ml/reinforcement-learning/eligibility-traces`
- `modules/ml/evaluation/bootstrap-intervals`
- `modules/ml/optimization/warmup-cosine-decay`
- `modules/ml/llm/tokenizer-comparison`
- `modules/ml/reinforcement-learning/importance-sampling`
- `modules/ml/llm/top-k-sampling`
- `modules/ml/evaluation/permutation-test`
- `modules/ml/evaluation/isotonic-calibration`
- `modules/ml/llm/reranker-metrics`
- `modules/ml/systems/expert-load-balancing`
- `modules/ml/data/missing-indicator`
- `modules/ml/evaluation/bradley-terry-ranking`
- `modules/ml/mlops/request-sla`
- `modules/ml/llm/sampling-pipeline`
- `modules/ml/data/robust-scaling`
- `modules/ml/llm/retrieval-fusion`
- `modules/ml/evaluation/wilson-interval`
- `modules/ml/reinforcement-learning/td-lambda`
- `modules/ml/evaluation/ab-test-analysis`
- `modules/ml/mlops/canary-rollout`
- `modules/ml/mlops/drift-detection`
- `modules/ml/evaluation/delong-test`
- `modules/ml/data/hash-trick`
- `modules/ml/llm/reciprocal-rank-fusion`
- `modules/ml/reinforcement-learning/generalized-advantage-estimation`
- `modules/ml/evaluation/brier-score`
- `modules/ml/representation/pairwise-ranking-loss`
- `modules/ml/mlops/online-shadow-mode`
- `modules/ml/optimization/one-cycle-schedule`
- `modules/ml/data/target-encoding`
- `modules/ml/llm/retrieval-recall-at-k`
- `modules/ml/reinforcement-learning/off-policy-correction`
- `modules/ml/evaluation/mean-reciprocal-rank`
- `modules/ml/data/count-vectorizer`
- `modules/ml/llm/answer-verification`
- `modules/ml/reinforcement-learning/advantage-normalization`
- `modules/ml/mlops/sequential-testing`
- `modules/ml/reinforcement-learning/off-policy-evaluation`
- `modules/ml/data/frequency-encoding`
- `modules/ml/llm/reciprocal-rank-metric`
- `modules/ml/optimization/cosine-restarts`
- `modules/ml/mlops/error-budget`
- `modules/ml/evaluation/ndcg`
- `modules/ml/data/chi-square-feature-selection`
- `modules/ml/llm/self-consistency-voting`
- `modules/ml/reinforcement-learning/value-normalization`
- `modules/ml/mlops/backfill-replay`
- `modules/ml/evaluation/top-k-accuracy`
- `modules/ml/data/rare-category-grouping`
- `modules/ml/llm/retrieval-precision-at-k`
- `modules/ml/reinforcement-learning/double-q-learning`
- `modules/ml/mlops/cost-per-request`
- `modules/ml/evaluation/hamming-loss`
- `modules/ml/data/weight-of-evidence`
- `modules/ml/llm/judge-calibration`
- `modules/ml/reinforcement-learning/target-network-update`
- `modules/ml/mlops/capacity-headroom`
- `modules/ml/evaluation/log-loss`
- `modules/ml/data/mean-encoding-smoothing`
- `modules/ml/llm/retrieval-f1-at-k`
- `modules/ml/reinforcement-learning/expected-sarsa`
- `modules/ml/mlops/tail-latency-budget`
- `modules/ml/evaluation/coverage-error`
- `modules/ml/data/category-cross-features`
- `modules/ml/llm/consensus-disagreement-rate`
- `modules/ml/reinforcement-learning/n-step-return`
- `modules/ml/mlops/queue-utilization`
- `modules/ml/evaluation/macro-f1`
- `modules/ml/data/entity-embedding-intuition`
- `modules/ml/llm/retrieval-hit-rate`
- `modules/ml/reinforcement-learning/td-error`
- `modules/ml/mlops/throughput-per-dollar`
- `modules/ml/evaluation/balanced-accuracy`
- `modules/ml/data/rare-token-pruning`
- `modules/ml/llm/rerank-gain`
- `modules/ml/reinforcement-learning/reward-clipping`
- `modules/ml/mlops/batch-fill-rate`
- `modules/ml/evaluation/micro-f1`
- `modules/ml/data/feature-bucketing`
- `modules/ml/llm/rerank-disagreement-rate`
- `modules/ml/reinforcement-learning/q-target`
- `modules/ml/mlops/admission-control`
- `modules/ml/evaluation/cohen-kappa`
- `modules/ml/data/frequency-capping`
- `modules/ml/llm/candidate-diversity`
- `modules/ml/reinforcement-learning/policy-entropy`
- `modules/ml/mlops/queue-delay`
- `modules/ml/evaluation/pr-auc`
- `modules/ml/data/token-budgeting`
- `modules/ml/llm/answer-stability`
- `modules/ml/reinforcement-learning/soft-update-gap`
- `modules/ml/mlops/retry-rate`
- `modules/ml/evaluation/agreement-rate`
- `modules/ml/data/feature-clipping`
- `modules/ml/llm/judge-agreement-matrix`
- `modules/ml/reinforcement-learning/entropy-bonus`
- `modules/ml/mlops/queue-age-percentiles`
- `modules/ml/evaluation/lift-at-k`
- `modules/ml/data/truncation-rate`
- `modules/ml/llm/majority-vote-margin`
- `modules/ml/reinforcement-learning/bootstrap-target`
- `modules/ml/mlops/saturation-rate`
- `modules/ml/evaluation/positive-rate`
- `modules/ml/data/overflow-count`
- `modules/ml/llm/vote-entropy`
- `modules/ml/reinforcement-learning/reward-scale`
- `modules/ml/mlops/queue-backlog-ratio`
- `modules/ml/evaluation/base-rate-gap`
- `modules/ml/data/budget-overrun-share`
- `modules/ml/llm/vote-concentration`
- `modules/ml/reinforcement-learning/terminal-mask`
- `modules/ml/mlops/depth-spike-rate`
- `modules/ml/evaluation/prevalence-ratio`
- `modules/ml/data/mean-overflow`
- `modules/ml/llm/top-vote-share`
- `modules/ml/reinforcement-learning/nonterminal-fraction`
- `modules/ml/mlops/capacity-breach-rate`
- `modules/ml/evaluation/prevalence-delta`
- `modules/ml/data/overflow-presence-rate`
- `modules/ml/llm/runner-up-vote-share`
- `modules/ml/reinforcement-learning/continuation-mask`
- `modules/ml/mlops/utilization-gap`
- `modules/ml/evaluation/risk-ratio`
- `modules/ml/data/overflow-tail`
- `modules/ml/llm/answer-uniqueness-rate`
- `modules/ml/reinforcement-learning/episode-end-rate`
- `modules/ml/mlops/overload-margin`
- `modules/ml/evaluation/prevalence-index`
- `modules/ml/data/overflow-quantile`
- `modules/ml/llm/answer-repeat-rate`
- `modules/ml/reinforcement-learning/terminal-share`
- `modules/ml/mlops/headroom-gap`
- `modules/ml/evaluation/base-rate-ratio`
- `modules/ml/data/overflow-peak`
- `modules/ml/llm/answer-mode-count`
- `modules/ml/reinforcement-learning/end-of-episode-mask`
- `modules/ml/mlops/overload-duration-share`
- `modules/ml/evaluation/prevalence-odds`
- `modules/ml/data/overflow-spread`
- `modules/ml/llm/answer-frequency-table`
- `modules/ml/reinforcement-learning/terminal-indicator`

## Top 10 Docs to Write Next

- `docs/ml/fundamentals/math/README.md`: connect Jacobian, Hessian, SVD, PCA, and optimization geometry in one place.
- `docs/ml/representation/embeddings/README.md`: connect cosine similarity, autoencoders, contrastive loss, and representation quality.
- `docs/ml/generative/diffusion/README.md`: organize DDPM, DDIM, guidance, and noise schedules.
- `docs/ml/optimization/schedules/README.md`: unify warmup, cosine decay, step decay, and restart intuition.
- `docs/ml/mlops/monitoring/README.md`: connect latency, drift, health metrics, and production alerting.
- `docs/ml/mlops/serving/README.md`: connect canaries, batching, SLAs, and online inference operations.
- `docs/ml/llm/tokenization/README.md`: connect character tokenization, BPE, and tokenizer-dependent evaluation.
- `docs/ml/llm/alignment/README.md`: connect SFT, RLHF, DPO, KL penalties, and PTX anchoring.
- `docs/ml/evaluation/uncertainty/README.md`: cover predictive uncertainty, confidence, and when probability estimates are actionable.
- `docs/ml/reinforcement-learning/rl-for-llm/README.md`: connect reward modeling, PPO-style alignment, and GRPO/GSPO ideas.

## Next Modules to Add

`modules/ml/generative/diffusion-guidance-tradeoffs` already covers the classifier-free guidance idea, so it is no longer tracked as a separate module.
`modules/ml/mlops/ab-testing`, `modules/ml/mlops/canary-deployment`, `modules/ml/mlops/feature-drift-psi`, and `modules/ml/representation/contrastive-loss` already cover the basic title areas, so exact-title follow-ups are lower priority than uncovered concepts.

- `modules/ml/mlops/pressure-score`: simple combined overload severity proxy.
- `modules/ml/evaluation/log-prevalence-ratio`: log transform of multiplicative prevalence comparison.
- `modules/ml/data/overflow-density`: overflow normalized by batch size and cap.
- `modules/ml/llm/vote-frequency-gap`: count gap between the top two normalized answers.
- `modules/ml/reinforcement-learning/not-done-mask`: scalar or vector mask for continuing transitions.
- `modules/ml/mlops/breach-severity-index`: combined breach incidence and margin score.

## Second Wave After That

- `modules/ml/evaluation/log-odds`
- `modules/ml/data/overflow-gini`
- `modules/ml/llm/vote-imbalance`
- `modules/ml/reinforcement-learning/done-fraction`
- `modules/ml/mlops/surge-pressure`
