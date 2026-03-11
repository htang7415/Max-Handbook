# APIs

This section is about contracts between systems and how those contracts survive change.

## Purpose

Use this page to understand:
- request and response contracts
- compatibility over time
- safe mutation semantics
- retries, deadlines, and delivery failure

## First Principles

- API design is contract design, not route naming.
- Backward compatibility is a product decision encoded in schemas and error behavior.
- A retried request is normal production behavior, not an edge case.
- Mutating endpoints need explicit safety rules such as idempotency or conflict handling.

## Canonical Modules

- `api-contract-basics`
- `schema-evolution-and-compatibility`
- `idempotency-keys`
- `pagination-patterns`
- `retries-timeouts-and-backoff`
- `webhooks-and-signature-validation`

## Math And Code

- Math here is lightweight and operational: timeout budgets, retry counts, page sizes, rate limits, and success/failure ratios.
- Code should focus on schemas, request validation, compatibility checks, idempotency state, and retry behavior at the boundary.

## When To Use What

- Start with contract basics and compatibility before advanced transport concerns.
- Use idempotency for retried writes, queued work, and externally retried calls.
- Add pagination once response size and traversal order both matter.
- Treat webhooks as hostile network edges and validate sender authenticity explicitly.
