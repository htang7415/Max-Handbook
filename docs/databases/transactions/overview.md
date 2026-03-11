# Transactions, MVCC, And Concurrency

Transactions are how a database stays correct when many things happen at once.

## Purpose

Use this topic to learn how isolation, MVCC, retries, and locks protect correctness under concurrent reads and writes.

## First Principles

- A transaction defines which changes succeed or fail together.
- Isolation level is about the anomalies you allow, not a vague "safer is better" slider.
- MVCC lets readers and writers coexist by working with row versions instead of one global mutable state.
- Retries and idempotency are part of transaction design because failures and deadlocks are normal in real systems.

## Minimal Query Mental Model

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 50
WHERE id = 1;

UPDATE accounts
SET balance = balance + 50
WHERE id = 2;

COMMIT;
```

## Canonical Modules

- `transaction-basics`
- `isolation-levels-and-anomalies`
- `mvcc-mental-model`
- `optimistic-concurrency-control`
- `deadlocks-and-lock-ordering`
- `idempotent-writes-and-retries`
- `outbox-pattern`

## When To Use What

- Start with transaction basics, then map the real bug to an isolation level or anomaly.
- Use optimistic concurrency when conflicts are real but explicit locking would be too heavy.
- Use retries for transient conflicts and deadlocks, not as a substitute for missing invariants.
- Use the outbox pattern when database writes must drive downstream queues or events reliably.
