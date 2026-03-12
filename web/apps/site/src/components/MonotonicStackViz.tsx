"use client";

import { useMemo, useState } from "react";

const TEMPERATURES = [73, 74, 75, 71, 69, 72, 76, 73] as const;

interface StackFrame {
  actions: string[];
  answers: number[];
  currentIndex: number;
  stack: number[];
}

function buildFrames(values: number[]) {
  const frames: StackFrame[] = [];
  const stack: number[] = [];
  const answers = Array(values.length).fill(0);

  for (let index = 0; index < values.length; index += 1) {
    const actions = [`visit day ${index}`];
    while (stack.length > 0 && values[index] > values[stack[stack.length - 1]]) {
      const resolved = stack.pop()!;
      answers[resolved] = index - resolved;
      actions.push(`resolve day ${resolved} with wait ${answers[resolved]}`);
    }
    stack.push(index);
    actions.push(`push day ${index}`);
    frames.push({
      currentIndex: index,
      answers: [...answers],
      stack: [...stack],
      actions,
    });
  }

  return frames;
}

export default function MonotonicStackViz() {
  const [step, setStep] = useState(TEMPERATURES.length - 1);
  const frames = useMemo(() => buildFrames([...TEMPERATURES]), []);
  const frame = frames[step];
  const maxTemp = Math.max(...TEMPERATURES);
  const minTemp = Math.min(...TEMPERATURES);

  if (!frame) return null;

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Monotonic Stack Walkthrough</div>
        <p className="observable-viz-subtitle">
          Step through daily temperatures and watch unresolved colder days stay on
          the stack until a warmer day pops them.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Step</span>
          <input
            className="observable-control-input"
            type="range"
            min="0"
            max={String(TEMPERATURES.length - 1)}
            step="1"
            value={step}
            onChange={(event) => setStep(Number(event.target.value))}
          />
          <span className="observable-control-value">{step}</span>
        </label>
      </div>

      <div className="stack-viz-columns">
        <div className="stack-viz-bars">
          {TEMPERATURES.map((temperature, index) => {
            const height = 34 + ((temperature - minTemp) / (maxTemp - minTemp || 1)) * 90;
            const inStack = frame.stack.includes(index);
            const resolved = frame.answers[index] > 0;
            const isCurrent = index === frame.currentIndex;
            return (
              <div key={index} className="stack-viz-bar-slot">
                <div
                  className={`stack-viz-bar ${
                    isCurrent
                      ? "stack-viz-bar-current"
                      : inStack
                        ? "stack-viz-bar-stack"
                        : resolved
                          ? "stack-viz-bar-resolved"
                          : "stack-viz-bar-pending"
                  }`}
                  style={{ height }}
                >
                  <span>{temperature}</span>
                </div>
                <strong>d{index}</strong>
                <small>{frame.answers[index] > 0 ? `${frame.answers[index]}d` : "-"}</small>
              </div>
            );
          })}
        </div>

        <div className="stack-viz-side">
          <div className="stack-viz-side-card">
            <div className="stack-viz-side-title">{"Stack top -> bottom"}</div>
            <div className="stack-viz-stack">
              {[...frame.stack].reverse().map((index) => (
                <span key={index} className="stack-viz-stack-item">
                  d{index} · {TEMPERATURES[index]}
                </span>
              ))}
              {frame.stack.length === 0 ? (
                <span className="stack-viz-stack-empty">empty</span>
              ) : null}
            </div>
          </div>

          <div className="stack-viz-side-card">
            <div className="stack-viz-side-title">Actions at this step</div>
            <div className="stack-viz-actions">
              {frame.actions.map((action) => (
                <span key={action} className="stack-viz-action">
                  {action}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Current day</span>
          <span className="observable-stat-value">d{frame.currentIndex}</span>
        </div>
        <div className="observable-stat-row">
          <span>Current temp</span>
          <span className="observable-stat-value">{TEMPERATURES[frame.currentIndex]}</span>
        </div>
        <div className="observable-stat-row">
          <span>Stack size</span>
          <span className="observable-stat-value">{frame.stack.length}</span>
        </div>
        <div className="observable-stat-row">
          <span>Resolved days</span>
          <span className="observable-stat-value">
            {frame.answers.filter((value) => value > 0).length}
          </span>
        </div>
      </div>
    </div>
  );
}
