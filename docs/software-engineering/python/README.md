# Python

This section is about writing Python that remains maintainable in real services, tools, and data-heavy systems.

## Purpose

Use this page to organize Python engineering into:
- project structure and packaging
- typing and interfaces
- async services
- testing and profiling

## First Principles

- Python scales best when interfaces and data shapes are made explicit.
- Type hints are communication tools as much as checker inputs.
- Async code increases throughput only when the I/O model actually matches it.
- Python performance work usually begins with measuring object, allocation, and serialization costs.

## Decision Table

| Practice | Use when | Engineering signal |
| --- | --- | --- |
| Project layout | Code will be imported, tested, packaged, or deployed | Imports and ownership are predictable |
| Typing | Data crosses module or service boundaries | Interfaces are reviewable before runtime |
| Async services | Work is I/O-bound and concurrent | Throughput improves without hiding cancellation |
| Service tests | Behavior depends on boundaries or side effects | Tests cover contracts, not only helpers |
| Profiling | Runtime cost affects latency or spend | Bottleneck evidence exists before optimization |

## Workflow

| Step | Action | Output |
| --- | --- | --- |
| 1 | Set package and import boundaries | Project shape |
| 2 | Type the public data and service contracts | Interface documentation |
| 3 | Add runtime checks where inputs are untrusted | Boundary validation |
| 4 | Test service behavior through public calls | Focused regression suite |
| 5 | Profile before performance rewrites | Measured bottleneck |

## Canonical Modules

- `typing-for-large-python-codebases`
- `async-python-services`
- `packaging-and-project-layout`
- `testing-python-services`
- `profiling-python`

## Math And Code

- Math level: `low`
- Main quantitative objects: occasional timeout, profiling, or service-limit measurements.
- Code shape: explicit interfaces, async service boundaries, typing discipline, and measurable Python runtime behavior.

## When To Use What

- Start with project layout and typing before advanced async patterns.
- Use async for I/O-heavy services, not as a default for every codebase.
- Add profiling before replacing simple Python with lower-level code.
- Keep Python examples small but production-shaped.
