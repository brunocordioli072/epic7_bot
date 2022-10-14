import logging
import os


def init_logger():
    LOG_LEVEL = os.getenv("LOG_LEVEL") if os.getenv(
        "LOG_LEVEL") is not None else "INFO"
    logging.basicConfig(level=logging.getLevelName(LOG_LEVEL),
                        format='%(asctime)s :: %(levelname)s :: %(message)s')


def log_process(process):
    def Inner(func):
        def wrapper(*args, **kwargs):
            logging.info(f"Started: \"{process}\"")
            func(*args, **kwargs)
            logging.info(f"Finished: \"{process}\"")
        return wrapper
    return Inner
