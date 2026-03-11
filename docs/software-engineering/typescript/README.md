# TypeScript

This section is about using types to keep web and backend systems honest across changing interfaces.

## Purpose

Use this page to organize TypeScript engineering into:
- type-driven interfaces
- runtime validation
- async backend behavior
- testing across client and server boundaries

## First Principles

- Static types help most when data crosses boundaries.
- Compile-time safety is not enough for untrusted runtime data.
- Shared types are useful only when ownership and versioning stay clear.
- TypeScript should clarify contracts, not turn every file into type-level metaprogramming.

## Canonical Modules

- `type-driven-api-design`
- `runtime-validation`
- `async-typescript-services`
- `testing-typescript-backends`
- `frontend-backend-shared-types`

## Math And Code

- Math is usually secondary here; keep it for capacity, timeout, or threshold reasoning where the service behavior depends on numbers.
- Code should emphasize what TypeScript is best at in this track: boundary types, runtime validation, async result shape, and shared-contract discipline.

## When To Use What

- Start with type-driven interfaces and runtime validation before advanced type tricks.
- Use runtime validation for all external or persisted data.
- Share types only when the boundary and release process can support it.
- Keep examples biased toward service and app code, not puzzle-style type programming.
