# Ownership At API Boundaries

> Track: `software-engineering` | Topic: `rust`

## Concept

Rust ownership becomes most useful at API boundaries because it makes borrowing, mutation, and consumption explicit to the caller.

## Use When

| API Need | Ownership Shape |
| --- | --- |
| Read without taking responsibility | Immutable borrow |
| Update caller-owned value | Mutable borrow |
| Take responsibility for value | Owned parameter |

## First Principles

- Borrowing lets callers inspect data without giving up ownership.
- Mutable borrowing makes in-place updates explicit.
- Consuming ownership is a signal that the API takes responsibility for the value.

## Workflow

1. Decide whether the callee reads, mutates, or consumes the value.
2. Pick `&T`, `&mut T`, or `T` to match that responsibility.
3. Keep ownership choices visible in public APIs.
4. Prefer the least ownership needed for the operation.

## Minimal Code Mental Model

```rust
let mut doc = Document::new("draft", "body");
assert_eq!(title_len(&doc), 5);
rename(&mut doc, "final");
let title = take_title(doc);
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Taking ownership only to read | Callers lose values unnecessarily |
| Mutating through hidden interior state | API responsibility is unclear |
| Cloning to avoid design | Performance and intent both suffer |

## Function

```rust
pub struct Document {
    pub title: String,
    pub body: String,
}

pub fn title_len(doc: &Document) -> usize;
pub fn rename(doc: &mut Document, new_title: &str);
pub fn take_title(doc: Document) -> String;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/ownership-at-api-boundaries/rust/Cargo.toml
```
