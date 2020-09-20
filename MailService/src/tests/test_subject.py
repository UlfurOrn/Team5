import sys
from unittest.mock import patch

from tests.test_base import TestBase
from tests.mail_service_stub import MailServiceStub


@patch("endpoints.subject.MailService")
class TestSubjectEndpoint(TestBase):

    def test_get(self, mock_mail):
        mock_mail.return_value = MailServiceStub()
        response = self.app.get("subject")
        data = response.json

        assert data["subject"] == "subject"

    def test_put(self, mock_mail):
        mock_mail.return_value = MailServiceStub()

        response = self.app.put("subject")
        data = response.json

        assert data["subject"] == "subject"
