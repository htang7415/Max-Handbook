# Workflows

This section is about how an agent routes tasks, hands state to another step or worker, and decides when to retry.

## Purpose

Use this page to understand:
- routing to the right worker
- structured handoffs
- bounded retries

## First Principles

- Workflows matter when one free-form agent loop is not enough.
- Routing should depend on task type, not on vague prompt wording alone.
- Handoffs should pass compact structured state, not the entire raw transcript.
- Retries should be limited and explicit.

## Minimal Code Mental Model

```python
route = route_task("summarize docs and file a ticket", routes)
handoff = build_handoff("task_7", route, {"doc_id": "abc"})
retry = should_retry(attempt=1, max_attempts=3, retryable=True)
```

## Canonical Modules

- Routing and handoff basics: `handoffs-and-routing`
- Retry and fallback basics: `retries-and-recovery`

## Supporting Modules

- Escalation routing after failed or risky steps: `escalation-routing`
- Critique-and-revise loops for improving a draft: `evaluator-optimizer-loops`
- Explicit latency budgets across multi-step runs: `latency-budget-accounting`
- Multimodal execution routing over text, image, audio, or video inputs: `multimodal-agent-loops`
- Sequential stage-to-stage prompting with explicit outputs: `prompt-chaining`
- Bayesian route ranking from observed success/failure evidence: `posterior-routing`
- Weighted route selection from explicit signals: `routing-scorecards`
- Runtime route choice with entropy and ambiguity checks: `uncertainty-aware-routing`
- Low-latency turn routing for voice and streaming sessions: `voice-and-realtime-agent-loops`
- Explicit state transitions for multi-step runs: `state-machine-basics`
- Parallel branches and join points in a workflow: `workflow-concurrency-basics`

## When To Use What

- Start with `handoffs-and-routing` when the agent needs more than one specialized step.
- Use `retries-and-recovery` when steps can fail transiently and need bounded retries or a safe fallback.
- Use `escalation-routing` when failures need a structured handoff to review instead of another retry.
- Use `evaluator-optimizer-loops` when one pass produces a draft that should be critiqued and revised instead of simply retried.
- Use `latency-budget-accounting` when response time needs an explicit total budget, per-step split, and overrun route.
- Use `multimodal-agent-loops` when the workflow must check required modalities, possibly call tools over them, and only then answer or escalate.
- Use `prompt-chaining` when one stage should transform output for the next stage instead of handing the whole task to one prompt.
- Use `posterior-routing` when repeated route outcomes should update route choice from observed evidence rather than fixed priors alone.
- Use `routing-scorecards` when route choice should come from weighted task, tool, and latency signals instead of loose keyword heuristics.
- Use `uncertainty-aware-routing` when a top route exists but the system still needs a quantitative check for ambiguity or low confidence before acting.
- Use `voice-and-realtime-agent-loops` when the workflow must handle streaming input, interruptions, or realtime response budgets.
- Use `state-machine-basics` when the workflow has a small fixed set of stages and transitions.
- Use `workflow-concurrency-basics` when independent steps can run in parallel and later join.
- Add more workflow depth only after the baseline route and handoff state are stable.
