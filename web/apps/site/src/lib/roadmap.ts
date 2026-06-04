import type { ContentIndex, Track, Topic } from "./content";

const TRACK_ORDER = [
  "dsa",
  "software-engineering",
  "databases",
  "ml",
  "ai-agents",
];

const TOPIC_ORDER: Record<string, string[]> = {
  "dsa": [
    "array",
    "linked-list",
    "hash-tables",
    "string",
    "double-pointers",
    "stack-and-queue",
    "binary-tree",
    "backtracking",
    "greedy-algorithm",
    "dynamic-programming",
    "monotonic-stack",
  ],
  "software-engineering": [
    "workflow-and-ai-tooling",
    "contracts-and-apis",
    "testing-and-verification",
    "security-and-trust",
    "concurrency-and-state",
    "observability-and-operations",
    "reliability-and-delivery",
    "performance-and-cost",
    "system-design-and-patterns",
    "implementation-and-practice",
  ],
  "databases": [
    "relational-core",
    "schema-design",
    "sql-and-analytics",
    "indexing-and-access-paths",
    "transactions-and-concurrency",
    "query-plans-and-performance",
    "caching",
    "streaming-and-cdc",
    "nosql-and-distributed-data",
    "vector-retrieval-and-memory",
  ],
  "ml": [
    "fundamentals",
    "data-and-representation",
    "classical-models",
    "evaluation-and-calibration",
    "optimization-and-training",
    "deep-learning",
    "llms",
    "generative-and-vision",
    "systems-and-mlops",
    "reinforcement-learning",
  ],
  "ai-agents": [
    "overview-and-architecture",
    "prompting-and-context",
    "tool-use-and-mcp",
    "retrieval-and-memory",
    "planning-and-workflows",
    "observability-and-tracing",
    "evaluation-and-benchmarks",
    "guardrails-and-security",
    "multi-agent-systems",
    "practice-and-capstones",
  ],
};

export interface HandbookTopicGroup {
  track: string;
  topic: string;
  name: string;
  sourceTopics: string[];
}

export interface HandbookTopicOutlineItem {
  stage: string;
  title: string;
  description: string;
}

export const MAX_HANDBOOK_SUBSECTIONS = 10;
export const MAX_HANDBOOK_SUBSUBSECTIONS = 20;

function outline(
  items: Array<[stage: string, title: string, description: string]>
): HandbookTopicOutlineItem[] {
  return items.map(([stage, title, description]) => ({
    stage,
    title,
    description,
  }));
}

export const HANDBOOK_TOPIC_OUTLINES: Record<
  string,
  Record<string, HandbookTopicOutlineItem[]>
