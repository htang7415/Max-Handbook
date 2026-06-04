# Tool Use

This section is about how an agent decides to call tools, how computer-use loops differ from ordinary API tools, and where MCP fits.

## Purpose

Use this page to keep tool-using agents in the right order:
- basic structured tool calls
- computer-use actions over a UI
- connector auth and scoped external access
- MCP as a standard way to expose tools, resources, and prompts

## First Principles

- Tool use is about deciding when the model should act outside pure text generation.
- Computer use is a special case where the agent acts over a changing interface instead of a fixed function API.
- MCP standardizes host-client-server integration for tools, resources, and prompts, but it is not a reasoning policy or an authorization system by itself.
- Good tool use needs structure, validation, and short feedback loops.
- Every tool surface should have an owner, a schema, a permission scope, a validation rule, and a failure path.

## Concept Ladder

1. Start with one typed function call.
2. Add result validation before using tool output as truth.
3. Add failure handling before retries become loops.
4. Add scopes, approval, and sandboxing before external side effects.
5. Add MCP when tool discovery and server lifecycle need a standard boundary.

## Engineering Boundary

This page is the tool-use map. The runnable select-call-result loop lives in `tool-use-basics`; decision math belongs in `expected-value-tool-selection` and security boundaries belong in `guardrails-and-security`.

## Current Standards Notes

- Treat MCP as a protocol boundary for tools, resources, prompts, and server lifecycle, not as a substitute for product policy.
- Current MCP practice should assume structured tool outputs, protected-resource metadata, resource indicators for OAuth safety, and explicit protocol-version handling for streamable HTTP clients.
- Tool results that include resources or external content still need validation before they can influence later tool calls.
- OpenAI and Anthropic both emphasize typed tool definitions, explicit tool outputs, and traceable tool calls; tool documentation should be treated like API design, not prompt decoration.
- Anthropic's MCP donation to the Linux Foundation's Agentic AI Foundation makes MCP a vendor-neutral ecosystem standard, so handbook content should teach protocol boundaries rather than provider-specific connector habits.

## Canonical Modules

- Core function calling: `tool-use-basics`
- UI action loops: `computer-use`
- Standardized tool and resource exposure: `mcp`
- External app scopes and auth refresh: `connectors-and-auth-scopes`

## Supporting Modules

- Shell-based execution with dry-run and review rules: `terminal-use`
- Adaptive tool choice with exploration vs exploitation tradeoffs: `bandit-style-exploration-exploitation`
- Utility-style ranking of tools by upside, cost, and failure downside: `expected-value-tool-selection`
- Validation of tool results before reuse: `tool-result-validation`
- Recovery decisions after tool failure: `tool-failure-handling`
- Choosing the best tool before calling it: `tool-selection-heuristics`
- Normalizing tool arguments before execution: `tool-argument-normalization`
- Matching requested arguments to the right tool schema: `tool-schema-matching`

## References

- [OpenAI Function Calling](https://developers.openai.com/api/docs/guides/function-calling)
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Anthropic MCP Donation and AAIF](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)

## When To Use What

- Start with `tool-use-basics` when the problem is ordinary function calling.
- Use `computer-use` when the agent must click, type, scroll, or inspect a live interface and risky screens may need checkpoints or takeover.
- Use `terminal-use` when the agent must inspect files, run commands, or operate through a shell instead of a GUI.
- Use `bandit-style-exploration-exploitation` when repeated tool choices should adapt from observed rewards instead of fixed heuristics only.
- Use `connectors-and-auth-scopes` when the agent talks to email, calendar, docs, CRM, or other external apps and must keep scopes narrow and sessions fresh.
- Use `expected-value-tool-selection` when the choice should reflect likely upside, execution cost, and failure downside rather than keywords alone.
- Use `mcp` when tools, resources, and prompts need a standard server-style interface with discovery, auth, and session-aware access instead of one-off adapters.
- Use `tool-result-validation` when tool outputs must be checked for schema shape, missing fields, or obvious execution errors.
- Use `tool-failure-handling` when the agent needs a simple retry / fallback / escalate decision after a tool call fails.
- Use `tool-selection-heuristics` when the main challenge is picking the right tool from several plausible options.
- Use `tool-argument-normalization` when inputs need basic cleanup or default filling before the tool call.
- Use `tool-schema-matching` when several tools look similar and the main question is which schema best fits the requested arguments.
- Pair tool use with `prompt-injection-defense`, `approval-gated-actions`, and `least-privilege-and-sandboxing` when tool output or external content can influence later actions.
