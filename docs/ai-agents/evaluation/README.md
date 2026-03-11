# Evaluation

This section is about how to measure whether an agent succeeds, whether its tool calls work, and where failures happen.

## Purpose

Use this page to understand:
- task success
- tool-call success
- latency and cost baselines
- failure category counts

## First Principles

- Agent evaluation should measure both final outcomes and the steps that produced them.
- Simple metrics are usually enough to find the main bottlenecks.
- A useful evaluation loop separates model failure, tool failure, and workflow failure.

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

## When To Use What

- Start with `agent-evaluation-basics` before adding judge-based or benchmark-heavy evaluation.
- Use `benchmark-harness-basics` when you need a fixed task suite with bucket labels and a frozen baseline before comparing variants.
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
