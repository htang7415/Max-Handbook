# Async TypeScript Services

> Track: `software-engineering` | Topic: `typescript`

## Concept

Typed async services should make backpressure, deadlines, and failure shape explicit instead of returning unstructured promises that force every caller to guess.

## Use When

| Situation | Service Rule |
| --- | --- |
| More work may start than the service can handle | Check budget first |
| Deadline is caller-visible | Track remaining time explicitly |
| Calls can fail in expected ways | Return typed success and failure |

## First Principles

- Async code still needs typed success and failure paths.
- Backpressure should be decided before starting more work.
- Deadline math should stay explicit because timeout bugs are usually operational bugs.

## Workflow

1. Define the service result shape.
2. Check concurrency budget before starting work.
3. Carry deadline math through the call path.
4. Retry only when the typed result says the failure is retryable.

## Minimal Code Mental Model

```typescript
const budget = concurrencyBudget(4, 8);
const result = await callWithBudget(3, budget, async () => "ok");
const retry = shouldRetry(result);
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Unstructured rejected promises | Callers guess which failures are retryable |
| Starting work before budget checks | Backpressure arrives too late |
| Hidden timeout math | Operational bugs appear as random failures |

## Function

```typescript
export function concurrencyBudget(workers: number, perWorkerLimit: number): number;
export function deadlineRemaining(timeoutMs: number, elapsedMs: number): number;
export function shouldRetry<T>(result: ServiceResult<T>): boolean;
export async function callWithBudget<T>(
  inFlight: number,
  limit: number,
  task: () => Promise<T>,
): Promise<ServiceResult<T>>;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/async-typescript-services/typescript/test_async_typescript_services.ts
```
