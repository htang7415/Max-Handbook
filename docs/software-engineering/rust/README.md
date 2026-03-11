# Rust

This section is about using Rust for correctness, explicit failure handling, and predictable systems behavior.

## Purpose

Use this page to organize Rust engineering into:
- ownership at interfaces
- error handling
- abstraction boundaries
- async and testing

## First Principles

- Rust pushes correctness decisions earlier in the development loop.
- Ownership and borrowing become most useful at API and state boundaries.
- Explicit error types improve recovery and observability.
- Performance gains are strongest when memory and concurrency behavior are already understood.

## Canonical Modules

- `result-error-handling`
- `ownership-at-api-boundaries`
- `traits-and-abstraction-boundaries`
- `async-rust-services`
- `testing-rust-libraries`

## Math And Code

- Math is rarely the main subject here; use it only where service limits, resource budgets, or concurrency capacity matter.
- Code should focus on what Rust makes explicit: ownership, error types, abstraction boundaries, async discipline, and testable invariants.

## When To Use What

- Start with ownership and errors before async or advanced traits.
- Use Rust where control over state, memory, or concurrency matters enough to justify the extra precision.
- Keep abstractions narrow until the real boundary is stable.
- Treat tests as executable documentation for invariants, not just behavior checks.
