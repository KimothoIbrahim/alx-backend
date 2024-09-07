#!/usr/bin/env python3
"""Craete a basic cache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """implements setting up, adding and retriving a cache"""

    def __init__(self):
        """call super from Parent"""
        super().__init__()

    def put(self, key, item):
        """add something to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve something from the cache"""
        if not key:
            return None
        if self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
