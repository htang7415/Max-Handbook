# Contributing

## Naming rules

- **Directories**: kebab-case (`prefix-sum`, `two-sum`, `binary-search`)
- **Python files**: snake_case (`prefix_sum.py`, `test_prefix_sum.py`)
- **Rust crates**: kebab-case directory, standard Rust naming inside

## Adding a module

A module teaches one concept with runnable code and tests.

```bash
./scripts/new_module.sh <track> <topic> <slug>
# Example: ./scripts/new_module.sh ml llm positional-encoding
```

This creates:

```
modules/<track>/<topic>/<slug>/
  README.md
  python/<slug_underscored>.py
  python/test_<slug_underscored>.py
```

Fill in the README with a concise explanation, implement the code, and write tests.

For DSA problem modules, prefer the reusable learning template in
`templates/dsa-problem/`. It adds recognition cues, baseline idea, core
insight, invariant/state, edge cases, common mistakes, and self-check prompts.
You can scaffold one with:

```bash
./scripts/new_dsa_problem.sh <topic> <slug> "<title>"
# Example: ./scripts/new_dsa_problem.sh array 704-binary-search "704.Binary Search"
```

## Testing

Run tests **one module at a time**:

```bash
# Python
pytest modules/<track>/<topic>/<slug>/python -q

# Rust
cargo test --manifest-path modules/<track>/<topic>/<slug>/rust/Cargo.toml
```

Use the Makefile shortcuts:

```bash
make run-py PATH=modules/dsa/arrays/prefix-sum/python
make run-rust MANIFEST=modules/dsa/arrays/prefix-sum/rust/Cargo.toml
```

## Code style

- Keep code minimal and readable
- Add concise comments only where logic is not self-evident
- Each module should be self-contained
- Keep one canonical solution per file; put alternate approaches in separate files
