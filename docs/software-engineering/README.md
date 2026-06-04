# Software Engineering

This track is about building software that stays correct when code is cheap, change is constant, and AI can generate implementations faster than humans can reason about consequences.

## Purpose

Use this track to learn the engineering responsibilities that still matter most in 2026:
- define stable contracts and invariants
- verify behavior before and after change
- handle state, latency, concurrency, and failure explicitly
- keep systems observable, secure, and operable
- use AI coding tools without giving up review discipline

## First Principles

- AI speeds up implementation. It does not remove the need for contracts, tests, or rollback paths.
- Most expensive bugs happen at boundaries: API boundaries, data boundaries, trust boundaries, and concurrency boundaries.
- Good engineering turns hidden assumptions into explicit schemas, thresholds, tests, alerts, and operating rules.
- Software quality is not just code quality. It also includes delivery safety, production behavior, and incident recovery.

## Frontier Lab Lessons

- OpenAI's structured-output and function-calling guidance reinforces contract-first engineering: schemas and tool outputs are runtime boundaries, not just prompt hints.
- Anthropic's Claude Code security model is a useful coding-agent pattern: read-only by default, explicit approval for edits and commands, sandboxing, and project-scoped write access.
- DeepMind's Frontier Safety Framework generalizes release engineering for powerful AI systems: identify capability thresholds, run early-warning evals, and require safety-case reviews for higher-risk deployments.
- Anthropic and OpenAI agent-eval guidance both turn traces, datasets, graders, and regression suites into normal software delivery artifacts.
- Hugging Face's agents course and evaluation material reinforce a practical engineering rule: systems should end in build, test, certify, share, and benchmark artifacts, not only explanations.

## How To Use This Track

- Start with `tooling`, `apis`, `testing`, and `security-basics`.
- Add `concurrency`, `observability`, `reliability`, and `performance` before going deep on `system-design`.
- Use `python`, `rust`, and `typescript` as implementation support, not as the main curriculum spine.
- Keep `design-patterns` secondary. Prefer patterns that clarify a real boundary or failure mode.
- Use `learning-paths` if you want a role-specific order instead of the full track order.
- Use `assessments` to check readiness before moving into capstones.
- Finish with `capstones` to combine contracts, tests, operations, and delivery decisions in one workflow.

## Module Authoring Rule

Each software-engineering module should answer the same six questions:
- What contract or invariant matters here?
- What usually fails?
- How do we test it?
- What do we monitor in production?
- What trust boundary exists?
- What changes when AI helps write the code?

## Math And Code Rule

- Math intensity should be explicit.
- `Low` math sections: `tooling`, `security-basics`, `design-patterns`, `python`, `rust`, `typescript`.
- `Medium` math sections: `apis`, `concurrency`, `testing`, `platform-and-delivery`, `system-design`, `capstones`.
- `High` math-for-software sections: `observability`, `reliability`, `performance`.
- Use math only when it clarifies an operational decision: rates, ratios, percentiles, error budgets, latency budgets, retry counts, queue depth, blast radius, or cost.
- Every module should have executable code that demonstrates the contract, invariant, threshold, or failure mode directly.
- Preferred code shapes are: boundary parsing, policy checks, threshold calculators, state transitions, retry/rollback logic, and small production-shaped workflows.
- Treat math as compression for reasoning and code as executable verification, not as separate learning tracks.

## Writing Shape

- Section docs should follow: `Purpose`, `First Principles`, `Canonical Modules`, optional `Supporting Modules`, `Math And Code`, `When To Use What`.
- Module docs should usually follow: `Concept`, `Key Points`, `Minimal Code Mental Model`, `Function`, `Run tests`.
- In section docs, `Math And Code` should usually answer three things in order: `Math level`, `Main quantitative objects`, `Code shape`.
- Add explicit math inside a module only when the topic genuinely needs a formula or threshold calculation.

## Handbook Subsections

