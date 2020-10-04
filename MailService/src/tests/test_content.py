
from unittest.mock import patch

from tests.test_base import TestBase
from mail_service.mail_service_stub import MailServiceStub


@patch("endpoints.content.MailService")
class TestContent(TestBase):

    def test_get_content(self, mock_mail_service):
        mock_mail_service.return_value = MailServiceStub()

        response = self.app.get("/content")
        data = response.json

        assert data["content"] == "content"

    def test_put_content(self, mock_mail_service):
        mock_mail_service.return_value = MailServiceStub()

        test_content = {
            "content": "Test Content"
        }

        response = self.app.put("/content", headers=self.valid_header, json=test_content)
        data = response.json

        assert data == test_content

        # Reset after test
        self.app.put("/content", headers=self.valid_header, json={"content": "content"})
