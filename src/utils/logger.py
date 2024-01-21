
import logging
from datetime import datetime

class Logger:
    def __init__(self):
        # Configure logging
        logging.basicConfig(filename='twitter_bot.log', level=logging.INFO)

    def log_info(self, message):
        # Log information messages
        logging.info(f'{datetime.now()}: {message}')

    def log_error(self, message):
        # Log error messages
        logging.error(f'{datetime.now()}: {message}')