1. Workflow and AI tooling: reproducible loops, codegen boundaries, CI, review, and AI-assisted delivery.
2. Contracts and APIs: schemas, compatibility, pagination, idempotency, retries, and webhooks.
3. Testing and verification: portfolios, contracts, properties, snapshots, flaky tests, and AI regressions.
4. Security and trust: authn/authz, validation, secrets, least privilege, supply chain, and agentic risk.
5. Concurrency and state: shared state, queues, idempotent consumers, cancellation, and state machines.
6. Observability and operations: logs, metrics, traces, SLOs, dashboards, runbooks, and debugging.
7. Reliability and delivery: retries, degradation, incidents, rollback, progressive delivery, and platforms.
8. Performance and cost: latency budgets, caching, profiling, batching, allocation, and trade-offs.
9. System design and patterns: requirements, boundaries, storage, statefulness, workflows, and practical patterns.
10. Implementation and practice: Python, Rust, TypeScript, learning paths, assessments, and capstones.

## Handbook Map Style

Each subsection should expose at most 20 curated subsubsections. Use this order:
- Frame the contract, invariant, boundary, or failure mode.
- Explain the engineering model or trade-off.
- Build the smallest production-shaped mechanism.
- Verify with tests, traces, metrics, or release checks.
- Operate with rollback, security, observability, and ownership.
- Finish with practice that leaves runnable artifacts.

## AI-Time 2026 Priorities

- Contract-first engineering over prompt-first engineering.
- Regression resistance for AI-generated changes.
- Observability and rollback before aggressive automation.
- Reliability rules for retries, queues, overload, and partial failure.
- Platform leverage that improves delivery speed without hiding ownership.
- Secure agentic workflows with least privilege, scoped credentials, approval gates, and traceable tool calls.
- Treat AI evals and red-team cases as release checks when software behavior depends on model or agent decisions.
- Treat supply-chain provenance, dependency risk, and generated-code review as normal delivery gates.

## First 20 Canonical Modules

Build the track in this order:

1. `ai-assisted-dev-loop`
2. `reproducible-dev-environments`
3. `repo-layout-and-codegen-boundaries`
4. `api-contract-basics`
5. `schema-evolution-and-compatibility`
6. `idempotency-keys`
7. `retries-timeouts-and-backoff`
8. `test-portfolio-in-practice`
9. `contract-tests`
10. `regression-tests-for-ai-generated-code`
11. `authn-vs-authz`
12. `least-privilege`
13. `race-conditions-and-shared-state`
14. `cancellation-deadlines-and-timeouts`
15. `logs-metrics-and-traces`
16. `slis-slos-and-alerting`
17. `graceful-degradation-and-overload`
18. `canary-rollout-and-rollback`
19. `latency-budgeting`
20. `service-boundaries-and-failure-domains`

## Scope Rule

- Prefer stable engineering principles over framework churn.
- Prefer compact modules with clear failure modes over long catalogs of tips.
- Prefer operationally meaningful topics over interview-style trivia.
- Treat AI as a workflow amplifier layered on top of software fundamentals, not as a replacement for them.

## Neighbor Tracks

- Use `docs/ai-agents/guardrails` when software workflows give agents external actions.
- Use `docs/databases/vector-db/overview.md` when AI product behavior depends on retrieval freshness or permissions.
- Use `docs/ml/llm/evaluation` when release gates depend on model or judge behavior.

## References

- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [OpenAI Function Calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Claude Code Security](https://code.claude.com/docs/en/security)
- [Google DeepMind Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en)
- [Hugging Face Agent Observability and Evaluation](https://huggingface.co/learn/agents-course/en/bonus-unit2/what-is-agent-observability-and-evaluation)

## Capstones

- `contract-to-production-api-service` is the first end-to-end capstone.
- `ai-assisted-feature-delivery` is the second capstone focused on spec, review, verification, and rollout discipline.
- `incident-recovery-drill` completes the initial capstone set with incident response and recovery workflow practice.
