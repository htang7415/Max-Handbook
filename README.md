# Max Handbook

Max Handbook is a learning-first knowledge base for modern AI, software, and problem solving. The repository is the source of truth: concise notes live in `docs/`, runnable learning units live in `modules/`, and `web/` renders the same content.

Read the live handbook at [max-handbook.vercel.app](https://max-handbook.vercel.app/).

## GitHub Preview

GitHub cannot render the interactive site components, so the README shows static previews for two core ML concepts and links them to the live handbook.

<p align="center">
  <a href="https://max-handbook.vercel.app/track/ml/representation#embeddings">
    <img src="docs/assets/readme-embeddings-preview.svg" width="49%" alt="Embeddings preview" />
  </a>
  <a href="https://max-handbook.vercel.app/track/ml/llm#attention-mechanisms">
    <img src="docs/assets/readme-attention-preview.svg" width="49%" alt="Attention preview" />
  </a>
</p>

<p align="center">
  <a href="https://max-handbook.vercel.app/track/ml/representation#embeddings"><strong>Embeddings</strong></a>
  · Dense vectors for retrieval, ranking, and transfer
  <br/>
  <a href="https://max-handbook.vercel.app/track/ml/llm#attention-mechanisms"><strong>Attention</strong></a>
  · Weighted token-to-token context lookup inside transformer-style models
</p>

## What Knowledge Lives Here

| Track | Focus | Representative topics |
| --- | --- | --- |
| [DSA](docs/dsa) | Core algorithmic problem-solving patterns | arrays, strings, double pointers, stacks and queues, hash tables, binary trees, backtracking, dynamic programming, greedy, monotonic stack |
| [Machine Learning](docs/ml/README.md) | Modern ML from first principles to AI-era systems | math and stats, data preprocessing, classical models, evaluation, deep learning, LLMs, MLOps, systems, reinforcement learning, representation learning, computer vision |
| [AI Agents](docs/ai-agents/overview/README.md) | Building agent loops that can plan, act, recover, and be measured | prompting, tool use, RAG, memory, planning, workflows, observability, evaluation, guardrails, multi-agent coordination, capstones |
| [Databases](docs/databases/README.md) | Data modeling and data-system reasoning for product and AI workloads | relational design, schema design, SQL patterns, indexing, transactions, query plans, caching, streaming, NoSQL, vector retrieval |
| [Software Engineering](docs/software-engineering/README.md) | Production engineering for systems that must stay correct under change | tooling, APIs, testing, security, concurrency, observability, reliability, performance, system design, platform delivery, Python, Rust, TypeScript |

## How The Handbook Is Organized

```text
max-handbook/
  docs/          concise concept notes and section maps
  modules/       compact labs with code and focused tests
  web/           site renderer for the same source content
```

- `docs/` explains the concept map: what a topic is, why it matters, and how it connects to nearby topics.
- `modules/` turns that map into executable learning units with minimal code and small tests.
- `web/` publishes the same source material without becoming a second content system.

## Engineering Style Contract

The handbook is written for builders. Each page should help an engineer decide, implement, verify, and operate an idea.

| Page element | What it must answer |
| --- | --- |
| Purpose | What problem does this solve? |
| First principles | What invariant, boundary, or trade-off matters? |
| Decision table | When should an engineer choose one option over another? |
| Workflow | What order should the work happen in? |
| Minimal code | What is the smallest executable shape of the idea? |
| Verification | What test, eval, metric, or check proves it works? |

Use tables when comparing choices. Use workflows when order matters. Use code only when it makes the concept executable.

See [Engineering Handbook Style](docs/software-engineering/learning-paths/engineering-handbook-style.md) for the authoring standard.

## Current Knowledge Map

### DSA

The DSA track covers the standard problem-solving spine used to build algorithmic fluency: arrays, strings, pointers, hash tables, trees, backtracking, dynamic programming, greedy methods, and monotonic-stack reasoning.

### Machine Learning

The ML track covers the connected stack rather than isolated silos: fundamentals, data, models, evaluation, deep learning, LLMs, systems, MLOps, reinforcement learning, generative modeling, representation learning, and vision.

### AI Agents

The AI agents track focuses on how a model becomes a working system: prompt structure, tool calling, retrieval, memory, planning, workflow routing, observability, evaluation, and guardrails.

### Databases

The databases track covers the data layer behind modern applications and AI systems: relational modeling, schema evolution, SQL patterns, access paths, transaction behavior, streaming, caching, and retrieval-oriented storage.

### Software Engineering

The software-engineering track focuses on stable contracts, verification, failure handling, delivery safety, and operating discipline for systems built in an AI-assisted workflow.

## Learning Style

- Start from first principles: problem, invariant, trade-off.
- Prefer canonical modules over near-duplicate variants.
- Keep code minimal, typed where useful, and easy to inspect.
- Use tests, evals, metrics, or release checks to make ideas executable.
- Prefer short decision tables and workflows over long prose.
- Optimize for concise engineering judgment instead of exhaustive catalogs.

## License

[MIT](LICENSE)
