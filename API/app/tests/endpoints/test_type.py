import requests
from unittest.mock import patch

from tests.endpoints.test_base import TestBase


@patch("main.services.db_api.DBapi.types")
class TestTypeEndpoint(TestBase):

    def test_get_single_type(self, mock_db):
        test_type = {
            'name': "TestType",
            'description': "Testing Test Type",
            'measurement': "1234.5678"
        }

        mock_db.return_value = [test_type]  # DB returns type in a list

        response = self.app.get("type/1")
        data = response.json

        assert data == test_type
        assert mock_db.called_once_with('GET', "1")

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

        response = self.app.get("/type")
        data = response.json

        assert data == {
            "types": test_type_list
        }
        assert mock_db.called_once_with('GET')

    def test_post_type(self, mock_db):
        self.app.post("/type")

    def test_put_type(self, mock_db):
        pass

    def test_delete_type(self, mock_db):
        pass
