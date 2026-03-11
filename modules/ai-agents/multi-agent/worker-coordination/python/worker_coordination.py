from __future__ import annotations


def select_worker(task: str, worker_keywords: dict[str, list[str]]) -> str | None:
    lowered = task.strip().lower()
    if not lowered:
        return None
    best_worker: str | None = None
    best_score = 0
    for worker, keywords in worker_keywords.items():
        score = sum(keyword.strip().lower() in lowered for keyword in keywords)
        if score > best_score:
            best_worker = worker
            best_score = score
    return best_worker


def worker_handoff(worker: str, task: str, context: dict[str, object]) -> dict[str, object]:
    if not worker.strip():
        raise ValueError("worker must be non-empty")
    if not task.strip():
        raise ValueError("task must be non-empty")
    return {
        "worker": worker,
        "task": task,
        "context": context,
    }


def merge_worker_outputs(outputs: list[dict[str, object]]) -> dict[str, object]:
    workers: list[str] = []
    results: list[object] = []
    for output in outputs:
        worker = str(output.get("worker", "")).strip()
        if not worker:
            continue
        workers.append(worker)
        results.append(output.get("result"))
    return {
        "workers": workers,
        "results": results,
        "count": len(workers),
    }
