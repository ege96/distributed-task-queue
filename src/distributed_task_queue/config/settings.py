from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    redis_host: str
    redis_port: int
    redis_db: int
    lease_duration_ms: int
    heartbeat_ttl_s: int
    scheduler_tick_ms: int
    monitor_tick_ms: int
    max_attempts: int
    timeout_s: int


def _get_env_int(name: str, default: int) -> int:
    value = os.environ.get(name)
    if value is None:
        return default
    return int(value)


def _get_env_str(name: str, default: str) -> str:
    value = os.environ.get(name)
    if value is None:
        return default
    return value


def load_settings() -> Settings:
    return Settings(
        redis_host=_get_env_str("REDIS_HOST", "127.0.0.1"),
        redis_port=_get_env_int("REDIS_PORT", 6379),
        redis_db=_get_env_int("REDIS_DB", 0),
        lease_duration_ms=_get_env_int("LEASE_DURATION_MS", 30_000),
        heartbeat_ttl_s=_get_env_int("HEARTBEAT_TTL_S", 60),
        scheduler_tick_ms=_get_env_int("SCHEDULER_TICK_MS", 1_000),
        monitor_tick_ms=_get_env_int("MONITOR_TICK_MS", 1_000),
        max_attempts=_get_env_int("MAX_ATTEMPTS", 5),
        timeout_s=_get_env_int("TIMEOUT_S", 60),
    )
