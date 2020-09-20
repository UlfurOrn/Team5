import logging


class LoggingRegistry:

    LOGGER = logging.getLogger()

    def get_logger(self):
        return self.LOGGER
