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
- Agentic software needs trace, transcript, and final-state tests when the system changes state over several tool calls.
- Evaluation suites should include both quality benchmarks and regression checks, with human calibration when model graders are used.

## Canonical Modules

- `test-portfolio-in-practice`
- `contract-tests`
- `property-based-testing-basics`
- `golden-and-snapshot-test-tradeoffs`
- `flaky-test-reduction`
- `regression-tests-for-ai-generated-code`

## Supporting Modules

- `metamorphic-tests-for-generated-code`

## Frontier Lab Notes

- OpenAI trace grading and Anthropic agent evals both emphasize that final output is not enough for multi-step systems; test the trajectory and the environment outcome.
- DeepMind's frontier-safety process is a reminder to add early-warning cases for capabilities or behaviors that would change the release risk.
- Hugging Face's agent observability and evaluation guidance is a practical reminder to define success first, then combine automated metrics, traces, labels, and regression checks.

## References

- [OpenAI Trace Grading](https://developers.openai.com/api/docs/guides/trace-grading)
- [Anthropic Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Google DeepMind Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)
- [Hugging Face Agent Observability and Evaluation](https://huggingface.co/learn/agents-course/en/bonus-unit2/what-is-agent-observability-and-evaluation)

## Math And Code

- Math level: `medium`
- Main quantitative objects: properties, distributions, flake rates, and threshold reasoning.
- Code shape: executable invariants through contract checks, regression cases, metamorphic relations, and focused failure reproduction.

## When To Use What

- Start with a practical test portfolio before expanding test types.
- Use contract tests at service and schema boundaries.
- Use property-based tests when inputs are wide and hand-picked examples miss edge cases.
- Use snapshot or golden tests only when output shape matters more than exact internal implementation.
