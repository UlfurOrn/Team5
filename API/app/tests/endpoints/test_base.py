import unittest
from unittest.mock import Mock

from flask import Flask
from flask_restplus import Api

from main.util.logging.logging_registry import LoggingRegistry

from main.controller.record_controller import api as record_ns
from main.controller.habit_controller import api as habit_ns
from main.controller.user_controller import api as user_ns
from main.controller.health_controller import api as health_ns
from main.controller.auth_controller import api as auth_ns


class TestBase(unittest.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()

        app = Flask(__name__)
        api = Api()

        api.add_namespace(record_ns)
        api.add_namespace(habit_ns)
        api.add_namespace(user_ns)
        api.add_namespace(health_ns)
        api.add_namespace(auth_ns)

        api.init_app(app)

        self.app = app.test_client()

        self.valid_header = {
            "Content-Type": "application/json"
        }

        # Create mock logger
        mock_logger = Mock()

        # Create mock logger methods
        mock_logger.debug()
        mock_logger.info()
        mock_logger.exception()
        mock_logger.critical()
        mock_logger.reset_mock()

        # Override normal logger with mock logger
        LoggingRegistry.LOGGER = mock_logger
