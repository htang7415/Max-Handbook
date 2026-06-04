# Frontend-Backend Shared Types

> Track: `software-engineering` | Topic: `typescript`

## Concept

Shared TypeScript types can reduce drift across frontend and backend code, but only when the boundary is versioned clearly and runtime validation still protects network inputs.

## Use When

| Signal | Shared Type Decision |
| --- | --- |
| Multiple clients consume the same contract | Share a versioned API type |
| UI needs only a subset | Expose a narrow projection |
| Network input is untrusted | Keep runtime validation |

## First Principles

- Shared packages do not eliminate API versioning.
- UI-facing projections should stay narrower than server storage records.
- Shared types help most when multiple clients consume the same stable contract.

## Workflow

1. Define the API contract separately from storage records.
2. Version the shared package or schema.
3. Project server data into UI-facing shapes.
4. Validate runtime input before trusting the shared type.

## Minimal Code Mental Model

```typescript
const card = toUserCard({
  id: "u_1",
  displayName: "Alex",
  role: "admin",
  version: 2,
});
const compatible = schemaVersionsCompatible(2, 2);
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Sharing database records | Storage changes leak into UI contracts |
| No versioning | Clients break on server changes |
| Type-only trust at network boundary | Invalid JSON reaches application logic |

## Function

```typescript
export function toUserCard(user: ApiUser): UserCard;
export function schemaVersionsCompatible(clientVersion: number, serverVersion: number): boolean;
export function shouldShareType(sharedConsumers: number, breakingChangesLastQuarter: number): boolean;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/frontend-backend-shared-types/typescript/test_frontend_backend_shared_types.ts
```
