from config import data_file

import json
import arrow

class Cache:
    def __init__(self):
        await self.load_from_file()
        self.data = {}
        self.file =

    async def load_from_file(self):
        self.file = data_file
        with open(self.file, 'r') as cache:
            try:
                self.data = json.load(cache)
            except Json

    async def save(self, key, value):
        self.data[key] = value

    async def get(self, key):
        return self.data[key]
