from discord import __verison__ as dversion
from platform import python_version as pversion

from DS.core import prefix
from DS.core import Logger

from config import token
from config import description
from config import pm_help

import arrow

if not token:
    token = input("Please enter a valid discord bot token: ")
    os.environ["BotToken"] = token

class DS(discord.ext.commands.Bot):
    def __init__(self):
        __super__().__init__(command_prefix=prefix.getPrefix, description=description, pm_help=pm_help)
        self.logger = Logger(name="BOT")

    async def track_start(self):
        await self.wait_until_ready()
        self.start_time = arrow.now()
        self.messages = cache.messages

    async def on_ready(self):
        self.logger.info("\n\n-------------------------------------------------")
        self.logger.info(f"{self.user.name} ready for combat")
        self.logger.info(f"Discord {dversion} - Python {pversion()}")
        self.logger.info(f"ID: self.user.id")
        self.logger.info(f"------------------------------------------------\n")
