# AI Agents

This section is about how an agent turns a goal into actions, keeps useful state, calls tools, and measures whether the workflow actually works.

## Purpose

Use this page to keep the agent stack in the right order:
- prompting and task framing
- tool use
- retrieval and memory
- planning and workflows
- tracing, evaluation, and guardrails
- assessments and capstone synthesis
- multi-agent coordination only when one loop is no longer enough

## First Principles

- An agent is not just a model. It is a loop around the model.
- Good agents keep only the state they need, use tools when text alone is not enough, and recover when steps fail.
- Most agent systems become easier to debug when planning, memory, tool use, and evaluation are separated.
- In 2026, useful agents need traces first, then repeatable eval datasets, then release gates.
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

## Handbook Subsections

1. Overview and architecture: agent loops, decision methods, and production priorities.
2. Prompting and context: instructions, examples, delimiters, and context engineering.
3. Tool use and MCP: structured tools, UI actions, terminal actions, connectors, and MCP.
4. Retrieval and memory: RAG, grounded answers, memory storage, retrieval, and compaction.
5. Planning and workflows: plans, routing, state machines, handoffs, retries, and concurrency.
6. Observability and tracing: spans, run analysis, sampling, dashboards, and root cause.
7. Evaluation and benchmarks: task success, trace grading, red-team evals, and release gates.
8. Guardrails and security: injection defense, approval gates, least privilege, and escalation.
9. Multi-agent systems: orchestration, workers, delegation budgets, arbitration, and roles.
10. Practice and capstones: assessments and end-to-end agent workflow builds.

## Supporting Guides

- Decision patterns: `decision-methods`
- 2026 production priorities: `roadmap-2026`

## When To Use What

- Start with prompting and one simple tool loop before adding more workflow structure.
- Add retrieval or memory only when the task depends on outside or prior context.
- Add planning and workflows when one free-form loop is no longer stable enough.
- Add tracing and observability as soon as tools or handoffs enter the loop.
- Add evaluation datasets and guardrails before scaling usage, not after.
- Use least privilege and approval gates whenever the agent can affect external systems.
- Use assessments to check whether your routing, risk, and metric choices are explicit enough.
- Start capstones only after the core single-agent loop is stable.
- Add multi-agent coordination only when role split is clearer than one stronger single-agent loop.
