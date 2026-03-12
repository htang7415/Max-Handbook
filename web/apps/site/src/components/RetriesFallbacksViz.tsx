"use client";

import { useMemo, useState } from "react";

const TRANSIENT_ERRORS = ["timeout", "rate_limit", "temporary_unavailable"] as const;
const ALL_ERRORS = [...TRANSIENT_ERRORS, "validation_error"] as const;
const PRIMARY_PATHS = [
  "live-recommendations",
  "semantic-search",
  "llm-summary",
] as const;

function retryAction(
  errorType: string,
  attempt: number,
  maxAttempts: number,
  idempotent: boolean
) {
  if (TRANSIENT_ERRORS.includes(errorType as (typeof TRANSIENT_ERRORS)[number]) && idempotent && attempt < maxAttempts) {
    return "retry";
  }
  if (TRANSIENT_ERRORS.includes(errorType as (typeof TRANSIENT_ERRORS)[number])) {
    return "fallback";
  }
  return "fail-fast";
}

function retryDelay(baseDelayMs: number, attempt: number, maxDelayMs: number) {
  return Math.min(maxDelayMs, baseDelayMs * 2 ** attempt);
}

function fallbackTarget(primaryPath: string) {
  const map: Record<string, string> = {
    "live-recommendations": "cached-recommendations",
    "semantic-search": "keyword-search",
    "llm-summary": "template-summary",
  };
  return map[primaryPath] ?? "none";
}

export default function RetriesFallbacksViz() {
  const [errorType, setErrorType] = useState<(typeof ALL_ERRORS)[number]>("timeout");
  const [primaryPath, setPrimaryPath] = useState<(typeof PRIMARY_PATHS)[number]>("semantic-search");
  const [idempotent, setIdempotent] = useState(true);
  const [maxAttempts, setMaxAttempts] = useState(3);
  const [baseDelayMs, setBaseDelayMs] = useState(200);

  const timeline = useMemo(() => {
    const steps: Array<{
      action: string;
      attempt: number;
      delayMs: number | null;
      label: string;
    }> = [];
    for (let attempt = 0; attempt <= maxAttempts; attempt += 1) {
      const action = retryAction(errorType, attempt, maxAttempts, idempotent);
      steps.push({
        attempt,
        action,
        delayMs: action === "retry" ? retryDelay(baseDelayMs, attempt, 2000) : null,
        label:
          action === "retry"
            ? `retry after ${retryDelay(baseDelayMs, attempt, 2000)}ms`
            : action === "fallback"
              ? `switch to ${fallbackTarget(primaryPath)}`
              : "stop immediately",
      });
      if (action !== "retry") break;
    }
    return steps;
  }, [baseDelayMs, errorType, idempotent, maxAttempts, primaryPath]);

  const finalStep = timeline[timeline.length - 1];

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Retries And Fallbacks</div>
        <p className="observable-viz-subtitle">
          Retries are for transient failures on safe operations. Once retries stop
          being worth it, the system should degrade intentionally instead of looping.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Error</span>
          <select
            className="observable-control-select"
            value={errorType}
            onChange={(event) => setErrorType(event.target.value as (typeof ALL_ERRORS)[number])}
          >
            {ALL_ERRORS.map((error) => (
              <option key={error} value={error}>
                {error}
              </option>
            ))}
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Primary path</span>
          <select
            className="observable-control-select"
            value={primaryPath}
            onChange={(event) =>
              setPrimaryPath(event.target.value as (typeof PRIMARY_PATHS)[number])
            }
          >
            {PRIMARY_PATHS.map((path) => (
              <option key={path} value={path}>
                {path}
              </option>
            ))}
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Idempotent</span>
          <select
            className="observable-control-select"
            value={idempotent ? "yes" : "no"}
            onChange={(event) => setIdempotent(event.target.value === "yes")}
          >
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Max attempts</span>
          <input
            className="observable-control-input"
            type="range"
            min="1"
            max="5"
            step="1"
            value={maxAttempts}
            onChange={(event) => setMaxAttempts(Number(event.target.value))}
          />
          <span className="observable-control-value">{maxAttempts}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Base delay</span>
          <input
            className="observable-control-input"
            type="range"
            min="100"
            max="600"
            step="50"
            value={baseDelayMs}
            onChange={(event) => setBaseDelayMs(Number(event.target.value))}
          />
          <span className="observable-control-value">{baseDelayMs}ms</span>
        </label>
      </div>

      <div className="retry-viz-timeline">
        {timeline.map((step) => (
          <div
            key={`${step.attempt}-${step.action}`}
            className={`retry-viz-step retry-viz-step-${step.action}`}
          >
            <div className="retry-viz-step-header">
              <strong>Attempt {step.attempt + 1}</strong>
              <span>{step.action}</span>
            </div>
            <p>{step.label}</p>
            {step.delayMs !== null ? (
              <div className="retry-viz-delay">
                <span style={{ width: `${Math.min((step.delayMs / 2000) * 100, 100)}%` }} />
              </div>
            ) : null}
          </div>
        ))}
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Error class</span>
          <span className="observable-stat-value">{errorType}</span>
        </div>
        <div className="observable-stat-row">
          <span>Terminal action</span>
          <span className="observable-stat-value">{finalStep?.action ?? "n/a"}</span>
        </div>
        <div className="observable-stat-row">
          <span>Fallback</span>
          <span className="observable-stat-value">
            {finalStep?.action === "fallback" ? fallbackTarget(primaryPath) : "none"}
          </span>
        </div>
        <div className="observable-stat-row">
          <span>Retry count</span>
          <span className="observable-stat-value">
            {timeline.filter((step) => step.action === "retry").length}
          </span>
        </div>
      </div>
    </div>
  );
}
