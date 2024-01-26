import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(error_message):
    logger.error(error_message)

def handle_error(error):
    try:
        # Handle specific errors based on their type here
        pass
    except Exception as e:
        log_error(f"Unhandled exception: {str(e)}")
