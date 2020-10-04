from unittest.mock import patch

from tests.test_base import TestBase


class TestEmail(TestBase):

    def test_get_email(self):
        response = self.app.get("/email")
        data = response.json

        assert data["subject"] == "subject"
        assert data["content"] == "content"

    def test_post_email(self):
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
        assert response.status_code == 200

    @patch("endpoints.email.mail_service.mail_service.send_email")
    def test_post_emails_failing(self, mock_get_mail):
        exception_message = "Failed"
        mock_get_mail.side_effect = Exception(exception_message)

        test_email = {
            "emails": [
                "test@email.com"
            ]
        }

        response = self.app.post("/email", headers=self.valid_header, json=test_email)
        data = response.json

        assert data == exception_message
        assert response.status_code == 503
