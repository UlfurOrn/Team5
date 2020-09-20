import logging
from logging.config import fileConfig


class LoggingPlugin:

    LOGGING_CONFIG = "main/util/logging/logging.ini"

    @classmethod
    def get_logger(cls):
        fileConfig(cls.LOGGING_CONFIG)
        return logging.getLogger()
