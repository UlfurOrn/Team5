import logging
from logging.config import fileConfig


class LoggingPlugin:

    LOGGING_LIVE_CONFIG = "main/util/logging/live_logging.ini"
    LOGGING_DEV_CONFIG = "main/util/logging/dev_logging.ini"

    @classmethod
    def get_logger(cls):
        fileConfig(cls.LOGGING_CONFIG)
        return logging.getLogger()