> = {
  "ml": {
    "fundamentals": outline([
      ["Frame", "Learning Problem", "Define the task, target, data, loss, and baseline before touching models."],
      ["Model", "Math Objects", "Use vectors, matrices, probability, statistics, gradients, and divergence as one shared notation layer."],
      ["Build", "Executable Formula", "Turn the smallest useful equation into vectorized code and a focused test."],
      ["Measure", "Sanity Checks", "Check dimensions, baselines, uncertainty, and whether the result can fail visibly."],
      ["Operate", "Numerical Behavior", "Track stability, scale, conditioning, and approximation limits."],
      ["Practice", "Learning Paths", "Use interview, math-first, and roadmap paths only after the shared notation is clear."],
    ]),
    "data-and-representation": outline([
      ["Frame", "Data Contract", "Name the input, label, split, missingness, leakage risk, and ownership boundary."],
      ["Model", "Representation Choice", "Choose tabular features, sparse text, embeddings, or metric spaces based on the task shape."],
      ["Build", "Preprocessing Pipeline", "Make scaling, encoding, imputation, clipping, and token budgeting reproducible."],
      ["Measure", "Split And Drift Signals", "Use stratification, imbalance checks, leakage tests, and data-quality counters."],
      ["Operate", "Feature Freshness", "Track schema, lineage, rare categories, and embedding refresh cadence."],
      ["Practice", "Canonical Families", "Learn feature families before narrow transforms or historical variants."],
    ]),
    "classical-models": outline([
      ["Frame", "Model Family Choice", "Separate linear, tree, probabilistic, kernel, clustering, and ensemble assumptions."],
      ["Model", "Bias And Variance", "Use capacity, regularization, and feature interactions to reason about error."],
      ["Build", "Fit Predict Loop", "Implement compact training, prediction, and score paths before tuning."],
      ["Measure", "Interpretability Checks", "Compare coefficients, splits, residuals, calibration, and cluster structure."],
      ["Operate", "Baseline Discipline", "Keep classical baselines for tabular, ranking, and small-data problems."],
      ["Practice", "Failure Modes", "Debug leakage, imbalance, outliers, multicollinearity, and overfitting first."],
    ]),
    "evaluation-and-calibration": outline([
      ["Frame", "Metric Contract", "Choose metrics from the decision cost, not from habit or leaderboard fashion."],
      ["Model", "Task Taxonomy", "Separate classification, regression, ranking, retrieval, clustering, agreement, and calibration."],
      ["Build", "Eval Harness", "Create repeatable datasets, baselines, slices, bootstrap intervals, and judge checks."],
      ["Measure", "Uncertainty", "Use confidence intervals, paired tests, calibration gaps, and error buckets."],
      ["Operate", "Release Gate", "Tie metric thresholds to rollout, rollback, and model-comparison decisions."],
      ["Practice", "LLM Era Evals", "Treat model judges, retrieval scores, and human review as calibrated measurement tools."],
    ]),
    "optimization-and-training": outline([
      ["Frame", "Objective", "Identify what is optimized, what is constrained, and what proxy can drift."],
      ["Model", "Loss Surface", "Use gradients, curvature, convexity, schedules, and stochastic noise to reason about training."],
      ["Build", "Training Step", "Implement optimizer state, clipping, schedules, and checkpoint-friendly updates."],
      ["Measure", "Stability Signals", "Watch loss curves, gradient norms, divergence, underfit, and overfit."],
      ["Operate", "Compute Budget", "Balance steps, batch size, precision, memory, and wall-clock cost."],
      ["Practice", "Tuning Order", "Tune data and objective before chasing optimizer variants."],
    ]),
    "deep-learning": outline([
      ["Frame", "Network Role", "Connect architecture pieces to the representation and loss they support."],
      ["Model", "Building Blocks", "Learn layers, activations, normalization, initialization, regularization, and losses as families."],
      ["Build", "Forward Backward Loop", "Make gradients, state, dropout, normalization, and batch behavior explicit."],
      ["Measure", "Gradient Flow", "Check saturation, exploding norms, dead activations, and loss mismatch."],
      ["Operate", "Training Robustness", "Use normalization, initialization, label smoothing, and early stopping deliberately."],
      ["Practice", "Canonical Families", "Prefer family modules over one-off activation, loss, or norm variants."],
    ]),
    "llms": outline([
      ["Frame", "Language Interface", "Connect tokenizer, prompt, context window, task, and output contract."],
      ["Model", "Transformer Core", "Use attention, position encoding, KV cache, MoE, precision, and decoding as one system."],
      ["Build", "Inference And Adaptation", "Implement serving, retrieval, fine-tuning, LoRA, quantization, and structured eval loops."],
      ["Measure", "Behavioral Evaluation", "Use task metrics, judge agreement, retrieval quality, reasoning checks, and safety gates."],
      ["Operate", "Latency And Cost", "Balance context length, cache reuse, batching, quantization, and quality loss."],
      ["Practice", "Alignment And Reasoning", "Separate SFT, preference optimization, RLHF/RLAIF, reasoning, and test-time compute."],
    ]),
    "generative-and-vision": outline([
      ["Frame", "Signal Type", "Separate image, sequence, latent-variable, diffusion, and adversarial generation problems."],
      ["Model", "Architectures", "Use CNNs, pooling, residual blocks, VAEs, GANs, diffusion, and autoregressive models by failure mode."],
      ["Build", "Generation Pipeline", "Make preprocessing, denoising, sampling, guidance, and postprocessing explicit."],
      ["Measure", "Output Quality", "Use task-specific quality, diversity, stability, and human-visible failure checks."],
      ["Operate", "Compute Shape", "Track memory, resolution, sampling steps, throughput, and deployment constraints."],
      ["Practice", "Modern Relevance", "Keep older models as mental models; emphasize diffusion, multimodal, and representation transfer."],
    ]),
    "systems-and-mlops": outline([
      ["Frame", "Production Contract", "Define model, data, eval, serving, rollout, monitoring, and rollback responsibilities."],
      ["Model", "System Bottlenecks", "Reason about GPU memory, distributed training, inference latency, data freshness, and cost."],
      ["Build", "Serving Path", "Implement model loading, batching, caching, quantization, tracing, and release gates."],
      ["Measure", "Operational Metrics", "Track quality, calibration, latency, throughput, drift, cost, and safety regressions together."],
      ["Operate", "Lifecycle", "Own retraining, eval refresh, incident response, and versioned deployment artifacts."],
      ["Practice", "Capstone Gate", "Use end-to-end capstones when model, eval, serving, and rollout choices interact."],
    ]),
    "reinforcement-learning": outline([
      ["Frame", "Decision Problem", "Name states, actions, rewards, horizon, constraints, and offline data limits."],
      ["Model", "RL Families", "Separate value methods, policy gradients, actor-critic, bandits, offline RL, and RL for LLMs."],
      ["Build", "Update Rule", "Implement reward, return, advantage, policy update, and safety constraint paths."],
      ["Measure", "Policy Quality", "Use regret, stability, reward hacking checks, off-policy evaluation, and human preference signals."],
      ["Operate", "Risk Boundary", "Treat exploration, reward misspecification, and deployment feedback loops as product risks."],
      ["Practice", "LLM Post-Training", "Connect RLHF, DPO, GRPO-style methods, and reward modeling to modern alignment practice."],
    ]),
  },
  "ai-agents": {
    "overview-and-architecture": outline([
      ["Frame", "Agent Boundary", "Separate model call, loop state, tool boundary, memory, and external side effects."],
      ["Model", "Workflow Or Agent", "Use deterministic workflows first; add autonomous loops only when the task needs them."],
      ["Build", "Loop Architecture", "Define observe, decide, act, validate, recover, and stop as explicit states."],
      ["Measure", "Run Outcome", "Track task success, latency, cost, tool success, and failure category."],
      ["Operate", "Control Surface", "Add traces, approvals, sandboxing, and rollback before scaling autonomy."],
      ["Practice", "Production Roadmap", "Move from single loop to workflows, evals, guardrails, and capstones."],
    ]),
    "prompting-and-context": outline([
      ["Frame", "Instruction Contract", "State role, task, constraints, examples, output schema, and refusal boundary."],
      ["Model", "Context Budget", "Separate durable instructions, task data, retrieved context, memory, and transient scratch."],
      ["Build", "Prompt Shape", "Use delimiters, examples, self-checks, and context-packing rules."],
      ["Measure", "Prompt Robustness", "Test ambiguity, missing context, formatting drift, and adversarial text."],
      ["Operate", "Context Hygiene", "Keep prompts versioned, inspectable, and small enough to debug."],
      ["Practice", "Prompt To System", "Prompts should become contracts, tools, eval cases, or guardrails when repeated."],
    ]),
    "tool-use-and-mcp": outline([
      ["Frame", "Action Boundary", "Decide when the agent should call a function, connector, terminal, computer UI, or MCP server."],
      ["Model", "Tool Contract", "Use schema, auth scope, permission, result type, failure path, and owner."],
      ["Build", "Call Validate Loop", "Normalize arguments, execute, validate result, and decide retry or escalation."],
      ["Measure", "Tool Reliability", "Track tool success, argument errors, result defects, latency, and risk-adjusted value."],
      ["Operate", "Protocol Boundary", "Treat MCP as tool/resource/prompt discovery and lifecycle, not as authorization by itself."],
      ["Practice", "Safe Expansion", "Add scoped connectors, terminal use, and computer use only after one typed tool is stable."],
    ]),
    "retrieval-and-memory": outline([
      ["Frame", "Grounding Need", "Decide whether the agent needs external facts, prior state, user memory, or long-term records."],
      ["Model", "Retrieval Shape", "Separate lexical retrieval, vector retrieval, metadata filters, reranking, and memory recall."],
      ["Build", "Grounded Context", "Assemble chunks, citations, memory compaction, and abstention rules."],
      ["Measure", "Retrieval Quality", "Use golden queries, coverage, hard negatives, answer support, and freshness checks."],
      ["Operate", "Memory Lifecycle", "Control retention, conflicts, privacy, poisoning risk, and update cadence."],
      ["Practice", "Agentic RAG", "Let agents reformulate and critique retrieval only after basic retrieval evals exist."],
    ]),
    "planning-and-workflows": outline([
      ["Frame", "Task Decomposition", "Name the goal, route choices, step budget, stop condition, and escalation criteria."],
      ["Model", "Workflow Pattern", "Choose chaining, routing, parallelization, orchestrator-worker, evaluator-optimizer, or state machine."],
      ["Build", "Stateful Run", "Represent plan, action, observation, retry, handoff, and recovery as structured state."],
      ["Measure", "Trajectory Quality", "Evaluate step correctness, budget use, failure recovery, and final outcome."],
      ["Operate", "Latency And Risk", "Bound retries, concurrency, handoffs, and tool side effects."],
      ["Practice", "Workflow Before Autonomy", "Use explicit workflows when they are clearer than open-ended planning."],
    ]),
    "observability-and-tracing": outline([
      ["Frame", "Run Visibility", "Decide what a human needs to inspect after a failure or risky success."],
      ["Model", "Span Taxonomy", "Separate model calls, tool calls, retrieval, memory writes, handoffs, guardrails, and final output."],
      ["Build", "Trace Packet", "Emit structured spans, attributes, costs, tokens, decisions, and outcome labels."],
      ["Measure", "Run Analytics", "Sample runs, cluster failures, alert on thresholds, and compare variants."],
      ["Operate", "Debug Loop", "Connect traces to dashboards, runbooks, root cause, and eval case creation."],
      ["Practice", "Eval Feedback", "Turn repeated trace failures into regression tests and release gates."],
    ]),
    "evaluation-and-benchmarks": outline([
      ["Frame", "Success Definition", "Write task, environment, expected outcome, allowed tools, and risk class."],
      ["Model", "Eval Layers", "Measure final outcome, trajectory, tool calls, retrieval support, calibration, and safety."],
      ["Build", "Benchmark Harness", "Freeze datasets, baselines, graders, trace checks, and release thresholds."],
      ["Measure", "Statistical Confidence", "Use paired comparisons, sample size, sequential stops, and cost-quality frontiers."],
      ["Operate", "Regression Gate", "Run evals before rollout and when models, tools, prompts, or data change."],
      ["Practice", "Human Calibration", "Use model graders only with spot checks, rubrics, and disagreement analysis."],
    ]),
    "guardrails-and-security": outline([
      ["Frame", "Trust Boundary", "Identify untrusted input, tool authority, secrets, external effects, and human review needs."],
      ["Model", "Risk Policy", "Use allow/deny rules, risk scoring, cost matrices, and escalation tables."],
      ["Build", "Guarded Action", "Validate inputs, filter outputs, gate approvals, sandbox tools, and limit privileges."],
      ["Measure", "Red Team Coverage", "Test prompt injection, data exfiltration, unsafe tools, memory poisoning, and overbroad scopes."],
      ["Operate", "Auditability", "Log policy decisions, approvals, blocked actions, and incident-ready evidence."],
      ["Practice", "Least Privilege", "Make risky actions opt-in, scoped, reversible, and reviewable."],
    ]),
    "multi-agent-systems": outline([
      ["Frame", "Coordination Need", "Use multiple agents only when role split beats one stronger loop."],
      ["Model", "Coordination Pattern", "Choose orchestrator-workers, role assignment, delegation budgets, debate, or arbitration."],
      ["Build", "Worker Contract", "Give each worker narrow context, output schema, status, and budget."],
      ["Measure", "Coordination Cost", "Track duplicate work, disagreement, latency, merge quality, and failure attribution."],
      ["Operate", "Shared State", "Keep global state, authority, and escalation under one accountable owner."],
      ["Practice", "Cap Coordination", "Stop adding agents when routing cost exceeds quality or reliability gains."],
    ]),
    "practice-and-capstones": outline([
      ["Frame", "Readiness Check", "Verify the learner can define the goal, tools, memory, eval, and risk boundary."],
      ["Model", "Integrated System", "Combine prompting, tools, retrieval, workflow state, observability, and guardrails."],
      ["Build", "Capstone Loop", "Implement a small agent with explicit decisions, tests, and run artifacts."],
      ["Measure", "Certification Gate", "Use task success, trace review, failure taxonomy, and regression cases."],
      ["Operate", "Release Decision", "Require rollback, escalation, cost ceiling, and monitoring before production use."],
      ["Practice", "Portfolio Artifact", "Leave behind a runnable system, not just notes."],
    ]),
  },
  "databases": {
    "relational-core": outline([
      ["Frame", "Source Of Truth", "Define entities, keys, relationships, constraints, and ownership."],
      ["Model", "Relational Algebra", "Use joins, null semantics, cascades, and integrity as the core reasoning layer."],
      ["Build", "Schema Plus Query", "Implement tables, keys, constraints, and simple joins before optimization."],
      ["Measure", "Correctness", "Check duplicates, orphan rows, cardinality, and constraint violations."],
      ["Operate", "Access Policy", "Add row-level security, soft deletes, and migration boundaries deliberately."],
      ["Practice", "Relational First", "Use JSON or NoSQL only when the relational boundary is understood."],
    ]),
    "schema-design": outline([
      ["Frame", "Product Grain", "Name entity, event, fact grain, history, tenancy, and delete boundaries."],
      ["Model", "Data Shape", "Choose normalized, denormalized, dimensional, snapshot, current-state, or document-chunk schemas."],
      ["Build", "Evolution Path", "Plan schema changes, backfills, audit tables, and lineage records."],
      ["Measure", "Data Quality", "Detect double counting, stale history, missing lineage, and tenant leakage."],
      ["Operate", "Lifecycle", "Support versioning, offboarding, retention, and ownership changes."],
      ["Practice", "AI Data", "Design chunks, embeddings, metadata, and eval logs as first-class tables."],
    ]),
    "sql-and-analytics": outline([
      ["Frame", "Question Shape", "Separate lookup, aggregation, latest-row, funnel, retention, as-of, and backfill questions."],
      ["Model", "Relational Transform", "Use windows, joins, grouping, watermarks, and materialization intentionally."],
      ["Build", "Composable Query", "Prefer readable CTEs, stable grain, and explicit filters."],
      ["Measure", "Analytic Correctness", "Check double counts, late arrivals, approximate counts, and refresh boundaries."],
      ["Operate", "Offline Stack", "Use DuckDB, Parquet, incremental refresh, and backfill strategy for local and batch work."],
      ["Practice", "Eval Analytics", "Treat model and retrieval eval analysis as ordinary analytics."],
    ]),
    "indexing-and-access-paths": outline([
      ["Frame", "Access Pattern", "Name predicates, ordering, cardinality, tenancy, and write frequency."],
      ["Model", "Index Family", "Use B-tree, composite, covering, partial, expression, GIN/JSONB, and partition pruning by access path."],
      ["Build", "Index Design", "Create indexes that match predicates and ordering, not generic columns."],
      ["Measure", "Selectivity", "Check scan type, write amplification, low-cardinality behavior, and index hit value."],
      ["Operate", "Maintenance", "Watch bloat, write cost, multi-tenant skew, and regression after schema changes."],
      ["Practice", "Index Boundaries", "Separate partitioning, indexing, and query-plan tuning decisions."],
    ]),
    "transactions-and-concurrency": outline([
      ["Frame", "Consistency Need", "Name invariants, isolation requirement, retry behavior, and replica expectations."],
      ["Model", "Concurrency Control", "Use transactions, MVCC, locks, optimistic control, sagas, and outbox patterns."],
      ["Build", "Safe Write Path", "Implement idempotent writes, serializable retries, lock ordering, and partial-failure handling."],
      ["Measure", "Anomalies", "Test write skew, phantom reads, deadlocks, lag, and failover behavior."],
      ["Operate", "Replica Reality", "Handle read-after-write, failover routing, and lag-aware reads."],
      ["Practice", "Boundary Choice", "Use sagas only when one transaction is no longer the right boundary."],
    ]),
    "query-plans-and-performance": outline([
      ["Frame", "Runtime Symptom", "Start from slow query, memory pressure, bad join, sort cost, or plan regression."],
      ["Model", "Planner Reasoning", "Use cardinality, selectivity, sargability, join order, scan choice, and statistics."],
      ["Build", "Plan Inspection", "Read EXPLAIN output and compare expected versus actual access paths."],
      ["Measure", "Regression Signal", "Track latency, row estimates, sort behavior, table lookups, and N+1 cost."],
      ["Operate", "Plan Stability", "Update stats, refine predicates, and avoid changes that hide real access-pattern problems."],
      ["Practice", "Tuning Order", "Fix query shape and statistics before adding speculative indexes."],
    ]),
    "caching": outline([
      ["Frame", "Freshness Contract", "Define value, key, owner, invalidation trigger, TTL, and stale tolerance."],
      ["Model", "Cache Pattern", "Choose cache-aside, write-through, write-behind, negative, semantic, or client-side cache."],
      ["Build", "Cache Path", "Design keys, TTL jitter, warming, admission, and stampede controls."],
      ["Measure", "Cache Value", "Track hit rate, semantic hit quality, stale reads, hot keys, and origin relief."],
      ["Operate", "Invalidation", "Treat invalidation as correctness logic, not a cleanup task."],
      ["Practice", "Semantic Cache", "Use semantic caching for repeated model calls only with eval and invalidation rules."],
    ]),
    "streaming-and-cdc": outline([
      ["Frame", "Change Flow", "Define event source, ordering, watermark, schema version, replay, and consumer ownership."],
      ["Model", "Pipeline Shape", "Separate application events, CDC, outbox relay, connectors, offsets, and materialized views."],
      ["Build", "Consumer Logic", "Implement idempotence, offsets, rebalances, backfills, and delete propagation."],
      ["Measure", "Lag And Correctness", "Track watermark lag, duplicate handling, missed deletes, and replay safety."],
      ["Operate", "Evolution", "Version events, handle late arrivals, and keep replay operational."],
      ["Practice", "Bridge Layer", "Use CDC to connect operational truth, analytics, retrieval, and AI eval stores."],
    ]),
    "nosql-and-distributed-data": outline([
      ["Frame", "Distribution Need", "Justify document, key-value, wide-row, sharding, quorum, or LSM design by access pattern."],
      ["Model", "Trade-Off Surface", "Reason about consistency, repair, compaction, read amplification, hotspots, and secondary indexes."],
      ["Build", "Partitioned Model", "Design keys, tenants, documents, wide rows, and repair boundaries."],
      ["Measure", "Distributed Health", "Track quorum outcomes, compaction debt, read/write amplification, and tenant skew."],
      ["Operate", "Repair Lifecycle", "Plan anti-entropy, read repair, compression, and offboarding."],
      ["Practice", "Postgres Check", "Ask when Postgres is enough before adding a distributed store."],
    ]),
    "vector-retrieval-and-memory": outline([
      ["Frame", "Retrieval Contract", "Define corpus, chunks, embeddings, metadata, permissions, freshness, and answer use."],
      ["Model", "Search Stack", "Combine exact search, ANN, HNSW, IVF, hybrid search, filters, reranking, and memory compaction."],
      ["Build", "Retrieval Pipeline", "Implement embedding tables, metadata filters, rerankers, agent memory, and eval datasets."],
      ["Measure", "Quality", "Use golden queries, hard negatives, recall, precision, rerank gain, and answer support."],
      ["Operate", "Freshness And Cost", "Track re-embedding, stale chunks, index growth, latency, and permission drift."],
      ["Practice", "Hybrid Capstone", "Tie relational truth, CDC, vector retrieval, cache, and eval logs together."],
    ]),
  },
  "software-engineering": {
    "workflow-and-ai-tooling": outline([
      ["Frame", "Development Contract", "Define spec, repo layout, generated-code boundary, review rule, and test target."],
      ["Model", "AI-Assisted Loop", "Use agents for implementation speed while humans own invariants, risk, and acceptance."],
      ["Build", "Reproducible Workflow", "Set up environments, CI, codegen boundaries, and review discipline."],
      ["Measure", "Delivery Signal", "Track CI time, flaky checks, review queue, generated-code risk, and merge blockers."],
      ["Operate", "Tool Boundary", "Keep sandboxing, permissions, secrets, and approvals explicit."],
      ["Practice", "Spec First", "Turn vague requests into spec, patch, tests, and review notes."],
    ]),
    "contracts-and-apis": outline([
      ["Frame", "Boundary Contract", "Define request, response, schema, idempotency, auth, compatibility, and error behavior."],
      ["Model", "API Lifecycle", "Use versioning, pagination, timeouts, retries, backoff, and webhook verification."],
      ["Build", "Runtime Validation", "Validate inputs and outputs at every external boundary."],
      ["Measure", "Contract Breakage", "Test schema evolution, retry safety, pagination completeness, and signature failures."],
      ["Operate", "Compatibility", "Keep consumers safe through migration windows and explicit deprecation rules."],
      ["Practice", "Structured Outputs", "Treat model/tool outputs like API responses with schemas and validators."],
    ]),
    "testing-and-verification": outline([
      ["Frame", "Invariant", "Name the property, contract, regression, or behavior that must survive change."],
      ["Model", "Test Portfolio", "Balance unit, contract, property, golden, integration, trace, and eval tests."],
      ["Build", "Focused Check", "Write small tests that expose the failure mode directly."],
      ["Measure", "Confidence", "Track flake rate, coverage of critical paths, regression classes, and eval disagreement."],
      ["Operate", "Release Gate", "Use tests and evals as deployment decisions, not just CI decoration."],
      ["Practice", "AI Generated Code", "Add regression and metamorphic checks when implementation comes from an agent."],
    ]),
    "security-and-trust": outline([
      ["Frame", "Threat Boundary", "Identify identity, authorization, data validation, secrets, dependency risk, and agentic tools."],
      ["Model", "Least Privilege", "Use deny-by-default scopes, explicit approvals, sandboxing, and audit logs."],
      ["Build", "Secure Path", "Implement validation, encoding, secret handling, supply-chain checks, and policy decisions."],
      ["Measure", "Risk Signal", "Track credential age, exposed permissions, dependency signals, unsafe tool attempts, and blocked actions."],
      ["Operate", "Review Discipline", "Make security part of code review, release, incident, and agent-tool design."],
      ["Practice", "Agentic Risk", "Test prompt injection, overbroad scopes, memory poisoning, and unsafe side effects."],
    ]),
    "concurrency-and-state": outline([
      ["Frame", "Shared State", "Name mutable state, queue, lock, timeout, retry, cancellation, and idempotency boundary."],
      ["Model", "Coordination Pattern", "Choose lock, queue, state machine, worker retry, or deadline propagation."],
      ["Build", "State Transition", "Represent states and transitions explicitly so retries and cancellation stay safe."],
      ["Measure", "Race Signal", "Test interleavings, duplicate delivery, timeout propagation, and retry semantics."],
      ["Operate", "Backpressure", "Watch queue depth, contention, dead time, and stuck work."],
      ["Practice", "State Machines", "Use state-machine thinking when ad hoc flags become unclear."],
    ]),
    "observability-and-operations": outline([
      ["Frame", "Production Question", "Decide whether you need logs, metrics, traces, SLOs, dashboards, or runbooks."],
      ["Model", "Signal Layer", "Use structured events, percentiles, error budgets, traces, and alert thresholds."],
      ["Build", "Operable Output", "Emit searchable logs, labeled metrics, trace context, and incident-ready dashboards."],
      ["Measure", "User Impact", "Alert on service risk and budget burn, not raw noise."],
      ["Operate", "Incident Loop", "Connect signals to root cause, runbooks, mitigation, and follow-up tests."],
      ["Practice", "Trace To Test", "Convert production failures into regression checks."],
    ]),
    "reliability-and-delivery": outline([
      ["Frame", "Failure Model", "Name overload, dependency failure, partial failure, rollback need, and platform boundary."],
      ["Model", "Resilience Pattern", "Use degradation, retries, fallback, bulkheads, circuit breakers, canaries, and progressive delivery."],
      ["Build", "Recovery Path", "Implement rollback, retry policy, blast-radius limit, and incident handoff."],
      ["Measure", "Reliability Signal", "Track success rate, error-budget burn, retry load, rollout health, and recovery time."],
      ["Operate", "Delivery Safety", "Use platform abstractions only when they reduce toil without hiding ownership."],
      ["Practice", "Postmortem Loop", "Turn incidents into better assumptions, tests, runbooks, and rollout checks."],
    ]),
    "performance-and-cost": outline([
      ["Frame", "Bottleneck", "Identify latency, throughput, memory, network, CPU, I/O, contention, or cost."],
      ["Model", "Budget", "Use latency decomposition, cache hit rate, batching trade-offs, allocation, and cost curves."],
      ["Build", "Measurement First", "Instrument before optimizing; then change one bottleneck at a time."],
      ["Measure", "Trade-Off", "Track tail latency, throughput, memory, hit rate, and unit cost together."],
      ["Operate", "Capacity", "Keep budgets visible in dashboards, alerts, and release decisions."],
      ["Practice", "Optimization Order", "Fix architecture, caching, batching, and profiling before micro-optimizations."],
    ]),
    "system-design-and-patterns": outline([
      ["Frame", "Requirements", "State functional needs, scale, latency, consistency, failure domains, and ownership."],
      ["Model", "Boundary Choice", "Choose services, storage, workflows, patterns, and state placement by trade-off."],
      ["Build", "Architecture Sketch", "Represent data flow, control flow, failure path, and recovery path."],
      ["Measure", "Design Stress", "Estimate capacity, fanout, queue depth, storage cost, and consistency risk."],
      ["Operate", "Evolution", "Keep ownership, migration, observability, and rollback in the design."],
      ["Practice", "Patterns As Tools", "Use adapters, DI, strategy, and state machines only when they clarify real boundaries."],
    ]),
    "implementation-and-practice": outline([
      ["Frame", "Language Role", "Use Python, Rust, and TypeScript as implementation tools, not separate curricula."],
      ["Model", "Runtime Boundary", "Map typing, ownership, async, validation, packaging, and profiling to service responsibilities."],
      ["Build", "Production-Shaped Code", "Write small libraries and services with explicit errors, tests, and interfaces."],
      ["Measure", "Readiness", "Use assessments for contracts, tests, operations, security, and delivery judgment."],
      ["Operate", "Capstone", "Combine spec, implementation, verification, rollout, incident, and recovery artifacts."],
      ["Practice", "Portfolio", "Finish with runnable systems that demonstrate engineering trade-offs."],
    ]),
  },
};

