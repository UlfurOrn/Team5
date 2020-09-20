from main.util.logging.logging_plugin import LoggingPlugin


class LoggingRegistry:
    LOGGER = LoggingPlugin.get_logger()

    @classmethod
    def get_logger(cls):
        return cls.LOGGER
