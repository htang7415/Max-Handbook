# Tooling

This section is about the development loop that turns changes into reviewed, reproducible, and shippable software.

## Purpose

Use this page to organize tooling into:
- local environment setup
- repo and code generation boundaries
- CI and release checks
- AI-assisted coding workflow
- review discipline

## First Principles

- A fast loop is only useful if it is reproducible.
- Generated code should have clear ownership boundaries.
- AI-generated code increases the need for review structure, not less.
- Tooling should reduce accidental variation in how code is built, tested, and shipped.
- Build and release automation should make provenance, dependency review, and generated-code boundaries visible to reviewers.
- Coding agents should run inside explicit permission, sandbox, and review boundaries; convenience modes are not substitutes for ownership or tests.

## Decision Table

| Tooling concern | Use when | Guard |
| --- | --- | --- |
| Reproducible environment | Local setup or CI differs across machines | One command produces the same baseline |
| Codegen boundary | Generated files can be edited or reviewed incorrectly | Ownership and regeneration path are explicit |
| CI pipeline | Checks must run before merge or release | Fast targeted checks block regressions |
| Review discipline | Change risk exceeds what tests can prove | Human review focuses on contract and failure modes |
| Spec-first AI coding | AI helps implement nontrivial changes | Acceptance checks exist before code generation |
| Generated-code checklist | AI or tools produce large diffs | Reviewers know what not to trust blindly |

## Workflow

| Step | Action | Output |
| --- | --- | --- |
| 1 | Make setup reproducible | Local and CI baseline |
| 2 | Mark generated and owned code paths | Review boundary |
| 3 | Define required checks by risk | CI gate |
| 4 | Use specs before AI-generated edits | Acceptance criteria |
| 5 | Review and merge with evidence | Traceable delivery decision |

## Canonical Modules

- `ai-assisted-dev-loop`
- `reproducible-dev-environments`
- `repo-layout-and-codegen-boundaries`
- `ci-pipeline-basics`
- `review-and-merge-discipline`

## Supporting Modules

- `spec-first-ai-coding`
- `generated-code-review-checklists`

## References

- [Claude Code Security](https://code.claude.com/docs/en/security)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)

## Math And Code

- Math level: `low`
- Main quantitative objects: CI time budgets, review queue size, and risk-based gating counts.
- Code shape: workflow rules such as required spec sections, merge blockers, generated-code boundaries, and reproducible setup checks.

## When To Use What

- Start here before deeper system topics.
- Use reproducible environment modules before debugging flaky local setup.
- Make code generation boundaries explicit before generated files spread through the repo.
- Add AI workflow rules before relying on agents for large code edits.
- Pair AI-assisted delivery with security-basics when generated changes touch dependencies, secrets, permissions, or external tool actions.
