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

## Canonical Modules

- `ai-assisted-dev-loop`
- `reproducible-dev-environments`
- `repo-layout-and-codegen-boundaries`
- `ci-pipeline-basics`
- `review-and-merge-discipline`

## Supporting Modules

- `spec-first-ai-coding`
- `generated-code-review-checklists`

## Math And Code

- Math here is lightweight and managerial: CI time budgets, review queue size, and risk-based gating rather than algorithm analysis.
- Code should express workflow rules directly: required spec sections, merge blockers, generated-code boundaries, and reproducible setup checks.

## When To Use What

- Start here before deeper system topics.
- Use reproducible environment modules before debugging flaky local setup.
- Make code generation boundaries explicit before generated files spread through the repo.
- Add AI workflow rules before relying on agents for large code edits.
