import requests
from unittest.mock import patch

from tests.endpoints.test_base import TestBase


@patch("main.controller.record_controller.DBapi.records")
class TestRecordEndpoint(TestBase):

    def setUp(self):
        super(TestRecordEndpoint, self).setUp()

        self.test_record = {
                'userid': 1,
                'typeid': 1,
                'rdatetime': "2020-01-01T01:01:01",
                'amount': 1234
            }

    def test_get_single_record(self, mock_db):
        mock_db.return_value = [self.test_record]  # DB returns record in a list

        response = self.app.get("record/1/1/2020-01-01T01:01:01", headers=self.valid_header)
        data = response.json

        assert data == self.test_record
        mock_db.assert_called_once_with('GET', ["1", "1", "2020-01-01T01:01:01"])

    def test_get_record_list(self, mock_db):
        test_record_list = [
            {
                'userid': 1,
                'typeid': 1,
                'rdatetime': "2020-01-01T01:01:01",
                'amount': 1234
            },
            {
                'userid': 2,
                'typeid': 2,
                'rdatetime': "2020-02-02T02:02:02",
                'amount': 12345
            },
            {
                'userid': 3,
                'typeid': 3,
                'rdatetime': "2020-03-03T03:03:03",
                'amount': 123456
            }
        ]

        mock_db.return_value = test_record_list

        response = self.app.get("/record", headers=self.valid_header)
        data = response.json

        assert data == {
            "records": test_record_list
        }
        mock_db.assert_called_once_with("GET")

    def test_post_record(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/record", headers=self.valid_header, json=self.test_record)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("POST", data=self.test_record)

    def test_put_record(self, mock_db):
        mock_db.return_value = None

        response = self.app.put("record/1/1/2020-01-01T01:01:01", headers=self.valid_header, json=self.test_record)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with('PUT', ["1", "1", "2020-01-01T01:01:01"], data=self.test_record)

    def test_delete_record(self, mock_db):
        mock_db.return_value = None

        response = self.app.delete("record/1/1/2020-01-01T01:01:01", headers=self.valid_header)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with('DELETE', ["1", "1", "2020-01-01T01:01:01"])
