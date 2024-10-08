#!/usr/bin/env python3
"""Implement a Fifo cache"""

from base_caching import BaseCaching
from typing import Optional, Any


class FIFOCache(BaseCaching):
    """make a fifo cache
    """

    def __init__(self):
        """initilize FIFOCache"""
        super().__init__()
        self.order = []

    def put(self, key: Any, item: Any) -> None:
        """ add something to cache """
        if key or item:
            self.cache_data[key] = item

            if key not in self.order:
                self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                firstKey = self.order.pop(0)
                del self.cache_data[firstKey]
                print("DISCARD:", firstKey)

    def get(self, key: Any) -> Optional[Any]:
        """ retrieve item from cache """
        if not key:
            return None
        if self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