export const HANDBOOK_TOPIC_GROUPS: Record<string, HandbookTopicGroup[]> = {
  "ml": [
    {
      track: "ml",
      topic: "fundamentals",
      name: "Fundamentals",
      sourceTopics: [
        "fundamentals",
        "path-beginner",
        "path-interview",
        "path-math-first",
        "roadmap",
      ],
    },
    {
      track: "ml",
      topic: "data-and-representation",
      name: "Data And Representation",
      sourceTopics: ["data", "representation"],
    },
    {
      track: "ml",
      topic: "classical-models",
      name: "Classical Models",
      sourceTopics: ["models"],
    },
    {
      track: "ml",
      topic: "evaluation-and-calibration",
      name: "Evaluation And Calibration",
      sourceTopics: ["evaluation"],
    },
    {
      track: "ml",
      topic: "optimization-and-training",
      name: "Optimization And Training",
      sourceTopics: ["optimization"],
    },
    {
      track: "ml",
      topic: "deep-learning",
      name: "Deep Learning",
      sourceTopics: ["deep-learning"],
    },
    {
      track: "ml",
      topic: "llms",
      name: "LLMs",
      sourceTopics: ["llm", "path-llm-systems"],
    },
    {
      track: "ml",
      topic: "generative-and-vision",
      name: "Generative And Vision",
      sourceTopics: ["generative", "computer-vision"],
    },
    {
      track: "ml",
      topic: "systems-and-mlops",
      name: "Systems And MLOps",
      sourceTopics: ["systems", "mlops", "assessments", "capstones"],
    },
    {
      track: "ml",
      topic: "reinforcement-learning",
      name: "Reinforcement Learning",
      sourceTopics: ["reinforcement-learning"],
    },
  ],
  "ai-agents": [
    {
      track: "ai-agents",
      topic: "overview-and-architecture",
      name: "Overview And Architecture",
      sourceTopics: ["overview"],
    },
    {
      track: "ai-agents",
      topic: "prompting-and-context",
      name: "Prompting And Context",
      sourceTopics: ["prompting"],
    },
    {
      track: "ai-agents",
      topic: "tool-use-and-mcp",
      name: "Tool Use And MCP",
      sourceTopics: ["tool-use"],
    },
    {
      track: "ai-agents",
      topic: "retrieval-and-memory",
      name: "Retrieval And Memory",
      sourceTopics: ["rag", "memory"],
    },
    {
      track: "ai-agents",
      topic: "planning-and-workflows",
      name: "Planning And Workflows",
      sourceTopics: ["planning", "workflows"],
    },
    {
      track: "ai-agents",
      topic: "observability-and-tracing",
      name: "Observability And Tracing",
      sourceTopics: ["observability"],
    },
    {
      track: "ai-agents",
      topic: "evaluation-and-benchmarks",
      name: "Evaluation And Benchmarks",
      sourceTopics: ["evaluation", "evals"],
    },
    {
      track: "ai-agents",
      topic: "guardrails-and-security",
      name: "Guardrails And Security",
      sourceTopics: ["guardrails"],
    },
    {
      track: "ai-agents",
      topic: "multi-agent-systems",
      name: "Multi-Agent Systems",
      sourceTopics: ["multi-agent"],
    },
    {
      track: "ai-agents",
      topic: "practice-and-capstones",
      name: "Practice And Capstones",
      sourceTopics: ["assessments", "capstones"],
    },
  ],
  "databases": [
    {
      track: "databases",
      topic: "relational-core",
      name: "Relational Core",
      sourceTopics: ["relational"],
    },
    {
      track: "databases",
      topic: "schema-design",
      name: "Schema Design",
      sourceTopics: ["schema-design"],
    },
    {
      track: "databases",
      topic: "sql-and-analytics",
      name: "SQL And Analytics",
      sourceTopics: ["sql-patterns"],
    },
    {
      track: "databases",
      topic: "indexing-and-access-paths",
      name: "Indexing And Access Paths",
      sourceTopics: ["indexing"],
    },
    {
      track: "databases",
      topic: "transactions-and-concurrency",
      name: "Transactions And Concurrency",
      sourceTopics: ["transactions"],
    },
    {
      track: "databases",
      topic: "query-plans-and-performance",
      name: "Query Plans And Performance",
      sourceTopics: ["query-plans"],
    },
    {
      track: "databases",
      topic: "caching",
      name: "Caching",
      sourceTopics: ["caching"],
    },
    {
      track: "databases",
      topic: "streaming-and-cdc",
      name: "Streaming And CDC",
      sourceTopics: ["streaming"],
    },
    {
      track: "databases",
      topic: "nosql-and-distributed-data",
      name: "NoSQL And Distributed Data",
      sourceTopics: ["nosql"],
    },
    {
      track: "databases",
      topic: "vector-retrieval-and-memory",
      name: "Vector Retrieval And Memory",
      sourceTopics: ["vector-db", "assessments", "capstones"],
    },
  ],
  "software-engineering": [
    {
      track: "software-engineering",
      topic: "workflow-and-ai-tooling",
      name: "Workflow And AI Tooling",
      sourceTopics: ["tooling"],
    },
    {
      track: "software-engineering",
      topic: "contracts-and-apis",
      name: "Contracts And APIs",
      sourceTopics: ["apis"],
    },
    {
      track: "software-engineering",
      topic: "testing-and-verification",
      name: "Testing And Verification",
      sourceTopics: ["testing"],
    },
    {
      track: "software-engineering",
      topic: "security-and-trust",
      name: "Security And Trust",
      sourceTopics: ["security-basics"],
    },
    {
      track: "software-engineering",
      topic: "concurrency-and-state",
      name: "Concurrency And State",
      sourceTopics: ["concurrency"],
    },
    {
      track: "software-engineering",
      topic: "observability-and-operations",
      name: "Observability And Operations",
      sourceTopics: ["observability"],
    },
    {
      track: "software-engineering",
      topic: "reliability-and-delivery",
      name: "Reliability And Delivery",
      sourceTopics: ["reliability", "platform-and-delivery"],
    },
    {
      track: "software-engineering",
      topic: "performance-and-cost",
      name: "Performance And Cost",
      sourceTopics: ["performance"],
    },
    {
      track: "software-engineering",
      topic: "system-design-and-patterns",
      name: "System Design And Patterns",
      sourceTopics: ["system-design", "design-patterns"],
    },
    {
      track: "software-engineering",
      topic: "implementation-and-practice",
      name: "Implementation And Practice",
      sourceTopics: [
        "python",
        "rust",
        "typescript",
        "learning-paths",
        "assessments",
        "capstones",
      ],
    },
  ],
};

