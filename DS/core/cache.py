from DS.core.Logging import Logger

from config import cache_file

import json
import arrow

class Cache:
    def __init__(self):
        self.logger = Logger(name='cache')
        self.data = self._load_from_file() or {}
        self.logger.debug("Loaded cache from file. Cache Initiated.")
        self.file = cache_file

    async def _load_from_file(self):
        with open(self.file, 'r') as cache:
            try:
                data = json.load(cache)
            except json.decoder.JSONDecodeError:
                self.logger.info("Cache file empty!")
                data = {}
        return data

    async def _save_to_file():
        with open(self.file, 'w') as cache:
            json.dump(self.data, cache)
            self.logger.debug("Saved cache to file")
            return True
        self.logger.warning("Error in cache while saving to Cache file.")

    async def save(self, key, value):
        self.data[key] = value
        self.logger.debug(f"{key} with the value {value} was saved to the Cache")
        _save_to_file()

    async def get(self, key):
        req = self.data[key]
        self.logger.debug(f"Requested {req}")
        return req

    async def delete(self):
        req = self.data.pop(key, none)
        self.logger.debug(f"Deleted {key} with value {self.data[key]}")
        return req
