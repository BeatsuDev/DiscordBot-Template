from discord import __version__ as dversion
from DS.core import DS

import errno
import sys
import os

# Yeet

os.system('pip install -r requirements.txt')

if not dversion >= (1, 0):
    print('[CRITICAL ERROR] Wrong version of discord! Please use the rewrite version, version 1.0.0a or above.')
    print('[INFO] This can be installed with: pip install discord-rewrite')
    exit(errno.EINVAL)

if not sys.version_info >= (3, 6):
    print('[CRITICAL ERROR] Wrong Python Version! This bot supports Python 3.6+ only!')
    exit(errno.EINVAL)

if __name__ == '__main__':
    bot = DS()
    DS.run()
