from distributed_task_queue.storage.client import redis_client

redis = redis_client()

def test_redis_connection() -> None:
    try:
        pong = redis.ping()
        assert pong is True
    except Exception as e:
        assert False, f"Redis connection failed: {e}"
def test_redis_set_get() -> None:
    test_key = "test_key"
    test_value = "test_value"

    redis.set(test_key, test_value)
    retrieved_value = redis.get(test_key)

    assert retrieved_value.decode("utf-8") == test_value

if __name__ == "__main__":
    test_redis_connection()
    test_redis_set_get()
    print("All Redis tests passed.")