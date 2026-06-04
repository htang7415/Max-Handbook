# Traits And Abstraction Boundaries

> Track: `software-engineering` | Topic: `rust`

## Concept

Traits define the behavior a caller needs while letting implementations vary behind a narrow boundary.

## Use When

| Need | Trait Choice |
| --- | --- |
| Compile-time dispatch | Generic bound |
| Runtime list of implementations | Trait object |
| Many unrelated methods | Split the trait |

## First Principles

- Traits are most useful when the boundary is stable and the implementations vary.
- Generic functions and trait objects solve related but different abstraction needs.
- Narrow traits are easier to test and reuse than broad interfaces.

## Workflow

1. Define the behavior the caller needs.
2. Keep the trait narrow and stable.
3. Choose generics for compile-time dispatch.
4. Choose trait objects when runtime heterogeneity matters.

## Minimal Code Mental Model

```rust
let upper = UppercaseFormatter;
assert_eq!(render(&upper, "hi"), "HI");
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Trait before variation exists | Extra abstraction without a caller need |
| Broad trait | Implementations depend on methods they do not use |
| Wrong dispatch shape | API becomes harder to call or store |

## Function

```rust
pub trait Formatter {
    fn format(&self, input: &str) -> String;
}

pub fn render<F: Formatter>(formatter: &F, input: &str) -> String;
pub fn render_all(formatters: &[&dyn Formatter], input: &str) -> Vec<String>;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/traits-and-abstraction-boundaries/rust/Cargo.toml
```
