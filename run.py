from discord import __version__ as dversion

from DS.core.bot import DS
from DS.core import Logging

from config import token
from config import discord_logging_level
from config import logging_format

import errno, sys, os, re
import logging

# Yeet

logger = Logging.get_logger('discord')

dversion = tuple([int(vnum) for vnum in (re.sub('[^1234567890.]', '', dversion)).split('.')])
dmajor, dminor, dmicro = dversion

if not (dmajor, dminor) >= (1, 0):
    print('[CRITICAL ERROR] Wrong version of discord! Please use the rewrite version, version 1.0.0a or above.')
    print('[INFO] This can be installed with: pip install discord-rewrite')
    exit(errno.EINVAL)

if not sys.version_info >= (3, 6):
    print('[CRITICAL ERROR] Wrong Python Version! This bot supports Python 3.6+ only!')
    exit(errno.EINVAL)

if __name__ == '__main__':
    os.system('pip install -r requirements.txt')
    bot = DS()
    bot.run(token)
