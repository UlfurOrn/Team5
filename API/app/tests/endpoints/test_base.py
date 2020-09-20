import unittest

from flask import Flask
from flask_restplus import Api

from main.controller.record_controller import api as record_ns
from main.controller.type_controller import api as type_ns
from main.controller.user_controller import api as user_ns
from main.controller.health_controller import api as health_ns


class TestBase(unittest.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()

        app = Flask(__name__)
        api = Api()

        api.add_namespace(record_ns)
        api.add_namespace(type_ns)
        api.add_namespace(user_ns)
        api.add_namespace(health_ns)

        api.init_app(app)

        self.app = app.test_client()

        self.valid_header = {
            "Content-Type": "application/json"
        }
