#!/usr/bin/env python3
"""A lifo cache implementation
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class implementing lifo caching
    """

    def __init__(self):
        """class Initialization
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Put something in the cache
        """
        if key or value:
            self.cache_data[key] = item

            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lastKey = self.order[-2]
                del self.cache_data[lastKey]
                print(f"DISCARD: {lastKey}")

    def get(self, key):
        """retrieve something from cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
