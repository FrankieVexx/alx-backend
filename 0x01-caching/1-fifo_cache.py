#!/usr/bin/env python3
"""A class FIFOCache that inherits from
BaseCaching m:
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class inheriting from BaseCaching
    """

    def __init__(self):
        """_init_ function
        """
        super().__init__()

    def put(self, key, item):
        """
            a function to add items to cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """
            A function thatGet items from cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
