from DS.core import Logger

from config import cache_file

import json
import arrow

class Cache:
    def __init__(self):
        self.logger = Logger(name='cache')
        self.data = await self._load_from_file() or {}
        self.file = cache_file

    async def _load_from_file(self):
        with open(self.file, 'r') as cache:
            try:
                data = json.load(cache)
            except json.decoder.JSONDecodeError:
                data = {}
        return data

    async def _save_to_file():
        with open(self.file, 'w') as cache:
            json.dump(self.data, cache)
            return True

    async def save(self, key, value):
        self.data[key] = value
        _save_to_file()

    async def get(self, key):
        return self.data[key]

    async def(self, delete):
        return self.data.pop(key, none)
