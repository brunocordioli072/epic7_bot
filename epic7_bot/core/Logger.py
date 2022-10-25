import logging
import os


def init_logger():
    LOG_LEVEL = os.getenv("LOG_LEVEL") if os.getenv(
        "LOG_LEVEL") is not None else "DEBUG"
    logging.basicConfig(level=logging.getLevelName(LOG_LEVEL),
                        format='%(asctime)s :: %(levelname)s :: %(message)s')
