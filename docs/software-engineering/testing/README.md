# Testing

This section is about verification strategies that keep code changes safe, especially when AI helps generate the code.

## Purpose

Use this page to organize testing into:
- fast local checks
- contract verification
- regression prevention
- nondeterminism control

## First Principles

- Testing should protect key invariants, not just increase line coverage.
- Fast and focused tests usually catch more useful regressions than large end-to-end suites alone.
- AI-generated code needs strong regression checks because the implementation can look plausible while violating contracts.
- Flaky tests destroy trust in the whole verification system.

## Canonical Modules

- `test-portfolio-in-practice`
- `contract-tests`
- `property-based-testing-basics`
- `golden-and-snapshot-test-tradeoffs`
- `flaky-test-reduction`
- `regression-tests-for-ai-generated-code`

## Supporting Modules

- `metamorphic-tests-for-generated-code`

## Math And Code

- Math level: `medium`
- Main quantitative objects: properties, distributions, flake rates, and threshold reasoning.
- Code shape: executable invariants through contract checks, regression cases, metamorphic relations, and focused failure reproduction.

## When To Use What

- Start with a practical test portfolio before expanding test types.
- Use contract tests at service and schema boundaries.
- Use property-based tests when inputs are wide and hand-picked examples miss edge cases.
- Use snapshot or golden tests only when output shape matters more than exact internal implementation.
