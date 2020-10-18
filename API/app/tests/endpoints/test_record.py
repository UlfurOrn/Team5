from unittest.mock import patch

from main.util.mappers.recordmapper import RecordMapper
from tests.endpoints.test_base import TestBase


class TestRecordEndpoint(TestBase):

    def setUp(self):
        super(TestRecordEndpoint, self).setUp()

        self.test_record_mapper = RecordMapper(1, 1, 1, 1234, "2020-01-01T01:01:01")
        self.test_record_dict = {
                'recordid': 1,
                'userid': 1,
                'habitid': 1,
                'rdate': "2020-01-01T01:01:01",
                'amount': 1234
            }

    @patch("main.controller.record_controller.DBapi.records.get")
    def test_get_single_record(self, mock_db):
        mock_db.return_value = [self.test_record_mapper]  # DB returns record in a list

        response = self.app.get("record/1", headers=self.valid_header)
        data = response.json

        assert data == self.test_record_dict
        mock_db.assert_called_once_with(1)

    @patch("main.controller.record_controller.DBapi.records.get")
    def test_get_record_list(self, mock_db):
        test_record_list_insert = [
            RecordMapper(1, 1, 1, 1234.0, "2020-01-01T01:01:01"),
            RecordMapper(2, 2, 2, 12345.0, "2020-02-02T02:02:02"),
            RecordMapper(3, 3, 3, 123456.0, "2020-03-03T03:03:03")
        ]
        test_record_list = [
            {'recordid': 1, 'userid': 1, 'habitid': 1, 'rdate': "2020-01-01T01:01:01", 'amount': 1234.0},
            {'recordid': 2, 'userid': 2, 'habitid': 2, 'rdate': "2020-02-02T02:02:02", 'amount': 12345.0},
            {'recordid': 3, 'userid': 3, 'habitid': 3, 'rdate': "2020-03-03T03:03:03", 'amount': 123456.0}
        ]

        mock_db.return_value = test_record_list_insert

        response = self.app.get("/record", headers=self.valid_header)
        data = response.json

        assert data == {
            "records": test_record_list
        }
        mock_db.assert_called_once()

    @patch("main.controller.record_controller.DBapi.records.post")
    def test_post_record(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/record", headers=self.valid_header, json=self.test_record_dict)
        data = response.json

        assert data is None
        mock_db.assert_called_once()

    @patch("main.controller.record_controller.DBapi.records.get")
    @patch("main.controller.record_controller.DBapi.records.put")
    def test_put_record(self, mock_db, mock_get):
        mock_get.return_value = [self.test_record_mapper]
        mock_db.return_value = None

        response = self.app.put("record/1", headers=self.valid_header, json=self.test_record_dict)
        data = response.json

        assert data == self.test_record_dict
        assert response.status_code == 201
        mock_db.assert_called_once()

    @patch("main.controller.record_controller.DBapi.records.get")
    @patch("main.controller.record_controller.DBapi.records.delete")
    def test_delete_record(self, mock_db, mock_get):
        mock_get.return_value = True
        mock_db.return_value = None

        response = self.app.delete("record/1", headers=self.valid_header)
        data = response.json

        assert data == ""
        assert response.status_code == 200
        mock_get.assert_called_once_with(1)
        mock_db.assert_called_once_with(1)
