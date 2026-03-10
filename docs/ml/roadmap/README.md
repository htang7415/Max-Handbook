# ML Coverage Roadmap

Goal: keep the ML track systematic, concise, and useful for 2026-era AI learning.
Scope is driven by `artifacts/deepml/problem_titles.md`, with additions outside that file only when they are clearly important for modern AI practice.

## Current Status

- Visible ML modules: `212`
- Hidden ML aliases: `311`
- Strategy: show canonical learning units first, keep old slugs only for compatibility

## Authoring Rules

- Prefer concise teaching-first docs over long inventories.
- Prefer one coherent family module over many narrow variants.
- Keep concept, math, and minimal code together.
- Avoid duplicate ML modules.
- Hide legacy narrow slugs as aliases instead of surfacing them in the main learning path.

## Canonical Learning Units

### Fundamentals

- Guides: `docs/ml/fundamentals/math`, `docs/ml/fundamentals/prob`, `docs/ml/fundamentals/stats`
- Core modules: `vectors-matrices`, `expectation`, `gradient-descent`, `pca`, `svd`, `kl-divergence`

### Data

- Guides: `docs/ml/data/preprocessing`, `docs/ml/data/overflow-metrics`
- Canonical families: `scaling-methods`, `categorical-encoding-methods`, `sparse-text-feature-methods`, `structured-feature-methods`, `overflow-metrics`
- Core standalone modules: `train-validation-test-split`, `stratified-split`, `imputation`, `smote`

### Classical Models

- Guides: `docs/ml/models/linear`, `docs/ml/models/trees`
- Canonical families: `linear-models`, `naive-bayes-models`
- Core modules: `gaussian-mixture-model-em`, `gradient-boosting`, `kernel-pca`, `isolation-forest`, `xgboost-objective`

### Deep Learning

- Guides: `docs/ml/deep-learning/training-techniques`
- Canonical families: `activation-functions`, `normalization-methods`, `loss-functions`, `regularization-methods`, `initialization-methods`
- Core standalone modules: `backpropagation`, `automatic-differentiation`, `cross-entropy`, `label-smoothing`, `knowledge-distillation-loss`

### Evaluation

- Guides: `docs/ml/evaluation/calibration`, `docs/ml/evaluation/uncertainty`
- Canonical families: `classification-metrics-core`, `ranking-metrics`, `calibration-metrics`, `uncertainty-intervals`, `agreement-metrics`, `binary-rate-comparison-metrics`, `regression-metrics`, `clustering-metrics`
- Core standalone modules: `permutation-test`, `ab-test-analysis`, `delong-test`

### LLM

- Guides: `docs/ml/llm/tokenization`, `docs/ml/llm/alignment`, `docs/ml/llm/evaluation`, `docs/ml/llm/inference-serving`, `docs/ml/llm/vote-metrics`
- Canonical families: `attention-mechanisms`, `alignment-methods`, `decoding-methods`, `retrieval-metrics`, `retrieval-fusion-methods`, `vote-metrics`, `parameter-efficient-fine-tuning`, `precision-and-quantization`
- Core standalone modules: `tokenization`, `tokenizer-comparison`, `embeddings`, `positional-encoding`, `transformer`, `pretraining`, `perplexity`, `exact-match`, `answer-verification`, `pass-at-k`, `mmlu-evaluation`, `bm25-ranking`, `kv-cache`, `speculative-decoding`, `qk-clip`

### Reinforcement Learning

- Guides: `docs/ml/reinforcement-learning/rl-for-llm`, `docs/ml/reinforcement-learning/transition-indicators`
- Canonical families: `bandit-exploration-methods`, `return-estimation-methods`, `td-control-methods`, `off-policy-estimation-methods`, `policy-gradient-methods`, `policy-optimization-utilities`, `transition-indicators`
- Core standalone modules: none

### Optimization

- Guides: `docs/ml/optimization/schedules`
- Canonical families: `optimizer-methods`, `learning-rate-schedules`
- Core standalone modules: `gradient-clipping`, `loss-scaling`, `detect-nans`, `muon-optimizer`

### Systems and MLOps

- Guides: `docs/ml/systems/gpu`, `docs/ml/systems/distributed`, `docs/ml/mlops/monitoring`, `docs/ml/mlops/serving`, `docs/ml/mlops/breach-buckets`
- Canonical families: `capacity-stress-metrics`
- Core standalone modules: `roofline-analysis`, `continuous-batching`, `chunked-prefill`, `tensor-parallelism`, `context-parallelism`, `expert-parallelism`, `request-sla`, `error-budget`, `cost-per-request`, `throughput-per-dollar`

### Generative and Representation

- Guides: `docs/ml/generative/diffusion`, `docs/ml/representation/embeddings`, `docs/ml/representation/metric-learning`, `docs/ml/computer-vision/architectures`
- Canonical families: `cnn-architectures`
- Core generative modules: `diffusion-models`, `ddpm-sampling`, `ddim-sampling`, `diffusion-guidance-tradeoffs`, `ema-diffusion-weights`, `model-selection`
- Core representation modules: `embeddings`, `contrastive-loss`, `triplet-loss`, `pairwise-ranking-loss`

## Supporting Content

Supporting content should stay visible when it teaches a distinct mental model, but it should not replace the canonical entry point.

- Specialized evaluation tasks: `bradley-terry-ranking`, `judge-calibration`, `judge-pairwise`, `judge-agreement-matrix`
- Rare-event log summaries: `log-rate-metrics`
- Specialized LLM systems topics: `prefix-cache`, `prefix-cache-metrics`
- Specialized RL topics: `monte-carlo-tree-search`
- Specialized generative comparisons: `gan-mode-collapse`, `vae-posterior-collapse`

## Legacy / Hidden

These should stay out of the main learning path and remain alias-only unless they become the best teaching unit again.

- Old activation and normalization variant slugs
- Old decoding variant slugs
- Old ranking, calibration, classification, uncertainty, and agreement metric slugs
- Old retrieval metric and reranker metric slugs
- Old scaling, categorical encoding, sparse text, structured feature, and overflow metric slugs
- Old vote, minority-cluster, and answer-fragmentation metric slugs
- Old breach-bucket and capacity-stress detail slugs
- Old transition-mask and transition-batch helper slugs

## Study Paths

- `docs/ml/path-beginner/README.md`
- `docs/ml/path-interview/README.md`
- `docs/ml/path-llm-systems/README.md`
- `docs/ml/path-math-first/README.md`

## Next Cleanup Priorities

- Keep refactoring section docs toward the concise first-principles format
- Deepen thin but high-value areas: `representation`, `generative`, `computer-vision`, `systems`
- Consolidate only when a merge creates a better learning unit, not just a smaller module count
- Keep checking new additions against `problem_titles.md` before adding more ML surface area
