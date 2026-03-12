"use client";

import { useMemo, useState } from "react";

function binomialCoefficient(n: number, k: number) {
  const effectiveK = Math.min(k, n - k);
  let result = 1;
  for (let index = 1; index <= effectiveK; index += 1) {
    result = (result * (n - effectiveK + index)) / index;
  }
  return result;
}

function bestOfN(success: number, samples: number) {
  return 1 - (1 - success) ** samples;
}

function majorityVote(success: number, samples: number) {
  let probability = 0;
  const threshold = Math.floor(samples / 2) + 1;
  for (let k = threshold; k <= samples; k += 1) {
    probability +=
      binomialCoefficient(samples, k) *
      success ** k *
      (1 - success) ** (samples - k);
  }
  return probability;
}

export default function ReasoningTestTimeComputeViz() {
  const [promptTokens, setPromptTokens] = useState(1200);
  const [reasoningTokens, setReasoningTokens] = useState(1600);
  const [answerTokens, setAnswerTokens] = useState(220);
  const [samples, setSamples] = useState(5);
  const [singleTrySuccess, setSingleTrySuccess] = useState(0.38);

  const summary = useMemo(() => {
    const totalTokens = samples * (promptTokens + reasoningTokens + answerTokens);
    const directTokens = promptTokens + answerTokens;
    const multiplier = totalTokens / directTokens;
    const best = bestOfN(singleTrySuccess, samples);
    const vote = majorityVote(singleTrySuccess, samples);
    const perTrace = promptTokens + reasoningTokens + answerTokens;
    return { totalTokens, multiplier, best, vote, perTrace };
  }, [answerTokens, promptTokens, reasoningTokens, samples, singleTrySuccess]);

  const perTrace = summary.perTrace || 1;

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Reasoning And Test-Time Compute</div>
        <p className="observable-viz-subtitle">
          Longer reasoning traces and more samples can improve quality, but every
          extra trace multiplies token cost and latency at inference time.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Prompt tokens</span>
          <input
            className="observable-control-input"
            type="range"
            min="400"
            max="2200"
            step="50"
            value={promptTokens}
            onChange={(event) => setPromptTokens(Number(event.target.value))}
          />
          <span className="observable-control-value">{promptTokens}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Reasoning tokens</span>
          <input
            className="observable-control-input"
            type="range"
            min="0"
            max="3200"
            step="100"
            value={reasoningTokens}
            onChange={(event) => setReasoningTokens(Number(event.target.value))}
          />
          <span className="observable-control-value">{reasoningTokens}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Answer tokens</span>
          <input
            className="observable-control-input"
            type="range"
            min="80"
            max="500"
            step="20"
            value={answerTokens}
            onChange={(event) => setAnswerTokens(Number(event.target.value))}
          />
          <span className="observable-control-value">{answerTokens}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Samples</span>
          <input
            className="observable-control-input"
            type="range"
            min="1"
            max="9"
            step="2"
            value={samples}
            onChange={(event) => setSamples(Number(event.target.value))}
          />
          <span className="observable-control-value">{samples}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Single-trace q</span>
          <input
            className="observable-control-input"
            type="range"
            min="0.1"
            max="0.9"
            step="0.02"
            value={singleTrySuccess}
            onChange={(event) => setSingleTrySuccess(Number(event.target.value))}
          />
          <span className="observable-control-value">{singleTrySuccess.toFixed(2)}</span>
        </label>
      </div>

      <div className="reasoning-viz-layout">
        <div className="reasoning-viz-card">
          <div className="reasoning-viz-title">Per-trace token composition</div>
          <div className="reasoning-viz-stack">
            <span
              className="reasoning-viz-stack-prompt"
              style={{ width: `${(promptTokens / perTrace) * 100}%` }}
            />
            <span
              className="reasoning-viz-stack-reasoning"
              style={{ width: `${(reasoningTokens / perTrace) * 100}%` }}
            />
            <span
              className="reasoning-viz-stack-answer"
              style={{ width: `${(answerTokens / perTrace) * 100}%` }}
            />
          </div>
          <div className="reasoning-viz-legend">
            <span><i className="reasoning-viz-legend-prompt" /> prompt</span>
            <span><i className="reasoning-viz-legend-reasoning" /> reasoning</span>
            <span><i className="reasoning-viz-legend-answer" /> answer</span>
          </div>
        </div>

        <div className="reasoning-viz-card">
          <div className="reasoning-viz-title">Quality wrappers over one trace</div>
          <div className="reasoning-viz-bars">
            <div className="reasoning-viz-bar-row">
              <span>Single trace</span>
              <div className="reasoning-viz-bar">
                <span style={{ width: `${singleTrySuccess * 100}%` }} />
              </div>
              <strong>{(singleTrySuccess * 100).toFixed(1)}%</strong>
            </div>
            <div className="reasoning-viz-bar-row">
              <span>Best-of-n</span>
              <div className="reasoning-viz-bar">
                <span
                  className="reasoning-viz-bar-best"
                  style={{ width: `${summary.best * 100}%` }}
                />
              </div>
              <strong>{(summary.best * 100).toFixed(1)}%</strong>
            </div>
            <div className="reasoning-viz-bar-row">
              <span>Majority vote</span>
              <div className="reasoning-viz-bar">
                <span
                  className="reasoning-viz-bar-vote"
                  style={{ width: `${summary.vote * 100}%` }}
                />
              </div>
              <strong>{(summary.vote * 100).toFixed(1)}%</strong>
            </div>
          </div>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Total tokens</span>
          <span className="observable-stat-value">{summary.totalTokens.toLocaleString()}</span>
        </div>
        <div className="observable-stat-row">
          <span>Multiplier</span>
          <span className="observable-stat-value">{summary.multiplier.toFixed(2)}x</span>
        </div>
        <div className="observable-stat-row">
          <span>Best-of-n</span>
          <span className="observable-stat-value">{summary.best.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Majority vote</span>
          <span className="observable-stat-value">{summary.vote.toFixed(2)}</span>
        </div>
      </div>
    </div>
  );
}
