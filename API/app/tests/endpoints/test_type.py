import requests
from unittest.mock import patch

from tests.endpoints.test_base import TestBase


@patch("main.controller.type_controller.DBapi.types")
class TestTypeEndpoint(TestBase):

    def setUp(self):
        super(TestTypeEndpoint, self).setUp()

        self.test_type = {
            'name': "TestType",
            'description': "Testing Test Type",
            'measurement': "1234.5678"
        }

    def test_get_single_type(self, mock_db):
        mock_db.return_value = [self.test_type]  # DB returns type in a list

        response = self.app.get("type/1", headers=self.valid_header)
        data = response.json

        assert data == self.test_type
        mock_db.assert_called_once_with('GET', "1")

    def test_get_type_list(self, mock_db):
        test_type_list = [
            {
                'name': "TestType1",
                'description': "Testing Test Type 1",
                'measurement': "1234.5678"
            },
            {
                'name': "TestType2",
                'description': "Testing Test Type 2",
                'measurement': "8765.4321"
            },
            {
                'name': "TestType3",
                'description': "Testing Test Type 3",
                'measurement': "1234"
            }
        ]

        mock_db.return_value = test_type_list

        response = self.app.get("/type", headers=self.valid_header)
        data = response.json

        assert data == {
            "types": test_type_list
        }
        mock_db.assert_called_once_with("GET")

    def test_post_type(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/type", headers=self.valid_header, json=self.test_type)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("POST", data=self.test_type)

    def test_put_type(self, mock_db):
        mock_db.return_value = None

        response = self.app.put("/type/1", headers=self.valid_header, json=self.test_type)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("PUT", "1", data=self.test_type)

    def test_delete_type(self, mock_db):
        mock_db.return_value = None

        response = self.app.delete("/type/1", headers=self.valid_header)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("DELETE", "1")
