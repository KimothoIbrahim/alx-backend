#!/usr/bin/env python3
"""MRUcache implementation
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """make the cache
    """

    def __init__(self):
        """initiaize cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add to cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                recentKey = self.order.pop(-2)
                del self.cache_data[recentKey]
                print(f'DISCARD: {recentKey}')
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """retrieve from cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
