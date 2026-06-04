# Engineering Handbook Style

This page defines the writing contract for Max Handbook. The goal is not brand imitation. The goal is an engineer-facing style: clear decisions, runnable checks, and concise explanations.

## Purpose

Use this standard when adding or revising handbook docs and modules.

Good pages help an engineer answer:
- What problem is this for?
- What boundary, invariant, or failure mode matters?
- What should I choose under real constraints?
- What is the smallest useful implementation?
- What test, eval, metric, or release gate proves it works?

## Style References

| Source | Useful habit to borrow | Handbook use |
| --- | --- | --- |
| Google DeepMind | Structured overviews, evidence, capability and safety framing | Use clear model/system boundaries, benchmark evidence, and release-risk language. |
| OpenAI | Eval workflows, datasets, graders, traces, and iteration loops | Treat behavior changes as measurable delivery changes. |
| Anthropic | Simple workflow patterns, explicit constraints, security and eval vocabulary | Prefer composable workflows before autonomous loops; state permission and failure boundaries. |
| Hugging Face | Quick starts, small code paths, API tables, task recipes | Make ML and agent concepts runnable and map them to practical library-shaped abstractions. |

## Page Contract

| Section | Required content | Keep it short by |
| --- | --- | --- |
| Purpose | One paragraph on the problem and audience | Avoid history unless it changes the engineering decision. |
| First Principles | The core invariant, boundary, or trade-off | Use bullets, not essays. |
| Decision Table | Choice, use case, signal, and failure mode | Compare only options the reader is likely to choose. |
| Workflow | Ordered steps for using the concept | Stop at the first reliable operating loop. |
| Minimal Code Mental Model | Tiny executable shape | Show the contract, not framework boilerplate. |
| Verification | Test, metric, eval, trace, or release check | Name the check and what it catches. |
| References | Source links when external systems are named | Prefer official docs, papers, or engineering posts. |

## Default Workflow

1. Frame the problem and the boundary.
2. Name the invariant or trade-off.
3. Choose the mechanism with a small decision table.
4. Build the smallest runnable version.
5. Verify with a focused test, eval, or metric.
6. Add operating checks only when deployment behavior matters.

## Tables

Use a table when the reader must compare three or more choices.

| Table type | Use for | Columns |
| --- | --- | --- |
| Decision | Choosing a method, metric, model, tool, or storage pattern | Option, use when, avoid when, signal |
| Failure | Debugging and production readiness | Failure, symptom, guard |
| Workflow | Ordered execution with gates | Step, action, output |
| Capability | Model, agent, or system boundary | Capability, requirement, evidence |

## Module Standard

Every module should make one idea executable.

| Module part | Requirement |
| --- | --- |
| `Concept` | One sentence that names the problem and mechanism. |
| `Use When` | A small table or bullets with the decision boundary. |
| `Minimal Code Mental Model` | One compact call path or formula-shaped implementation. |
| `Failure Modes` | The common way the idea breaks. |
| `Function` | Public functions the tests exercise. |
| `Run tests` | One target only, never the whole repo. |

## Writing Rules

- Prefer direct nouns and verbs.
- Keep paragraphs under four lines.
- Use bullets for scanability, but avoid long flat catalogs.
- Define acronyms the first time they matter.
- Use math only when it compresses a real decision.
- Use code only when it clarifies the implementation contract.
- Do not add a new module when an existing canonical family can absorb the idea.
- Do not cite labs as authority alone; cite them to explain a reusable engineering habit.

## Reference Links

- [Google DeepMind Model Cards](https://deepmind.google/models/model-cards)
- [OpenAI Evaluation Best Practices](https://platform.openai.com/docs/guides/evaluation-best-practices)
- [OpenAI Agent Evals](https://platform.openai.com/docs/guides/agent-evals)
- [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [Hugging Face Transformers Quickstart](https://huggingface.co/docs/transformers/quicktour)
