# Result Error Handling

> Track: `software-engineering` | Topic: `rust`

## Concept

Rust error handling is strongest when failures are explicit in the type system and callers are forced to deal with them instead of relying on hidden exceptions.

## Use When

| Situation | Error Shape |
| --- | --- |
| Caller can recover or report the error | `Result` |
| Failure cases are known and small | Explicit enum |
| Failure should abort immediately | Panic only for programmer bugs |

## First Principles

- `Result` makes success and failure part of the function signature.
- Small, explicit error enums are easier to test and reason about.
- Propagating errors with `?` keeps code linear without hiding control flow.

## Workflow

1. Name the failure cases the caller should handle.
2. Encode them in a small error enum.
3. Return `Result` from fallible public functions.
4. Use `?` to propagate without hiding that failure is possible.

## Minimal Code Mental Model

```rust
let port = parse_port("8080")?;
let addr = bind_address("127.0.0.1", "8080")?;
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Stringly typed errors everywhere | Callers cannot match failure cases safely |
| Panic for user input | Recoverable failures crash the program |
| Huge shared error enum | Public API becomes noisy and imprecise |

## Function

```rust
pub enum ParsePortError {
    Empty,
    Invalid,
    OutOfRange,
    InvalidHost,
}

pub fn parse_port(input: &str) -> Result<u16, ParsePortError>;
pub fn bind_address(host: &str, port: &str) -> Result<String, ParsePortError>;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/result-error-handling/rust/Cargo.toml
```
