import redis


class Service:
    def __init__(self):
        self._redis = redis.Redis(host='redis', port=6379, password='password', decode_responses=True)
        self._redis.ping()

    def exists(self, key):
        return self._redis.exists(key)

    def get(self, key):
        return self._redis.get(key)

    def put(self, key, value):
        self._redis.set(key, value)
