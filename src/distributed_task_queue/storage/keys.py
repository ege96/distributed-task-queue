from __future__ import annotations

TASK_KEY_PREFIX = "task:"
TASK_STREAM = "stream:tasks"
DLQ_STREAM = "stream:dlq"
PROCESSING_ZSET = "processing:zset"
WORKER_HEARTBEAT_PREFIX = "worker:heartbeat:"
SCHEDULER_LEADER_KEY = "scheduler:leader"
MONITOR_LEADER_KEY = "monitor:leader"


def task_key(task_id: str) -> str:
    return f"{TASK_KEY_PREFIX}{task_id}"


def worker_heartbeat_key(worker_id: str) -> str:
    return f"{WORKER_HEARTBEAT_PREFIX}{worker_id}"
