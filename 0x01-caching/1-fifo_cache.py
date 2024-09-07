#!/usr/bin/env python3
"""Implement a Fifo cache"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """make a fifo cache
    """

    def __init__(self):
        """initilize FIFOCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ add something to cache """
        if key or item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey = next(iter(self.cache_data))
            del self.cache_data[firstKey]
            print("DISCARD:", firstKey)

    def get(self, key):
        """ retrieve item from cache """
        if not key:
            return None
        if self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
