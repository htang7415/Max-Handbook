# Prompting

Prompting is the layer that turns a raw user request into a structured input the model can reliably follow.

## Purpose

Use this page to understand:
- how to separate system instructions from user intent
- when to add explicit constraints
- how to keep prompts short and structured

## First Principles

- Good prompts reduce ambiguity before the model starts generating.
- System instructions define behavior; user messages define the task.
- Constraints are most useful when they are explicit and easy to check.

## Concept Ladder

1. Separate stable behavior from the user's current task.
2. Add only constraints that the model or evaluator can check.
3. Use examples and delimiters when format ambiguity causes errors.
4. Pack memory and retrieved context only when the task needs them.
5. Add self-checks after the prompt has a clear contract.

## Engineering Boundary

This page is the prompting map. The runnable message-building pattern lives in `prompt-structuring`; context packing belongs in `context-engineering-for-agents`.

## Canonical Modules

- Main structuring pattern: `prompt-structuring`

## Supporting Modules

- Few-shot examples and explicit delimiters: `examples-and-delimiters`
- Packing instructions, memory, and retrieval into one active prompt: `context-engineering-for-agents`
- Lightweight answer verification prompts: `self-check-patterns`

## When To Use What

- Start with `prompt-structuring` when the problem is basic message layout and instruction clarity.
- Use `context-engineering-for-agents` when the main problem is deciding which instructions, memory, and retrieved evidence should fit into the active prompt.
- Use `examples-and-delimiters` when the model needs a clearer output pattern or stronger separation between sections.
- Use `self-check-patterns` when the model should verify constraints before returning a final answer.
- Keep prompts short before adding more examples or scaffolding.
