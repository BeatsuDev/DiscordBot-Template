import os

# bot
token = os.getenv('BotToken', '')

prefix_server = 'd!'
prefix_dm = ['d!', '']
description = 'A Discord bot designed to moderate entire servers and guide users through a tutorial of Discord'
pm_help = True

data_file = os.path.abspath(os.path.join(os.getcwd(), 'data/cache.json'))

# logging
log_file = os.path.abspath(os.path.join(os.getcwd(), 'logs.txt'))
file_logging_level = 'info'
stream_logging_level = 'warning'
logging_stdout = True
logging_format = "%(levelname)s:%(asctime)s - %(name)s:%(filename)s:%(message)s"
