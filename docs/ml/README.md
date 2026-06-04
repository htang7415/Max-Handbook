# Machine Learning

Use this track to learn the ML stack from first principles without getting buried in low-value variants.

## Purpose

This track is optimized for:
- clear mental models
- enough math to understand why a method works
- enough code to make the idea concrete
- the topics that matter most for AI work in 2026

## First Principles

- Learn ML in this order: concept, math, then code.
- Prefer canonical family modules over narrow variants or old aliases.
- Use docs pages as routing maps and modules as executable learning units.
- Treat classical ML, deep learning, LLMs, and systems as one connected stack rather than separate silos.

## Frontier Lab Lessons

- OpenAI's deliberative alignment work shows that safety behavior can improve when models learn interpretable specifications and how to reason over them, not only outcome labels.
- Anthropic's interpretability work shows that model understanding is becoming an engineering discipline, but features are not enough; circuits, usage, and safety interventions still need evidence.
- DeepMind's AlphaEvolve shows that LLMs can become optimization systems when paired with automated evaluators and iterative search over code or algorithms.
- DeepMind's frontier-safety work turns capability evaluation into a release discipline; ML handbook topics should connect model capability, eval coverage, and deployment risk.

## How To Use This Track

- Start with one section, not the whole tree.
- Use section docs for the concept map.
- Use canonical modules for the main learning unit.
- Use alias or narrow modules only after the canonical family is clear.
- Treat `artifacts/deepml/problem_titles.md` as the main scope boundary.

## Math And Code

- Learn each ML topic in this order: intuition, equation, then code.
- Use the equation to understand the quantity being optimized or measured.
- Use the code to see the smallest executable version of that equation.
- If a topic turns into a long catalog of variants, go back to the canonical family first.

```python
# The default ML learning loop in this repo:
concept = understand_problem()
equation = write_core_formula(concept)
code = implement_smallest_working_version(equation)
```

## Start Here

- If your goal is interview prep, use `docs/ml/path-interview`.
- Otherwise, start with `docs/ml/fundamentals`, then move to `docs/ml/data` and `docs/ml/models`.
- For modern AI systems, continue into `docs/ml/evaluation`, `docs/ml/llm`, and `docs/ml/systems` before treating deployment as finished.

## Handbook Subsections

1. Fundamentals: math, probability, statistics, and learning paths.
2. Data and representation: preprocessing, features, embeddings, and metric learning.
3. Classical models: linear models, trees, Bayes, kernels, clusters, and ensembles.
4. Evaluation and calibration: metrics, uncertainty, ranking, judges, and confidence.
5. Optimization and training: loss surfaces, optimizers, schedules, stability, and clipping.
6. Deep learning: activations, normalization, initialization, losses, and regularization.
7. LLMs: tokenization, attention, training, retrieval, reasoning, alignment, and serving.
8. Generative and vision: diffusion, VAE/GAN concepts, CNNs, pooling, and architectures.
9. Systems and MLOps: training loops, hardware bottlenecks, serving, monitoring, rollout, and capstone release gates.
10. Reinforcement learning: MDPs, value methods, policy gradients, off-policy ideas, and RL for LLMs.

## Canonical Families

- Deep learning: `activation-functions`, `normalization-methods`
- Evaluation: `classification-metrics-core`, `ranking-metrics`, `calibration-metrics`, `uncertainty-intervals`, `agreement-metrics`, `binary-rate-comparison-metrics`
- Data: `scaling-methods`, `categorical-encoding-methods`, `sparse-text-feature-methods`, `structured-feature-methods`, `overflow-metrics`
- LLM: `reasoning-and-test-time-compute`, `long-context-and-caching`, `multimodal-llms`, `decoding-methods`, `retrieval-metrics`, `vote-metrics`
- Production and RL helpers: `capacity-stress-metrics`, `transition-indicators`

## When To Use What

- Use the top-level section docs when you need the next concept family, not the final detail.
- Use canonical family modules before narrow variants or preserved alias pages.
- Follow the subsection order until you know what kind of failure you are debugging: data, model, metric, training, serving, or policy.
- Add systems and MLOps after you can already choose models, metrics, and core deep-learning tools.
- Use LLM evaluation, retrieval, long-context, and inference modules when product behavior depends on prompts, tools, or serving constraints rather than only model weights.
- Use assessments and capstones to check whether model quality, calibration, latency, cost, and rollout rules work together.
- Treat reinforcement learning, generative models, representation learning, and computer vision as specializations after the main spine is comfortable.

## Scope Rule

- Prefer concise explanations over exhaustive catalogs.
- Prefer canonical families over many near-duplicate modules.
- Only add ML topics outside `problem_titles.md` when they are clearly important to AI practice in 2026.

## Neighbor Tracks

- Use `docs/ai-agents/evaluation` when model behavior is embedded in a tool-using workflow.
- Use `docs/databases/vector-db/overview.md` when retrieval, metadata, or freshness affects LLM output quality.
- Use `docs/software-engineering/performance` and `docs/software-engineering/reliability` when serving budgets or rollback rules decide deployment.

## References

- [OpenAI Deliberative Alignment](https://openai.com/index/deliberative-alignment/)
- [Anthropic Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Google DeepMind AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [Google DeepMind Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)