function buildRankMap(order: string[]) {
  const map = new Map<string, number>();
  order.forEach((id, index) => map.set(id, index));
  return map;
}

const TRACK_RANK = buildRankMap(TRACK_ORDER);
const TOPIC_RANKS = new Map(
  Object.entries(TOPIC_ORDER).map(([trackId, order]) => [trackId, buildRankMap(order)])
);

function topicFromGroup(content: ContentIndex, group: HandbookTopicGroup): Topic {
  const sourceTopicSet = new Set(group.sourceTopics);
  const docCount = content.docs.filter(
    (doc) => doc.track === group.track && sourceTopicSet.has(doc.topic)
  ).length;
  const moduleCount = content.modules.filter(
    (module) => module.track === group.track && sourceTopicSet.has(module.topic)
  ).length;

  return {
    track: group.track,
    topic: group.topic,
    name: group.name,
    path: `/track/${group.track}/${group.topic}`,
    hasDoc: docCount > 0,
    docCount,
    moduleCount,
  };
}

export function hasHandbookGroups(trackId: string) {
  return (HANDBOOK_TOPIC_GROUPS[trackId] ?? []).length > 0;
}

export function getHandbookTopics(content: ContentIndex, trackId?: string): Topic[] {
  const groupedTrackIds = new Set(Object.keys(HANDBOOK_TOPIC_GROUPS));
  const groupedTopics = Object.entries(HANDBOOK_TOPIC_GROUPS)
    .filter(([groupTrackId]) => !trackId || groupTrackId === trackId)
    .flatMap(([, groups]) => groups.map((group) => topicFromGroup(content, group)));

  const ungroupedTopics = content.topics.filter(
    (topic) =>
      !groupedTrackIds.has(topic.track) &&
      (!trackId || topic.track === trackId)
  );

  return sortTopics([...ungroupedTopics, ...groupedTopics]);
}

