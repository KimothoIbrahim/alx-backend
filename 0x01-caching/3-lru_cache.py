#!/usr/bin/env python3
""" LRU caching module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """Initialize the cache system with LRU behavior"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
