from DS.core import Logging

from config import cache_file

import arrow, json, os

class Cache:
    def __init__(self):
        self.logger = Logging.get_logger(name='cache')
        self.logger.debug("Cache Initiated")
        self.file = cache_file

        try:
            os.mkdir(self.file)
            self.logger.info(f"Created directory \"{self.file}\"")
        except OSError:
            self.logger.debug(f"Cache file not created; already exists")

    async def _load_from_file(self):
        self.logger.debug("Attempting to load Cache from file")
        with open(self.file, 'r') as cache:
            try:
                data = json.load(cache)
                self.logger.info("Loaded Cache from file")
                self.logger.debug(f"Loaded Cache from file; length: {len(data)}")
            except json.decoder.JSONDecodeError:
                self.logger.info("Cache file empty")
                data = {}
            return True
        self.logger.error(f"Failed to load Cache from file {self.file}")
        return False

    async def _save_to_file():
        with open(self.file, 'w') as cache:
            json.dump(self.data, cache)
            self.logger.debug("Saved cache to file")
            return True
        self.logger.warning("Error in cache while saving to Cache file")

    async def save(self, key, value):
        self.data[key] = value
        self.logger.debug(f"{key} with the value {value} was saved to the Cache")
        self._save_to_file()

    async def get(self, key):
        req = None
        if not self.data: await self._load_from_file()
        try:
            req = self.data[key]
            self.logger.debug(f"Requested {req}")
        except KeyError:
            self.logger.info(f"Requested key \"{key}\" not found.")
        return req

    async def delete(self):
        try:
            req = self.data.pop(key, none)
            self.logger.debug(f"Deleted {key} with value {self.data[key]}")
        except KeyError:
            self.logger.info(f"Deletion of key \"{key}\" not succesfull. Key not found.")
        return req
