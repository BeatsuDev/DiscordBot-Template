import logging, os

# bot
token = os.getenv('BotToken') or ''

prefix_server = 'd!'
prefix_dm = ['d!', '']
description = 'A Discord bot designed to moderate entire servers and guide users through a tutorial of Discord'
pm_help = True

data_file = os.path.abspath(os.path.join(os.getcwd(), 'data/cache.json'))

# logging
log_file = os.path.abspath(os.path.join(os.getcwd(), 'logs.log'))
file_logging_level = logging.INFO
stream_logging_level = logging.WARNING
discord_logger_level = logging.INFO
logging_stdout = True
logging_file = True
logging_format = "%(levelname)s:%(asctime)s - %(name)s:%(filename)s:%(message)s"
