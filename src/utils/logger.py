
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log(message):
    logger.info(message)
