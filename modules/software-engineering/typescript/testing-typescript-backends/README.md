# Testing TypeScript Backends

> Track: `software-engineering` | Topic: `typescript`

## Concept

TypeScript backend handlers become easier to test when request parsing, pure decisions, and side effects are separated behind small typed seams.

## Use When

| Handler Shape | Test Layer |
| --- | --- |
| Pure decision logic exists | Unit test |
| Repository or clock dependency exists | Inject fake |
| Network contract is owned by another system | Contract test |

## First Principles

- A handler with hidden globals is harder to unit test no matter how good the types are.
- Fake repositories are useful when the contract is small and deterministic.
- Contract tests matter once the handler crosses a network-owned boundary.

## Workflow

1. Split request parsing, decisions, and side effects.
2. Inject repositories, clocks, and clients.
3. Unit test pure decision paths.
4. Add contract tests for network-owned boundaries.

## Minimal Code Mental Model

```typescript
const layers = recommendedTestLayers({
  hasDatabase: true,
  hasExternalHttp: true,
  pureDecisionSteps: 2,
});
const ready = handlerReadyForUnitTest(true, 0);
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Hidden globals | Tests need real environment state |
| Fake with a broad contract | Fake behavior drifts from production |
| No contract tests | Type-safe code can still violate wire behavior |

## Function

```typescript
export function recommendedTestLayers(shape: HandlerShape): string[];
export function fakeRepository<T extends { id: string }>(rows: T[]): Repository<T>;
export function handlerReadyForUnitTest(dependenciesInjected: boolean, hiddenGlobals: number): boolean;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/testing-typescript-backends/typescript/test_testing_typescript_backends.ts
```
