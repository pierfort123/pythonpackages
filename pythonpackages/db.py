import os
import redis

auth_secret = os.getenv('AUTH_POLICY_SECRET', '')
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_secret = os.getenv('REDIS_SESSIONS_SECRET', '')
redis = redis.from_url(redis_url)