export function resolveHandbookTopic(
  content: ContentIndex,
  trackId: string,
  topicId: string
): { topic: Topic; sourceTopics: string[]; isGrouped: boolean } | undefined {
  const group = HANDBOOK_TOPIC_GROUPS[trackId]?.find(
    (candidate) => candidate.topic === topicId
  );
  if (group) {
    return {
      topic: topicFromGroup(content, group),
      sourceTopics: group.sourceTopics,
      isGrouped: true,
    };
  }

  const topic = content.topics.find(
    (candidate) => candidate.track === trackId && candidate.topic === topicId
  );
  if (!topic) return undefined;
  return { topic, sourceTopics: [topic.topic], isGrouped: false };
}

export function getCanonicalTopicId(trackId: string, sourceTopic: string) {
  const group = HANDBOOK_TOPIC_GROUPS[trackId]?.find((candidate) =>
    candidate.sourceTopics.includes(sourceTopic)
  );
  return group?.topic ?? sourceTopic;
}

export function getHandbookTopicOutline(trackId: string, topicId: string) {
  return HANDBOOK_TOPIC_OUTLINES[trackId]?.[topicId] ?? [];
}

export function sortTracks(tracks: Track[]): Track[] {
  return tracks.slice().sort((a, b) => {
    const rankA = TRACK_RANK.get(a.id) ?? Number.MAX_SAFE_INTEGER;
    const rankB = TRACK_RANK.get(b.id) ?? Number.MAX_SAFE_INTEGER;
    if (rankA !== rankB) return rankA - rankB;
    return a.name.localeCompare(b.name);
  });
}

