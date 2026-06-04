# RAG

RAG is the pattern where an agent retrieves outside knowledge and then answers using that retrieved context.

## Purpose

Use this page to understand:
- when retrieval is better than pure prompting
- how to select and pack evidence
- why grounded context should stay short

## First Principles

- Retrieval is useful when the answer depends on information not already in the prompt.
- The model only benefits from context that is both relevant and compact.
- Packing too many chunks can hurt just as much as retrieving too little.

## Concept Ladder

1. Retrieve candidate chunks.
2. Keep only the evidence that is relevant enough to use.
3. Pack a short grounded context.
4. Generate an answer that cites or depends on that context.
5. Check whether each important claim is supported.

## Engineering Boundary

This page is the RAG map. The runnable retrieve-pack loop lives in `rag-basics`; use the supporting modules when the problem is evidence coverage, citations, abstention, or post-answer grounding.

## Canonical Modules

- Main retrieval-to-answer loop: `rag-basics`

## Supporting Modules

- Abstaining or retrieving more when evidence coverage is weak: `retrieval-abstention-and-coverage`
- Grounding checks and citation coverage: `retrieval-quality-and-citations`
- Claim-level grounding checks after answer generation: `answer-grounding-checks`

## When To Use What

- Start with `rag-basics` when you need the simplest retrieve-then-answer workflow.
- Use `retrieval-abstention-and-coverage` when the main question is whether the retrieved evidence is strong enough to answer at all.
- Use `retrieval-quality-and-citations` when the answer needs explicit evidence coverage.
- Use `answer-grounding-checks` when the answer is already generated and you need to score whether each claim is actually supported.
- Keep chunk packing conservative before optimizing fancier reranking or fusion.
