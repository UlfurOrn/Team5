import unittest

from flask import Flask
from flask_restplus import Api

from endpoints.subject import api as subject_ns
from endpoints.content import api as content_ns


class TestBase(unittest.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()

        app = Flask(__name__)
        api = Api()

        api.add_namespace(subject_ns)
        api.add_namespace(content_ns)

        api.init_app(app)

        self.app = app.test_client()

        self.valid_header = {
            "Content-Type": "application/json"
        }