#!/usr/bin/env python3
"""
Cache class store an instance of Redis client as a private
named _redis and flush flushdb. the method store generate
random key
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    create a cacle class and store method
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes]:
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, bytes]:
        return self.get(key, fn=int)
