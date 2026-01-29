from dataclasses import dataclass
from typing import Any, TypedDict

from task_queue.core.constants import TaskStatus


class Payload(TypedDict):
    args: list[Any]
    kwargs: dict[str, Any]


@dataclass(slots=True)
class TaskRecord:
    id: str
    task_name: str
    payload_json: str

    status: TaskStatus
    attempt: int
    max_attempts: int
    timeout_s: int

    enqueued_at_ms: int
    updated_at_ms: int

    scheduled_at_ms: int | None = None
    started_at_ms: int | None = None
    lease_expires_at_ms: int | None = None
    assigned_worker_id: str | None = None
    last_error: str | None = None
    idempotency_key: str | None = None