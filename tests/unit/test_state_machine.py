import pytest

from distributed_task_queue.common.state_machine import validate_transition
from distributed_task_queue.domain.enums import TaskStatus, TERMINAL_STATUSES


def test_allowed_transitions_succeed() -> None:
    allowed = {
        (None, TaskStatus.PENDING),
        (TaskStatus.PENDING, TaskStatus.QUEUED),
        (TaskStatus.QUEUED, TaskStatus.PROCESSING),
        (TaskStatus.PROCESSING, TaskStatus.COMPLETED),
        (TaskStatus.PROCESSING, TaskStatus.PENDING),
        (TaskStatus.PROCESSING, TaskStatus.FAILED),
    }

    for old_status, new_status in allowed:
        validate_transition(old_status, new_status)


def test_invalid_transitions_raise() -> None:
    allowed = {
        (None, TaskStatus.PENDING),
        (TaskStatus.PENDING, TaskStatus.QUEUED),
        (TaskStatus.QUEUED, TaskStatus.PROCESSING),
        (TaskStatus.PROCESSING, TaskStatus.COMPLETED),
        (TaskStatus.PROCESSING, TaskStatus.PENDING),
        (TaskStatus.PROCESSING, TaskStatus.FAILED),
    }

    all_old_statuses: list[TaskStatus | None] = [None, *TaskStatus]

    for old_status in all_old_statuses:
        for new_status in TaskStatus:
            if (old_status, new_status) in allowed:
                continue
            with pytest.raises(ValueError):
                validate_transition(old_status, new_status)


def test_terminal_states_are_terminal() -> None:
    for terminal in TERMINAL_STATUSES:
        for new_status in TaskStatus:
            if new_status == terminal:
                continue
            with pytest.raises(ValueError):
                validate_transition(terminal, new_status)
