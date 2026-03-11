# 2026 Gap-Closure Roadmap

This roadmap closes the largest gaps between the current `ai-agents` track and a production-grade 2026 agent curriculum.

## Purpose

Use this page to decide what to add next and in what order:
- secure tool-using agents
- approval-gated execution
- named agent architectures
- production evaluation
- multimodal and connector-driven workflows

## First Principles

- Close control and safety gaps before adding more orchestration patterns.
- Add new modules only for distinct mental models, implementation patterns, or failure modes.
- Reuse adjacent `ml/llm` material when the gap is model-side math or evaluation, then add the agent-side workflow around it.
- Prefer modules that teach stable patterns that still matter across agent frameworks in 2026.

## Priority 1

- Add `prompt-injection-defense` under `guardrails`.
  Teach why retrieved text, tool output, web pages, and UI content are all untrusted inputs.
- Add `approval-gated-actions` under `guardrails`.
  Teach confirm / deny / edit loops before emails, purchases, destructive file changes, and other external side effects.
- Add `least-privilege-and-sandboxing` under `guardrails`.
  Teach narrow scopes, isolated execution, secret handling, and why risky tools should run with minimal permissions.
- Expand `computer-use` instead of splitting it.
  Add sensitive-action checkpoints, takeover mode, and unsafe-screen detection to the existing module.

## Priority 2

- Add `terminal-use` under `tool-use`.
  Teach shell planning, dry runs, parseable outputs, retries, and destructive-command policies.
- Expand `mcp` instead of keeping it as capability flags only.
  Cover client-host-server architecture, tools vs resources vs prompts, auth, sessions, and server lifecycle.
- Add `connectors-and-auth-scopes` under `tool-use`.
  Teach external app access, stale permissions, token scopes, and connector failure handling.
- Add `orchestrator-workers` under `multi-agent`.
  Teach a coordinator that assigns bounded subgoals to workers and merges structured results.
- Add `evaluator-optimizer-loops` under `workflows`.
  Teach generate-critique-revise loops and when they beat one-pass generation.

## Priority 3

- Expand `handoffs-and-routing` and `workflow-concurrency-basics` instead of adding duplicate routing modules.
  Pull in the named 2026 patterns: prompt chaining, routing, and parallel branches.
- Add `benchmark-harness-basics` under `evaluation`.
  Teach frozen task sets, baseline locking, task buckets, and regression suites for agents.
- Add `judge-and-trace-grading` under `evaluation`.
  Pull judge-based scoring into the agent track and connect it to step traces, not just final answers.
- Add `security-and-red-team-evals` under `evaluation`.
  Teach prompt-injection, exfiltration, privilege-escalation, and unsafe-action evals.
- Add `multimodal-agent-loops` under `workflows`.
  Teach agents that combine text with images, audio, or video before and after tool use.

## Cross-Track Integration

- Link `judge-and-trace-grading` to `modules/ml/llm/judge-evaluation-methods`.
- Link `benchmark-harness-basics` to `docs/ml/llm/evaluation` and `modules/ml/llm/reasoning-evaluation`.
- Link RAG improvements to `modules/ml/llm/retrieval-metrics`, `modules/ml/llm/bm25-ranking`, and `modules/ml/llm/retrieval-fusion-methods`.
- Link `multimodal-agent-loops` to `modules/ml/llm/multimodal-llms` and `modules/ml/llm/multimodal-evaluation`.
- Expand `prompt-structuring` and `memory-compaction` toward context engineering instead of creating a duplicate context-engineering topic.

## Suggested Build Order

1. `prompt-injection-defense`
2. `approval-gated-actions`
3. `least-privilege-and-sandboxing`
4. `terminal-use`
5. expanded `mcp`
6. `connectors-and-auth-scopes`
7. `orchestrator-workers`
8. `evaluator-optimizer-loops`
9. `benchmark-harness-basics`
10. `judge-and-trace-grading`
11. `security-and-red-team-evals`
12. `multimodal-agent-loops`

## When To Use What

- Follow Priority 1 before adding more autonomy to real tools or external systems.
- Follow Priority 2 when the repo is ready to teach production agent architectures instead of only single-loop basics.
- Follow Priority 3 when you need stronger evaluation, multimodal coverage, and clearer alignment with current agent practice.
- Keep routing, parallelization, judge metrics, and multimodal model math linked to existing modules when the core concept already exists elsewhere in the repo.