export function sortTopics(topics: Topic[]): Topic[] {
  return topics.slice().sort((a, b) => {
    const trackRankA = TRACK_RANK.get(a.track) ?? Number.MAX_SAFE_INTEGER;
    const trackRankB = TRACK_RANK.get(b.track) ?? Number.MAX_SAFE_INTEGER;
    if (trackRankA !== trackRankB) return trackRankA - trackRankB;
    if (a.track !== b.track) return a.track.localeCompare(b.track);

    const topicRank = TOPIC_RANKS.get(a.track);
    const rankA = topicRank?.get(a.topic);
    const rankB = topicRank?.get(b.topic);
    if (rankA != null && rankB != null) return rankA - rankB;
    if (rankA != null) return -1;
    if (rankB != null) return 1;

    return a.name.localeCompare(b.name);
  });
}

export function sortTopicsForTrack(topics: Topic[], trackId: string): Topic[] {
  const topicRank = TOPIC_RANKS.get(trackId);
  return topics.slice().sort((a, b) => {
    const rankA = topicRank?.get(a.topic);
    const rankB = topicRank?.get(b.topic);
    if (rankA != null && rankB != null) return rankA - rankB;
    if (rankA != null) return -1;
    if (rankB != null) return 1;
    return a.name.localeCompare(b.name);
  });
}

