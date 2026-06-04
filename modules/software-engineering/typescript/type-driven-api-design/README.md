# Type-Driven API Design

> Track: `software-engineering` | Topic: `typescript`

## Concept

TypeScript is most useful at API boundaries when the request and response shapes make invalid states harder to represent in the first place.

## Use When

| API Need | Type Design Move |
| --- | --- |
| Stable request or response shape | Named type |
| Partial update | Narrow patch type |
| Unknown runtime value | Type guard or parser |

## First Principles

- The stable contract should be expressed as named types, not scattered object literals.
- Patch types should expose only fields that are actually mutable.
- Type guards help keep the runtime and the compile-time model aligned.

## Workflow

1. Name the request and response types.
2. Model invalid states as impossible where practical.
3. Create patch types from truly mutable fields.
4. Add type guards for values that cross runtime boundaries.

## Minimal Code Mental Model

```typescript
const updated = applyUserPatch(user, { displayName: "A. Lee", active: false });
const fields = updatableFields({ role: "editor", active: true });
const complete = isCompleteUserRecord(updated);
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Scattered object literals | API changes are hard to review |
| Patch type mirrors full record | Callers can update forbidden fields |
| No runtime guard | Static model diverges from actual inputs |

## Function

```typescript
export function applyUserPatch(user: UserRecord, patch: UserPatch): UserRecord;
export function updatableFields(patch: UserPatch): Array<keyof UserPatch>;
export function isCompleteUserRecord(value: Partial<UserRecord>): value is UserRecord;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/type-driven-api-design/typescript/test_type_driven_api_design.ts
```
