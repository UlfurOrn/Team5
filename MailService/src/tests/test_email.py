
from unittest.mock import patch

from tests.test_base import TestBase
from tests.mail_service_stub import MailServiceStub


@patch("endpoints.email.MailService")
class TestSubject(TestBase):

    def test_get_email(self, mock_mail_service):
        mock_mail_service.return_value = MailServiceStub()

        response = self.app.get("/email")
        data = response.json

        assert data["subject"] == "subject"
        assert data["content"] == "content"

    def test_post_email(self, mock_mail_service):
        mock_mail_service.return_value = MailServiceStub()

        test_emails = {
            "emails": [
                "test1@email.com",
                "test2@email.com",
                "test3@email.com"
            ]
        }

        response = self.app.post("/email", headers=self.valid_header, json=test_emails)
        data = response.json

        assert data == ""
