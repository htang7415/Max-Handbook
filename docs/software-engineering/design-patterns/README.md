# Design Patterns

This section is about a small set of patterns that still clarify real systems in 2026.

## Purpose

Use this page to organize patterns into:
- boundary translation
- dependency control
- behavior selection
- explicit state

## First Principles

- Patterns are useful only when they remove ambiguity or repeated failure modes.
- Most software does not improve by collecting more abstractions.
- Prefer patterns that explain a boundary or control flow clearly in code review.
- If a pattern hides behavior, it is probably the wrong pattern for a learning-first repo.

## Canonical Modules

- `adapters-and-anti-corruption-layers`
- `dependency-injection-basics`
- `strategy-pattern-in-real-systems`
- `state-machine-basics`
- `composition-over-inheritance`

## Math And Code

- Math is usually minimal here; the important structure is behavioral shape, not formula depth.
- Code should show the boundary clearly: who owns the interface, what varies, and what stays invariant under the pattern.

## When To Use What

- Use adapters when integrating with an unstable or externally owned interface.
- Use dependency injection when testing and replacement of side effects matter.
- Use strategy when you need multiple policy choices behind one stable contract.
- Use explicit state machines when workflow correctness matters more than elegance.
