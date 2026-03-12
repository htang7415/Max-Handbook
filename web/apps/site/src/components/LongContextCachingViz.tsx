"use client";

import { useMemo, useState } from "react";

function quadraticPairs(length: number) {
  return length * length;
}

export default function LongContextCachingViz() {
  const [promptTokens, setPromptTokens] = useState(64000);
  const [cachedPrefix, setCachedPrefix] = useState(48000);
  const [repeatedRequests, setRepeatedRequests] = useState(6);
  const [contextWindow, setContextWindow] = useState(128000);

  const summary = useMemo(() => {
    const cached = Math.min(cachedPrefix, promptTokens);
    const effectivePrompt = promptTokens - cached;
    const hitRate = promptTokens === 0 ? 0 : cached / promptTokens;
    const utilization = promptTokens / contextWindow;
    const savedTokens = cached * Math.max(0, repeatedRequests - 1);
    const beforePairs = quadraticPairs(promptTokens);
    const afterPairs = quadraticPairs(effectivePrompt);
    return {
      cached,
      effectivePrompt,
      hitRate,
      utilization,
      savedTokens,
      beforePairs,
      afterPairs,
    };
  }, [cachedPrefix, contextWindow, promptTokens, repeatedRequests]);

  const pairScale = Math.max(summary.beforePairs, 1);

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Long Context And Caching</div>
        <p className="observable-viz-subtitle">
          Long prompts increase prefill cost quickly. Shared cached prefixes reduce
          fresh prompt work and compound savings across repeated requests.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Prompt tokens</span>
          <input
            className="observable-control-input"
            type="range"
            min="8000"
            max="128000"
            step="4000"
            value={promptTokens}
            onChange={(event) => setPromptTokens(Number(event.target.value))}
          />
          <span className="observable-control-value">{Math.round(promptTokens / 1000)}k</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Cached prefix</span>
          <input
            className="observable-control-input"
            type="range"
            min="0"
            max={String(promptTokens)}
            step="4000"
            value={Math.min(cachedPrefix, promptTokens)}
            onChange={(event) => setCachedPrefix(Number(event.target.value))}
          />
          <span className="observable-control-value">{Math.round(summary.cached / 1000)}k</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Repeated reqs</span>
          <input
            className="observable-control-input"
            type="range"
            min="1"
            max="12"
            step="1"
            value={repeatedRequests}
            onChange={(event) => setRepeatedRequests(Number(event.target.value))}
          />
          <span className="observable-control-value">{repeatedRequests}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Context window</span>
          <input
            className="observable-control-input"
            type="range"
            min="32000"
            max="256000"
            step="8000"
            value={contextWindow}
            onChange={(event) => setContextWindow(Number(event.target.value))}
          />
          <span className="observable-control-value">{Math.round(contextWindow / 1000)}k</span>
        </label>
      </div>

      <div className="context-viz-layout">
        <div className="context-viz-card">
          <div className="context-viz-card-title">Prompt work before / after cache</div>
          <div className="context-viz-bars">
            <div className="context-viz-bar-row">
              <span>Before</span>
              <div className="context-viz-bar">
                <span
                  className="context-viz-bar-before"
                  style={{ width: `${(summary.beforePairs / pairScale) * 100}%` }}
                />
              </div>
              <strong>{(summary.beforePairs / 1_000_000).toFixed(1)}M</strong>
            </div>
            <div className="context-viz-bar-row">
              <span>After</span>
              <div className="context-viz-bar">
                <span
                  className="context-viz-bar-after"
                  style={{ width: `${(summary.afterPairs / pairScale) * 100}%` }}
                />
              </div>
              <strong>{(summary.afterPairs / 1_000_000).toFixed(1)}M</strong>
            </div>
          </div>
        </div>

        <div className="context-viz-card">
          <div className="context-viz-card-title">Prompt composition</div>
          <div className="context-viz-stack">
            <span
              className="context-viz-stack-cached"
              style={{ width: `${summary.hitRate * 100}%` }}
            />
            <span
              className="context-viz-stack-fresh"
              style={{ width: `${(1 - summary.hitRate) * 100}%` }}
            />
          </div>
          <div className="context-viz-legend">
            <span><i className="context-viz-legend-cached" /> cached prefix</span>
            <span><i className="context-viz-legend-fresh" /> fresh prefill</span>
          </div>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Effective prompt</span>
          <span className="observable-stat-value">{summary.effectivePrompt.toLocaleString()}</span>
        </div>
        <div className="observable-stat-row">
          <span>Cache hit rate</span>
          <span className="observable-stat-value">{(summary.hitRate * 100).toFixed(1)}%</span>
        </div>
        <div className="observable-stat-row">
          <span>Saved tokens</span>
          <span className="observable-stat-value">{summary.savedTokens.toLocaleString()}</span>
        </div>
        <div className="observable-stat-row">
          <span>Utilization</span>
          <span className="observable-stat-value">{(summary.utilization * 100).toFixed(1)}%</span>
        </div>
      </div>
    </div>
  );
}
