from main.util.logging.logging_plugin import LoggingPlugin


class LoggingRegistry:
    LOGGER = LoggingPlugin.get_logger()

    def get_logger(self):
        return self.LOGGER
