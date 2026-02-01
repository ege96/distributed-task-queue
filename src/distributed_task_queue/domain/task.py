from __future__ import annotations

from dataclasses import dataclass

from distributed_task_queue.domain.enums import TaskStatus


@dataclass
class TaskRecord:
    id: str
    task_name: str
    payload_json: str
    status: TaskStatus
    attempt: int
    max_attempts: int
    timeout_s: int
    enqueued_at_ms: int | None
    updated_at_ms: int | None
    owner_worker_id: str | None
    lease_expires_at_ms: int | None
    lease_token: str | None
    last_error: str | None
