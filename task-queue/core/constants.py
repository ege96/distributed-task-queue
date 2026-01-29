from enum import StrEnum
from dataclasses import dataclass

class TaskStatus(StrEnum):
    PENDING = "PENDING"
    SCHEDULED = "SCHEDULED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"



TERMINAL_STATUSES = {TaskStatus.COMPLETED, TaskStatus.FAILED}


@dataclass(frozen=True)
class RedisKeys:
    # Queues
    intake_queue: str = "queue:intake"
    dlq_queue: str = "queue:dlq"
    inbox_prefix: str = "queue:inbox:"  # inbox key = f"{inbox_prefix}{worker_id}"

    # Canonical tasks
    task_prefix: str = "task:"  # task key = f"{task_prefix}{task_id}"

    # Leases
    processing_zset: str = "processing:zset"

    # Heartbeats
    heartbeat_prefix: str = "worker:heartbeat:"  # heartbeat key = f"{heartbeat_prefix}{worker_id}"

    # Leadership locks
    scheduler_leader_lock: str = "scheduler:leader"
    monitor_leader_lock: str = "monitor:leader"

DEFAULT_LEASE_DURATION_MS = 30_000
DEFAULT_HEARTBEAT_TTL_S = 10
DEFAULT_SCHEDULER_TICK_MS = 500
DEFAULT_MONITOR_TICK_MS = 500
DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_TIMEOUT_S = 30
