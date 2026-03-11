# System Design

This section is about choosing boundaries, state placement, and failure domains for systems that have to evolve.

## Purpose

Use this page to understand:
- requirements and tradeoffs
- service and storage boundaries
- background work and workflows
- consistency and failure-domain decisions

## First Principles

- Good system design starts with nonfunctional requirements, not component diagrams.
- Boundaries should make ownership, failure, and scaling easier to reason about.
- Stateful systems need explicit consistency and recovery rules.
- Architecture is mostly about choosing what can fail independently and what must stay coupled.

## Canonical Modules

- `requirements-and-failure-models`
- `service-boundaries-and-failure-domains`
- `stateless-vs-stateful-design`
- `storage-choice-basics`
- `background-jobs-and-workflows`
- `consistency-tradeoffs`

## Math And Code

- Math level: `medium`
- Main quantitative objects: capacity, fanout, tail latency, queue depth, storage cost, and consistency tradeoffs.
- Code shape: simulation-sized models of state placement, workflow coordination, storage choice, and boundary failure behavior.

## When To Use What

- Start here after the API, testing, reliability, and observability foundations are clear.
- Use service boundaries when they simplify ownership or failure isolation, not just to create more services.
- Use stateful designs only with explicit recovery and consistency reasoning.
- Treat workflows and job systems as part of architecture, not as afterthoughts.
