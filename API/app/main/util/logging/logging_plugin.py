import logging
from logging.config import fileConfig

LOGGING_TYPE = "DEV"


class LoggingPlugin:

    LOGGING_LIVE_CONFIG = "main/util/logging/live_logging.ini"
    LOGGING_DEV_CONFIG = "main/util/logging/dev_logging.ini"

    @classmethod
    def get_logger(cls):
        if LOGGING_TYPE == "DEV":
            fileConfig(cls.LOGGING_DEV_CONFIG)

        elif LOGGING_TYPE == "LIVE":
            fileConfig(cls.LOGGING_LIVE_CONFIG)

        logger = logging.getLogger()

        if LOGGING_TYPE == "DEV":
            logger.setLevel("DEBUG")

        elif LOGGING_TYPE == "LIVE":
            logger.setLevel("WARNING")

        return logger
