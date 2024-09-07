#!/usr/bin/env python3
""" """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    """
    def __init__(self):
        """call super from Parent
        """
        super().__init__()

    def put(self, key, item):
        """
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        """
        if not key:
            return None
        if self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
