"use client";

import { useMemo, useState } from "react";

const WORKSPACES = [6, 7, 8, 9] as const;
const STATUSES = ["completed", "running", "failed"] as const;

type Status = (typeof STATUSES)[number];

interface EvalRun {
  createdDay: number;
  id: string;
  status: Status;
  workspaceId: number;
}

const RUNS: EvalRun[] = WORKSPACES.flatMap((workspaceId, workspaceIndex) =>
  STATUSES.flatMap((status, statusIndex) =>
    Array.from({ length: 4 }, (_, index) => ({
      id: `${workspaceId}-${status[0]}-${index + 1}`,
      workspaceId,
      status,
      createdDay: 24 - workspaceIndex * 2 - statusIndex - index,
    }))
  )
);

function formatDay(day: number) {
  return `2026-03-${String(day).padStart(2, "0")}`;
}

export default function BTreeBasicsViz() {
  const [planMode, setPlanMode] = useState<"scan" | "index">("index");
  const [workspaceId, setWorkspaceId] = useState(7);
  const [status, setStatus] = useState<Status>("completed");
  const [limit, setLimit] = useState(3);

  const summary = useMemo(() => {
    const candidateRows = RUNS.filter(
      (run) => run.workspaceId === workspaceId && run.status === status
    ).sort((left, right) => right.createdDay - left.createdDay);
    const returnedRows = candidateRows.slice(0, limit);

    return {
      candidateRows,
      returnedRows,
      plan:
        planMode === "index"
          ? "SEARCH eval_runs USING INDEX idx_eval_runs_workspace_status_created"
          : "SCAN eval_runs",
      touchedRows: planMode === "index" ? candidateRows.length : RUNS.length,
      traversal:
        planMode === "index"
          ? "root -> workspace_id -> status+created_at"
          : "full table scan",
    };
  }, [limit, planMode, status, workspaceId]);

  const workspaceX = new Map(
    WORKSPACES.map((value, index) => [value, 85 + index * 120])
  );
  const statusY = new Map<Status, number>([
    ["completed", 178],
    ["running", 222],
    ["failed", 266],
  ]);

  const visitedIds = new Set(
    planMode === "index"
      ? summary.candidateRows.map((run) => run.id)
      : RUNS.map((run) => run.id)
  );
  const returnedIds = new Set(summary.returnedRows.map((run) => run.id));

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Composite B-Tree Path</div>
        <p className="observable-viz-subtitle">
          Compare a full table scan with a composite index on
          {" "}
          <code>(workspace_id, status, created_at DESC)</code>.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Plan</span>
          <select
            className="observable-control-select"
            value={planMode}
            onChange={(event) =>
              setPlanMode(event.target.value === "scan" ? "scan" : "index")
            }
          >
            <option value="index">Composite index</option>
            <option value="scan">Table scan</option>
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Workspace</span>
          <input
            className="observable-control-input"
            type="range"
            min="6"
            max="9"
            step="1"
            value={workspaceId}
            onChange={(event) => setWorkspaceId(Number(event.target.value))}
          />
          <span className="observable-control-value">{workspaceId}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Status</span>
          <select
            className="observable-control-select"
            value={status}
            onChange={(event) => setStatus(event.target.value as Status)}
          >
            {STATUSES.map((statusValue) => (
              <option key={statusValue} value={statusValue}>
                {statusValue}
              </option>
            ))}
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Limit</span>
          <input
            className="observable-control-input"
            type="range"
            min="1"
            max="4"
            step="1"
            value={limit}
            onChange={(event) => setLimit(Number(event.target.value))}
          />
          <span className="observable-control-value">{limit}</span>
        </label>
      </div>

      <div className="observable-chart">
        <svg
          viewBox="0 0 520 310"
          className="observable-chart-svg"
          role="img"
          aria-label="B-tree indexing path"
        >
          <g className="btree-viz-links">
            {WORKSPACES.map((value) => {
              const active = planMode === "index" && value === workspaceId;
              const scan = planMode === "scan";
              return (
                <line
                  key={`root-${value}`}
                  x1="260"
                  y1="52"
                  x2={workspaceX.get(value) ?? 0}
                  y2="108"
                  className={`btree-viz-link ${
                    active ? "btree-viz-link-active" : scan ? "btree-viz-link-scan" : ""
                  }`}
                />
              );
            })}
            {WORKSPACES.flatMap((value) =>
              STATUSES.map((statusValue) => {
                const active =
                  planMode === "index" &&
                  value === workspaceId &&
                  statusValue === status;
                const scan = planMode === "scan";
                return (
                  <line
                    key={`${value}-${statusValue}`}
                    x1={workspaceX.get(value) ?? 0}
                    y1="124"
                    x2={workspaceX.get(value) ?? 0}
                    y2={statusY.get(statusValue) ?? 0}
                    className={`btree-viz-link ${
                      active ? "btree-viz-link-active" : scan ? "btree-viz-link-scan" : ""
                    }`}
                  />
                );
              })
            )}
          </g>

          <g
            className={`btree-viz-node ${
              planMode === "index" ? "btree-viz-node-active" : "btree-viz-node-muted"
            }`}
            transform="translate(190 18)"
          >
            <rect width="140" height="34" rx="12" />
            <text x="70" y="15" textAnchor="middle">
              root
            </text>
            <text x="70" y="26" textAnchor="middle" className="btree-viz-node-subtitle">
              {"workspace -> status -> created_at"}
            </text>
          </g>

          {WORKSPACES.map((value) => {
            const active = planMode === "index" && value === workspaceId;
            const scan = planMode === "scan";
            const x = (workspaceX.get(value) ?? 0) - 36;
            return (
              <g
                key={`workspace-${value}`}
                className={`btree-viz-node ${
                  active
                    ? "btree-viz-node-active"
                    : scan
                      ? "btree-viz-node-scan"
                      : "btree-viz-node-muted"
                }`}
                transform={`translate(${x} 108)`}
              >
                <rect width="72" height="28" rx="10" />
                <text x="36" y="18" textAnchor="middle">
                  ws={value}
                </text>
              </g>
            );
          })}

          {WORKSPACES.flatMap((value) =>
            STATUSES.map((statusValue) => {
              const active =
                planMode === "index" &&
                value === workspaceId &&
                statusValue === status;
              const scan = planMode === "scan";
              const y = (statusY.get(statusValue) ?? 0) - 16;
              const x = (workspaceX.get(value) ?? 0) - 44;
              return (
                <g
                  key={`leaf-${value}-${statusValue}`}
                  className={`btree-viz-node ${
                    active
                      ? "btree-viz-node-active"
                      : scan
                        ? "btree-viz-node-scan"
                        : "btree-viz-node-muted"
                  }`}
                  transform={`translate(${x} ${y})`}
                >
                  <rect width="88" height="32" rx="10" />
                  <text x="44" y="14" textAnchor="middle">
                    {statusValue}
                  </text>
                  <text x="44" y="25" textAnchor="middle" className="btree-viz-node-subtitle">
                    4 rows
                  </text>
                </g>
              );
            })
          )}
        </svg>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Plan</span>
          <span className="observable-stat-value">{summary.plan}</span>
        </div>
        <div className="observable-stat-row">
          <span>Rows touched</span>
          <span className="observable-stat-value">{summary.touchedRows}</span>
        </div>
        <div className="observable-stat-row">
          <span>Rows returned</span>
          <span className="observable-stat-value">{summary.returnedRows.length}</span>
        </div>
        <div className="observable-stat-row">
          <span>Traversal</span>
          <span className="observable-stat-value">{summary.traversal}</span>
        </div>
      </div>

      <div className="btree-viz-results">
        <div className="btree-viz-results-header">
          Query:
          {" "}
          <code>
            WHERE workspace_id = {workspaceId} AND status = '{status}' ORDER BY
            {" "}
            created_at DESC LIMIT {limit}
          </code>
        </div>
        <div className="btree-viz-run-grid">
          {RUNS.map((run) => {
            const visited = visitedIds.has(run.id);
            const returned = returnedIds.has(run.id);
            return (
              <span
                key={run.id}
                className={`btree-viz-run ${
                  returned
                    ? "btree-viz-run-returned"
                    : visited
                      ? "btree-viz-run-visited"
                      : "btree-viz-run-skipped"
                }`}
              >
                {run.id}
                <small>{formatDay(run.createdDay)}</small>
              </span>
            );
          })}
        </div>
      </div>
    </div>
  );
}
