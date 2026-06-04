# Runtime Validation

> Track: `software-engineering` | Topic: `typescript`

## Concept

TypeScript types disappear at runtime, so untrusted data still needs explicit validation before it crosses into trusted application code.

## Use When

| Input Source | Validation Need |
| --- | --- |
| HTTP request body | Validate before handler logic |
| Queue payload | Validate before processing side effects |
| Database document with loose schema | Validate before trusted use |

## First Principles

- Compile-time safety does not validate JSON from a request, queue, or database.
- Runtime validation should report concrete errors instead of failing later in business logic.
- Parse at the boundary, then use the validated type internally.

## Workflow

1. Treat unknown input as `unknown`.
2. Validate required fields and value ranges at the boundary.
3. Return concrete validation errors.
4. Pass only validated types into business logic.

## Minimal Code Mental Model

```typescript
const errors = validationErrors(input);
const valid = isPaymentRequest(input);
const request = parsePaymentRequest(input);
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Casting with `as` | Invalid data gets a trusted type |
| Late validation | Side effects may happen before errors surface |
| Generic error messages | Callers cannot fix malformed input |

## Function

```typescript
export function validationErrors(input: unknown): string[];
export function isPaymentRequest(input: unknown): input is PaymentRequest;
export function parsePaymentRequest(input: unknown): PaymentRequest;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/runtime-validation/typescript/test_runtime_validation.ts
```
