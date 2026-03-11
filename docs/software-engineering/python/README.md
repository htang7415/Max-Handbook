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
