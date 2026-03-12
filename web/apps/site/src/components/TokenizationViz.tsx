"use client";

import { useMemo, useState } from "react";

const EXAMPLES = [
  {
    label: "Prompting",
    text: "Summarize the retrieval logs for workspace seven before noon.",
  },
  {
    label: "Long word",
    text: "Tokenization changes how unbelievably long identifiers fit into context windows.",
  },
  {
    label: "Code-ish",
    text: "def score_prompt(prompt_text): return prompt_text.count('token')",
  },
] as const;

function characterTokens(text: string) {
  return Array.from(text).filter((char) => char.trim().length > 0);
}

function wordTokens(text: string) {
  return text.match(/[A-Za-z0-9_]+(?:'[A-Za-z0-9_]+)?|[^\sA-Za-z0-9_]/g) ?? [];
}

function subwordTokens(text: string) {
  return wordTokens(text).flatMap((token) => {
    if (!/[A-Za-z0-9_]/.test(token[0] ?? "")) {
      return [token];
    }
    if (token.length <= 6) {
      return [token];
    }

    const pieces = [token.slice(0, 4)];
    for (let index = 4; index < token.length; index += 3) {
      pieces.push(`##${token.slice(index, index + 3)}`);
    }
    return pieces;
  });
}

const TOKENIZERS = [
  {
    id: "character",
    label: "Character-like",
    description: "Small vocabulary, long sequences.",
    tokenize: characterTokens,
  },
  {
    id: "subword",
    label: "Subword-like",
    description: "Balanced vocabulary and length.",
    tokenize: subwordTokens,
  },
  {
    id: "word",
    label: "Word-like",
    description: "Short sequences, brittle on unseen words.",
    tokenize: wordTokens,
  },
] as const;

export default function TokenizationViz() {
  const [exampleIndex, setExampleIndex] = useState(0);
  const [budget, setBudget] = useState(18);

  const rows = useMemo(() => {
    const text = EXAMPLES[exampleIndex]?.text ?? "";
    return TOKENIZERS.map((tokenizer) => {
      const tokens = tokenizer.tokenize(text);
      return {
        ...tokenizer,
        tokens,
        count: tokens.length,
        attentionCost: tokens.length * tokens.length,
        fitsBudget: tokens.length <= budget,
      };
    });
  }, [budget, exampleIndex]);

  const maxCount = Math.max(...rows.map((row) => row.count), budget, 1);

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Tokenization Trade-Offs</div>
        <p className="observable-viz-subtitle">
          The same text can consume very different context budget depending on
          what the tokenizer treats as a unit.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Example</span>
          <select
            className="observable-control-select"
            value={exampleIndex}
            onChange={(event) => setExampleIndex(Number(event.target.value))}
          >
            {EXAMPLES.map((example, index) => (
              <option key={example.label} value={index}>
                {example.label}
              </option>
            ))}
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Token budget</span>
          <input
            className="observable-control-input"
            type="range"
            min="8"
            max="36"
            step="1"
            value={budget}
            onChange={(event) => setBudget(Number(event.target.value))}
          />
          <span className="observable-control-value">{budget}</span>
        </label>
      </div>

      <div className="token-viz-grid">
        {rows.map((row) => {
          const usage = Math.min((row.count / maxCount) * 100, 100);
          return (
            <section
              key={row.id}
              className={`token-viz-card token-viz-card-${row.id}`}
            >
              <div className="token-viz-card-header">
                <div>
                  <strong>{row.label}</strong>
                  <p>{row.description}</p>
                </div>
                <span
                  className={`token-viz-badge ${
                    row.fitsBudget ? "token-viz-badge-fit" : "token-viz-badge-over"
                  }`}
                >
                  {row.fitsBudget ? "Fits budget" : `+${row.count - budget} over`}
                </span>
              </div>

              <div className="token-viz-stats">
                <span>
                  <strong>{row.count}</strong>
                  tokens
                </span>
                <span>
                  <strong>{row.attentionCost}</strong>
                  n^2 attention
                </span>
              </div>

              <div className="token-viz-bar">
                <span style={{ width: `${usage}%` }} />
              </div>

              <div className="token-viz-chips">
                {row.tokens.map((token, index) => (
                  <span key={`${row.id}-${index}-${token}`} className="token-viz-chip">
                    {token}
                  </span>
                ))}
              </div>
            </section>
          );
        })}
      </div>
    </div>
  );
}
