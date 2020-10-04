import unittest

from flask import Flask
from flask_restplus import Api

from endpoints.email import api as email_ns
from endpoints.content import api as content_ns
from endpoints.subject import api as subject_ns

from mail_service.mail_service import mail_service
from mail_service.mail_service_stub import MailServiceStub


class TestBase(unittest.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()

        app = Flask(__name__)
        api = Api()

        api.add_namespace(email_ns)
        api.add_namespace(content_ns)
        api.add_namespace(subject_ns)

        api.init_app(app)

        self.app = app.test_client()

        self.valid_header = {
            "Content-Type": "application/json"
        }

        mail_service.mail_service = MailServiceStub()
