# 2026 Production Roadmap

This roadmap keeps the `ai-agents` track aligned with production-grade agent practice in 2026.

## Purpose

Use this page to decide what to strengthen next:
- trace-first debugging
- repeatable agent evals
- secure tool and connector use
- MCP and external app boundaries
- multimodal and multi-agent workflows only after the single-agent loop is stable

## First Principles

- Close control and safety gaps before adding more autonomy.
- Add new modules only for distinct mental models, implementation patterns, or failure modes.
- Reuse adjacent `ml/llm` material when the gap is model-side math or evaluation, then add the agent-side workflow around it.
- Prefer modules that teach stable patterns that still matter across agent frameworks in 2026.

## Current Priority Order

1. Trace every model call, tool call, handoff, guardrail decision, and external side effect.
2. Turn repeated traces into eval datasets with stable cases, buckets, and baseline gates.
3. Treat retrieved text, tool output, web pages, emails, and UI content as untrusted input.
4. Minimize tool functionality, permissions, and autonomy before adding more tools.
5. Use MCP as a standard integration boundary, not as a substitute for authorization or approval.
6. Add multi-agent coordination only when subgoals, permissions, and merge criteria are explicit.
7. Add multimodal loops only when the task genuinely needs image, audio, video, or screen state.

## Current Coverage

- Secure tool use: `prompt-injection-defense`, `approval-gated-actions`, `least-privilege-and-sandboxing`, `terminal-use`, `connectors-and-auth-scopes`, `mcp`
- Production evals: `benchmark-harness-basics`, `judge-and-trace-grading`, `security-and-red-team-evals`, `regression-checks`, `step-level-evaluation`
- Agent architecture: `handoffs-and-routing`, `workflow-concurrency-basics`, `orchestrator-workers`, `evaluator-optimizer-loops`
- Multimodal workflows: `multimodal-agent-loops`, with model-side links to `modules/ml/llm/multimodal-llms`

## Cross-Track Integration

- Link `judge-and-trace-grading` to `modules/ml/llm/judge-evaluation-methods`.
- Link `benchmark-harness-basics` to `docs/ml/llm/evaluation` and `modules/ml/llm/reasoning-evaluation`.
- Link RAG improvements to `modules/ml/llm/retrieval-metrics`, `modules/ml/llm/bm25-ranking`, and `modules/ml/llm/retrieval-fusion-methods`.
- Link `multimodal-agent-loops` to `modules/ml/llm/multimodal-llms` and `modules/ml/llm/multimodal-evaluation`.
- Expand `prompt-structuring` and `memory-compaction` toward context engineering instead of creating a duplicate context-engineering topic.

## Remaining Gaps

- Add more explicit security crosswalks from `guardrails` to OWASP LLM and agentic application risks.
- Expand `mcp` only when the added content teaches concrete server lifecycle, consent, OAuth, or trust-boundary behavior.
- Expand eval modules toward trace-level grading and dataset maintenance rather than adding narrow metric pages.
- Add connector examples only when they teach a new auth-scope, consent, or stale-permission failure mode.

## When To Use What

- Follow the priority order before adding more autonomy to real tools or external systems.
- Use the current coverage list to avoid duplicate modules with different names.
- Use remaining gaps for targeted expansions, not broad catalogs.
- Keep routing, parallelization, judge metrics, and multimodal model math linked to existing modules when the core concept already exists elsewhere in the repo.
