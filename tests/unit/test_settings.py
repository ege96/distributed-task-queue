from distributed_task_queue.config.settings import load_settings


def test_settings_defaults() -> None:
    settings = load_settings()

    assert settings.redis_host == "127.0.0.1"
    assert settings.redis_port == 6379
    assert settings.redis_db == 0
    assert settings.lease_duration_ms == 30_000
    assert settings.heartbeat_ttl_s == 60
    assert settings.scheduler_tick_ms == 1_000
    assert settings.monitor_tick_ms == 1_000
    assert settings.max_attempts == 5
    assert settings.timeout_s == 60


def test_settings_env_overrides(monkeypatch) -> None:
    monkeypatch.setenv("REDIS_HOST", "redis.local")
    monkeypatch.setenv("REDIS_PORT", "6380")
    monkeypatch.setenv("REDIS_DB", "2")
    monkeypatch.setenv("LEASE_DURATION_MS", "45000")
    monkeypatch.setenv("HEARTBEAT_TTL_S", "75")
    monkeypatch.setenv("SCHEDULER_TICK_MS", "2500")
    monkeypatch.setenv("MONITOR_TICK_MS", "3000")
    monkeypatch.setenv("MAX_ATTEMPTS", "9")
    monkeypatch.setenv("TIMEOUT_S", "120")

    settings = load_settings()

    assert settings.redis_host == "redis.local"
    assert settings.redis_port == 6380
    assert settings.redis_db == 2
    assert settings.lease_duration_ms == 45_000
    assert settings.heartbeat_ttl_s == 75
    assert settings.scheduler_tick_ms == 2_500
    assert settings.monitor_tick_ms == 3_000
    assert settings.max_attempts == 9
    assert settings.timeout_s == 120
