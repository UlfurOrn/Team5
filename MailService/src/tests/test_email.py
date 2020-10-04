
from unittest.mock import patch

from tests.test_base import TestBase


class TestSubject(TestBase):

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
