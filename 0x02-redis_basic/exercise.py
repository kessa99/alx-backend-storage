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