export function extractModuleOrder(
  docContent: string | undefined,
  trackId: string,
  topicId: string
): string[] {
  const order: string[] = [];
  const seen = new Set<string>();
  if (!docContent) return order;

  const { canonical, supporting } = extractTopicEntryGroups(
    docContent,
    trackId,
    topicId
  );
  for (const slug of [...canonical, ...supporting]) {
    if (!seen.has(slug)) {
      seen.add(slug);
      order.push(slug);
    }
  }

  const pattern = new RegExp(`modules/${trackId}/${topicId}/([a-z0-9-]+)`, "g");
  let match: RegExpExecArray | null;
  while ((match = pattern.exec(docContent)) !== null) {
    const slug = match[1];
    if (!seen.has(slug)) {
      seen.add(slug);
      order.push(slug);
    }
  }
  return order;
}

function extractSectionBodies(
  docContent: string | undefined,
  headingNames: string[]
): string[] {
  if (!docContent) return [];
  const headingSet = new Set(headingNames.map((heading) => heading.toLowerCase()));
  const lines = docContent.split(/\r?\n/);
  const bodies: string[] = [];
  let active = false;
  let currentLines: string[] = [];

  function flush() {
    if (active && currentLines.length > 0) {
      bodies.push(currentLines.join("\n").trim());
    }
    currentLines = [];
  }

  for (const line of lines) {
    const heading = line.match(/^##\s+(.+)$/);
    if (heading) {
      flush();
      active = headingSet.has(heading[1].trim().toLowerCase());
      continue;
    }
    if (active) currentLines.push(line);
  }
  flush();

  return bodies.filter(Boolean);
}

function extractReferencedSlugs(
  content: string,
  trackId: string,
  topicId: string
): string[] {
  const slugs: string[] = [];
  const seen = new Set<string>();
  const pathPattern = new RegExp(
    `(?:docs|modules)/${trackId}/${topicId}/([a-z0-9-]+)`,
    "g"
  );
  const inlinePattern = /`([^`]+)`/g;

  function push(raw: string) {
    const trimmed = raw.trim();
    let slug: string | undefined;
    const pathMatch = trimmed.match(
      new RegExp(`^(?:docs|modules)/${trackId}/${topicId}/([a-z0-9-]+)$`)
    );
    if (pathMatch) {
      slug = pathMatch[1];
    } else if (/^[a-z0-9-]+$/.test(trimmed)) {
      slug = trimmed;
    }
    if (slug && !seen.has(slug)) {
      seen.add(slug);
      slugs.push(slug);
    }
  }

  let match: RegExpExecArray | null;
  while ((match = inlinePattern.exec(content)) !== null) {
    push(match[1]);
  }
  while ((match = pathPattern.exec(content)) !== null) {
    push(match[1]);
  }

  return slugs;
}

export function extractTopicEntryGroups(
  docContent: string | undefined,
  trackId: string,
  topicId: string
): { canonical: string[]; supporting: string[] } {
  const canonicalBodies = extractSectionBodies(docContent, [
    "canonical modules",
    "canonical families",
    "canonical learning units",
  ]);
  const supportingBodies = extractSectionBodies(docContent, [
    "supporting modules",
    "supporting guides",
    "supporting content",
  ]);

  return {
    canonical: canonicalBodies.flatMap((body) =>
      extractReferencedSlugs(body, trackId, topicId)
    ),
    supporting: supportingBodies.flatMap((body) =>
      extractReferencedSlugs(body, trackId, topicId)
    ),
  };
}
