from __future__ import annotations

from distributed_task_queue.domain.enums import TaskStatus, TERMINAL_STATUSES

_ALLOWED_TRANSITIONS: set[tuple[TaskStatus | None, TaskStatus]] = {
    (None, TaskStatus.PENDING),
    (TaskStatus.PENDING, TaskStatus.QUEUED),
    (TaskStatus.QUEUED, TaskStatus.PROCESSING),
    (TaskStatus.PROCESSING, TaskStatus.COMPLETED),
    (TaskStatus.PROCESSING, TaskStatus.PENDING),
    (TaskStatus.PROCESSING, TaskStatus.FAILED),
}


def validate_transition(old_status: TaskStatus | None, new_status: TaskStatus) -> None:
    if (old_status, new_status) in _ALLOWED_TRANSITIONS:
        return

    if old_status in TERMINAL_STATUSES:
        raise ValueError(
            f"Invalid transition from terminal status {old_status} to {new_status}."
        )

    raise ValueError(f"Invalid transition from {old_status} to {new_status}.")
