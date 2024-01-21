
from redis import Redis
cache = Redis(host='redis', port=6379)

def get_cached_data(key):
    return cache.get(key)

def set_cache_data(key, value):
    cache.set(key, value)
