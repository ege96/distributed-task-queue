import redis
from distributed_task_queue.config.settings import load_settings



def redis_client():
    settings = load_settings()

    host = settings.redis_host
    port = settings.redis_port
    db = settings.redis_db
    
    client = redis.Redis(host=host, port=port, db=db)
    return client