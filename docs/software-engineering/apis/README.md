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

## Decision Table

| Concern | Use when | Engineering signal |
| --- | --- | --- |
| Contract basics | A caller depends on request, response, or error shape | Schema, status codes, and examples are stable enough to test |
| Compatibility | Existing clients must survive a change | Old payloads still parse and old behavior still has a defined path |
| Idempotency | Writes can be retried, duplicated, or queued | The same logical request has one durable outcome |
| Pagination | Responses can grow without bound | Ordering, cursor shape, and page size are explicit |
| Retry and timeout policy | Calls cross a network or dependency boundary | Deadlines, retry count, and overload behavior are bounded |
| Webhook validation | External systems call back into your service | Sender identity and payload integrity are verified |

## Workflow

| Step | Action | Output |
| --- | --- | --- |
| 1 | Define the resource, operation, and caller contract | Request, response, error, and ownership boundary |
| 2 | Decide compatibility and versioning rules | Allowed changes and blocked changes |
| 3 | Add mutation safety | Idempotency key, conflict rule, or state transition |
| 4 | Bound production behavior | Timeout, retry, pagination, and rate-limit policy |
| 5 | Verify the boundary | Contract tests and compatibility fixtures |

## Canonical Modules

- `api-contract-basics`
- `schema-evolution-and-compatibility`
- `idempotency-keys`
- `pagination-patterns`
- `retries-timeouts-and-backoff`
- `webhooks-and-signature-validation`

## Math And Code

- Math level: `medium`
- Main quantitative objects: timeout budgets, retry counts, page sizes, rate limits, and success/failure ratios.
- Code shape: boundary validators, schema compatibility checks, idempotency state, pagination rules, and retry policy helpers.

## When To Use What

- Start with contract basics and compatibility before advanced transport concerns.
- Use idempotency for retried writes, queued work, and externally retried calls.
- Add pagination once response size and traversal order both matter.
- Treat webhooks as hostile network edges and validate sender authenticity explicitly.
