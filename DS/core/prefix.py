from discord.ext import commands

from config import prefix_dm
from config import prefix_server

async def getPrefix():
    if not message.guild: return commands.when_mentioned_or(*prefix_dm)(bot, message)
    return commands.when_mentioned_or(*prefix_server)(bot, message)
