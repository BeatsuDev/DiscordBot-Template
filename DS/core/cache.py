from config import cache_file

import json
import arrow

class Cache:
    def __init__(self):
        await self.load_from_file()
        self.data = {}
        self.file = cache_file

    async def load_from_file(self):
        self.file = data_file
        with open(self.file, 'r') as cache:
            try:
                self.data = json.load(cache)
            except json.decoder.JSONDecodeError:
                self.data = {}

    async def save_to_file()

    async def save(self, key, value):
        self.data[key] = value

    async def get(self, key):
        return self.data[key]
