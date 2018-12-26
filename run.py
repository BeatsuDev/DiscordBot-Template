from discord import __version__ as dversion

from DS.core import DS

from config import token
from config import discord_logger_level
from config import logging_format

import errno, sys, os
import logging

# Yeet

os.system('pip install -r requirements.txt')

logger = logging.getLogger('discord')
logger.setLevel(discord_logger_level)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(logging_format))
logger.addHandler(handler)

if not dversion >= (1, 0):
    print('[CRITICAL ERROR] Wrong version of discord! Please use the rewrite version, version 1.0.0a or above.')
    print('[INFO] This can be installed with: pip install discord-rewrite')
    exit(errno.EINVAL)

if not sys.version_info >= (3, 6):
    print('[CRITICAL ERROR] Wrong Python Version! This bot supports Python 3.6+ only!')
    exit(errno.EINVAL)

if __name__ == '__main__':
    bot = DS()
    DS.run(token)
