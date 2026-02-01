import redis
import os



def redis_client():

    host = os.getenv('REDIS_HOST', 'localhost')
    port = int(os.getenv('REDIS_PORT', 6379))
    db = int(os.getenv('REDIS_DB', 0))
    
    client = redis.Redis(host=host, port=port, db=db)
    return client