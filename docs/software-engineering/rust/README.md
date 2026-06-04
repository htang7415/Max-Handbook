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

## Decision Table

| Practice | Use when | Engineering signal |
| --- | --- | --- |
| Ownership at API boundaries | State lifetime or mutation must be explicit | The compiler enforces the ownership contract |
| Result error handling | Callers need recovery or observability context | Errors are typed and handled intentionally |
| Traits | Multiple implementations share a stable behavior contract | Abstraction is narrow and testable |
| Async Rust | I/O concurrency matters enough to manage runtime complexity | Cancellation and backpressure are explicit |
| Library tests | Invariants should be stable across refactors | Tests document behavior and failure paths |

## Workflow

| Step | Action | Output |
| --- | --- | --- |
| 1 | Name the state and ownership boundary | Borrowing or ownership contract |
| 2 | Define recoverable errors | Result type |
| 3 | Keep traits narrow until the boundary repeats | Minimal abstraction |
| 4 | Add async only when I/O shape justifies it | Runtime-aware service path |
| 5 | Test invariants through public APIs | Executable contract |

## Canonical Modules

- `result-error-handling`
- `ownership-at-api-boundaries`
- `traits-and-abstraction-boundaries`
- `async-rust-services`
- `testing-rust-libraries`

## Math And Code

- Math level: `low`
- Main quantitative objects: occasional service limits, resource budgets, or concurrency capacity.
- Code shape: ownership boundaries, explicit result types, narrow traits, async discipline, and invariant-driven tests.

## When To Use What

- Start with ownership and errors before async or advanced traits.
- Use Rust where control over state, memory, or concurrency matters enough to justify the extra precision.
- Keep abstractions narrow until the real boundary is stable.
- Treat tests as executable documentation for invariants, not just behavior checks.
