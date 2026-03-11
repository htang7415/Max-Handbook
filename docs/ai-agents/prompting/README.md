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

## Core Math

- Active prompt budget:
  $$
  \text{system} + \text{task} + \text{memory} + \text{retrieved context} \le \text{context window}
  $$
- Constraint coverage:
  $$
  \frac{\text{satisfied constraints}}{\text{required constraints}}
  $$

## Minimal Code Mental Model

```python
checklist = format_checklist(["answer in bullets", "cite sources"])
messages = build_messages(
    system_prompt="You are a careful research assistant.",
    user_prompt="Summarize the latest policy changes.",
    checklist=["answer in bullets", "cite sources"],
)
```

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
