
from unittest.mock import patch

from tests.test_base import TestBase
from tests.mail_service_stub import MailServiceStub


class TestSubject(TestBase):

    @patch("endpoints.subject.MailService")
    def test_get_subject(self, mock_mail_service):
        mock_mail_service.return_value = MailServiceStub()

        response = self.app.get("/subject")
        data = response.json

        assert data["subject"] == "subject"
