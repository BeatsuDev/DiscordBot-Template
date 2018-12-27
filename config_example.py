import logging, os

# bot
token = os.getenv('BotToken') or '<!-- Enter you bot token here -->'

prefix_server = 'd!'
prefix_dm = ['d!', '']
description = 'A Discord bot designed to moderate entire servers and guide users through a tutorial of Discord'
pm_help = True

cache_file = os.path.abspath(os.path.join(os.getcwd(), 'cache/cache.json'))

# logging
log_file = os.path.abspath(os.path.join(os.getcwd(), 'logs.log'))
file_logging_level = logging.INFO
stream_logging_level = logging.INFO
logging_stdout = True
logging_file = True
logging_format = "%(levelname)s:%(asctime)s - %(name)s:%(filename)s:%(message)s"
