import redis
from distributed_task_queue.config.settings import load_settings


class RedisFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedisFactory,cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance


    def _initialize(self):
        settings = load_settings()

        self.pool = redis.ConnectionPool(host=settings.redis_host,port = settings.redis_port, db = settings.redis_db)
    def get_client(self):
        return redis.Redis(connection_pool=self.pool)
    



def redis_client():
    return RedisFactory().get_client()
    