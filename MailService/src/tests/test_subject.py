from unittest.mock import patch

from tests.test_base import TestBase


class TestSubject(TestBase):

    def test_get_subject(self):
        response = self.app.get("/subject")
        data = response.json

        assert data["subject"] == "subject"

    def test_put_subject(self):
        test_subject = {
            "subject": "Test Subject"
        }

        response = self.app.put("/subject", headers=self.valid_header, json=test_subject)
        data = response.json

        assert data == test_subject

        # Reset after test
        self.app.put("/subject", headers=self.valid_header, json={"subject": "subject"})
