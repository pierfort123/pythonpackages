import os
import redis


redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
db = redis.from_url(redis_url)
