from discord.ext import commands
from discord import __version__ as dversion
from platform import python_version as pversion

from DS.core.Logging import Logger
from DS.core.cache import Cache

from config import token
from config import description
from config import pm_help
from config import prefix_dm
from config import prefix_server

import discord, arrow, os

class DS(discord.ext.commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=self.getPrefix, description=description, pm_help=pm_help)
        self.logger = Logger(name="bot")
        self.cache = Cache()

    async def track_start(self):
        """
        Starts tracking statistics
        """
        await self.wait_until_ready()
        self.start_time = arrow.now()
        self.messages = cache.messages

    async def load_all_extensions(self):
        """
        Attempts to load all .py files in /cogs/ as cog extensions
        """
        await self.wait_until_ready()
        await asyncio.sleep(1)  # ensure that on_ready has completed and finished printing
        cogs = [x.stem for x in os.abspath(join(os.getcwd(), "DS/cogs")).glob('*.py')]
        for extension in cogs:
            try:
                self.load_extension(f'cogs.{extension}')
                self.logger.info(f'Loaded {extension}')
            except Exception as e:
                error = f'{extension}\n {type(e).__name__} : {e}'
                self.logger.error(f'Failed to load extension; {error}')
            print('-' * 10)

    async def getPrefix(self, message):
        if not message.guild: return commands.when_mentioned_or(*prefix_dm)(self, message)
        return commands.when_mentioned_or(*prefix_server)(self, message)

    async def on_ready(self):
        self.app_info = await self.application_info()
        self.logger.info("\n\n-------------------------------------------------")
        self.logger.info(f"Bot: {self.user.name} | ready to fight those commands >:)")
        self.logger.info(f"Bot creator: BeatsuDev")
        self.logger.info(f"Bot owner: {self.app_info.owner}")
        self.logger.info(f"Running Discord {dversion} - Python {pversion()}")
        self.logger.info(f"ID: self.user.id")
        self.logger.info(f"------------------------------------------------\n")

    async def on_message(self, message):
        if message.author.id in cache.get(blacklisted): return
        if message.author.bot: return
        self.process_command(message)
