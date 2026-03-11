# AI Agents

This section is about how an agent turns a goal into actions, keeps useful state, calls tools, and measures whether the workflow actually works.

## Purpose

Use this page to keep the agent stack in the right order:
- prompting and task framing
- tool use
- retrieval and memory
- planning and workflows
- observability, evaluation, and guardrails
- multi-agent coordination only when one loop is no longer enough

## First Principles

- An agent is not just a model. It is a loop around the model.
- Good agents keep only the state they need, use tools when text alone is not enough, and recover when steps fail.
- Most agent systems become easier to debug when planning, memory, tool use, and evaluation are separated.
- As systems grow, routing, latency, and risk decisions should become explicit scores, budgets, or thresholds instead of ad hoc prompt intuition.

## Core Math

- Success rate:
  $$
  \frac{\text{successful runs}}{\text{total runs}}
  $$
- Route or policy score:
  $$
  \text{value} - \text{cost} - \text{risk penalty}
  $$
- End-to-end latency:
  $$
  \sum_i \text{step latency}_i
  $$

## Minimal Code Mental Model

```python
prompt = build_prompt(goal, context)
call = tool_call("search_docs", {"query": goal})
memory = retrieve_relevant_memories(goal, notes, k=2)
plan = make_plan(goal, steps)
score = task_success_rate([True, False, True])
```

## Canonical Modules

- Prompt structure: `docs/ai-agents/prompting`
- Tool use: `docs/ai-agents/tool-use`
- Retrieval: `docs/ai-agents/rag`
- Memory: `docs/ai-agents/memory`
- Planning: `docs/ai-agents/planning`
- Workflows: `docs/ai-agents/workflows`
- Observability: `docs/ai-agents/observability`
- Evaluation: `docs/ai-agents/evaluation`
- Guardrails: `docs/ai-agents/guardrails`
- Multi-agent coordination: `docs/ai-agents/multi-agent`

## Supporting Docs

- Agent decision methods: `decision-methods`
- 2026 gap-closure roadmap: `roadmap-2026`

## When To Use What

- Start with prompting and one simple tool loop before adding more workflow structure.
- Add retrieval or memory only when the task depends on outside or prior context.
- Add planning and workflows when one free-form loop is no longer stable enough.
- Add observability once the agent is useful enough that failures need structured debugging.
- Add evaluation and guardrails before scaling usage, not after.
- Add multi-agent coordination only when role split is clearer than one stronger single-agent loop.
