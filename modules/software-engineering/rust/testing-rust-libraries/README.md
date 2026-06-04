# Testing Rust Libraries

> Track: `software-engineering` | Topic: `rust`

## Concept

Rust libraries are easiest to test when most logic is pure, boundaries are injectable, and the crate exposes small deterministic functions.

## Use When

| Code Shape | Test Scope |
| --- | --- |
| Pure function | Unit test |
| Boundary with I/O | Integration test or injected fake |
| Hidden global state | Refactor before relying on tests |

## First Principles

- Pure functions are cheap to unit test.
- Hidden global state makes libraries harder to reason about and harder to isolate.
- Integration tests are strongest when the library surface is already clean.

## Workflow

1. Push deterministic logic into small functions.
2. Keep I/O behind explicit boundaries.
3. Test pure logic directly.
4. Add integration tests for the public crate behavior.

## Minimal Code Mental Model

```rust
assert_eq!(normalize_slug("Hello, Rust!"), "hello-rust");
assert_eq!(test_scope(true, false), "integration");
assert!(library_ready_for_unit_tests(0, 1));
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Hidden globals | Tests depend on order or environment |
| Only integration tests | Small logic bugs are harder to locate |
| Public surface too broad | Tests lock in accidental behavior |

## Function

```rust
pub fn normalize_slug(input: &str) -> String;
pub fn test_scope(has_io: bool, pure_logic: bool) -> &'static str;
pub fn library_ready_for_unit_tests(hidden_globals: usize, injectable_boundaries: usize) -> bool;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/testing-rust-libraries/rust/Cargo.toml
```
