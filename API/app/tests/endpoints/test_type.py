import requests
from unittest.mock import patch

from tests.endpoints.test_base import TestBase


@patch("main.services.db_api.DBapi.types")
class TestTypeEndpoint(TestBase):

    def test_get_single_type(self, mock_db):
        test_type = {
            'name': "TestType",
            'description': "Testing Test Type",
            'measurement': 1234.5678
        }

        mock_db.return_value = test_type

        response = self.app.get("type/1")
        data = response.json

        print(data)

        assert data == test_type

    def test_get_type_list(self, mock_db):
        pass

    def test_post_type(self, mock_db):
        pass

    def test_put_type(self, mock_db):
        pass

    def test_delete_type(self, mock_db):
        pass
