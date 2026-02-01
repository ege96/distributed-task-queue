from __future__ import annotations

from dataclasses import dataclass

from distributed_task_queue.domain.enums import TaskStatus
import uuid

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
    
    @staticmethod
    def create_task(
        task_name: str,
        payload_json: str,
        max_attempts: int,
        timeout_s: int,
    ) -> TaskRecord:
        return TaskRecord(
            id=str(uuid.uuid4()),
            task_name=task_name,
            payload_json=payload_json,
            status=TaskStatus.PENDING,
            attempt=0,
            max_attempts=max_attempts,
            timeout_s=timeout_s,
            updated_at_ms=None,
            owner_worker_id=None,
            lease_expires_at_ms=None,
            lease_token=None,
            last_error=None,
        )
