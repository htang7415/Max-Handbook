# Evaluation

This section is about how to measure whether an agent succeeds, whether its tool calls work, and where failures happen.

## Purpose

Use this page to understand:
- task success
- tool-call success
- trace-level behavior
- repeatable datasets and baseline gates
- latency and cost baselines
- failure category counts

## First Principles

- Agent evaluation should measure both final outcomes and the steps that produced them.
- Start with traces when behavior is still unclear, then turn repeated cases into datasets.
- Simple metrics are usually enough to find the first bottleneck.
- A useful evaluation loop separates model failure, tool failure, and workflow failure.
- Benchmark harnesses should keep cases stable while prompts, tools, models, and policies change.

## Frontier Lab Lessons

- OpenAI's trace-grading guidance makes traces the first debugging surface, then moves to repeatable datasets and eval runs once "good" is defined.
- Anthropic's agent-eval guidance separates task, trial, grader, transcript, outcome, harness, and suite; this is a useful vocabulary for multi-turn agent testing.
- DeepMind's Frontier Safety Framework uses early-warning evaluations and capability thresholds for severe-risk domains; production agent evals should similarly include early warning cases before full release gates.

## Core Math

- Task success rate:
  $$
  \frac{\text{successful tasks}}{\text{tasks evaluated}}
  $$
- Tool-call success rate:
  $$
  \frac{\text{successful tool calls}}{\text{tool calls}}
  $$
- Mean latency:
  $$
  \frac{1}{N}\sum_i \text{latency}_i
  $$

## Minimal Code Mental Model

```python
success = task_success_rate([True, False, True])
tool_success = tool_call_success_rate([True, True, False])
breakdown = failure_breakdown(["tool", "model", "tool"])
gate = benchmark_gate(candidate_success=0.76, baseline_success=0.78, min_success=0.75, max_drop=0.03)
```

## Canonical Modules

- Core agent metrics: `agent-evaluation-basics`

## Supporting Modules

- Frozen suites, bucket counts, and baseline gates: `benchmark-harness-basics`
- Running benchmark beliefs updated from prior plus new evidence: `bayesian-benchmark-updating`
- Rollup from bucket scores to group and overall benchmark scores: `hierarchical-benchmark-aggregation`
- Bucket-wise calibration tables and expected calibration error: `bucketed-calibration-diagnostics`
- Confidence-vs-accuracy alignment across runs: `confidence-calibration`
- Final-answer judge scores plus trace-aware grading: `judge-and-trace-grading`
- Multi-metric frontier detection across variants: `pareto-front-benchmark-comparisons`
- Paired-case significance checks for variant comparisons: `paired-run-significance`
- Sequential likelihood-ratio stopping rules: `sequential-test-stopping`
- Approximate sample sizing and detectable effect estimates: `sample-size-and-power`
- Success scores penalized by risky failures: `risk-adjusted-benchmark-summaries`
- Security-focused attack suites and release gates: `security-and-red-team-evals`
- Step-level completion and blockage summaries: `step-level-evaluation`
- Cost-quality summaries across runs: `cost-quality-tradeoffs`
- A/B-style comparison between agent variants: `experiment-comparison`
- Detecting quality drift against a baseline: `regression-checks`
- Grouping failures into stable categories: `failure-taxonomy`

## References

- [OpenAI Agent Evals](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI Trace Grading](https://developers.openai.com/api/docs/guides/trace-grading)
- [Anthropic Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Google DeepMind Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)

## When To Use What

- Start with `agent-evaluation-basics` before adding judge-based or benchmark-heavy evaluation.
- Use `agent-evaluation-basics` for telemetry metrics: final success, tool success, latency, and failure labels.
- Use `benchmark-harness-basics` when you need a fixed task suite with bucket labels and a frozen baseline before comparing variants.
- Use `judge-and-trace-grading` when final-answer scoring hides where the agent failed inside the run.
- Use `bayesian-benchmark-updating` when benchmark evidence arrives in batches and you want an explicit posterior belief instead of only raw running averages.
- Use `hierarchical-benchmark-aggregation` when benchmark results are naturally grouped and you need explicit bucket, group, and overall rollups.
- Use `bucketed-calibration-diagnostics` when a single global calibration gap is too coarse and you need to see where confidence is misaligned by band.
- Use `confidence-calibration` when the agent emits confidence scores and you need to know whether those scores match observed correctness.
- Use `judge-and-trace-grading` when references are weak and you need final-answer judging plus step-trace evidence before accepting a run.
- Use `pareto-front-benchmark-comparisons` when multiple variants trade off success, cost, latency, or safety and you need the non-dominated shortlist.
- Use `paired-run-significance` when two variants were run on the same cases and you want to separate real disagreement from noise.
- Use `sequential-test-stopping` when benchmark evidence arrives incrementally and you want a principled early-stop rule instead of a fixed sample only.
- Use `sample-size-and-power` when you need to estimate how many eval cases are required before a target effect is realistically detectable.
- Use `risk-adjusted-benchmark-summaries` when raw success rates hide too much safety or high-risk failure cost.
- Use `security-and-red-team-evals` when the main benchmark question is whether prompt injection, exfiltration, privilege escalation, or unsafe-action cases are blocked reliably enough to ship.
- Use `step-level-evaluation` when whole-run success is too coarse to explain where the agent fails.
- Use `cost-quality-tradeoffs` when comparing variants where quality, cost, and success all matter.
- Use `experiment-comparison` when you need a side-by-side summary of two prompts, tools, or workflows.
- Use `regression-checks` when a new variant should not fall below an existing baseline on key metrics.
- Use `failure-taxonomy` when repeated failures need a stable set of labels for triage and reporting.
- Track latency and failure labels together so you know whether the bottleneck is planning, tool use, or execution.
