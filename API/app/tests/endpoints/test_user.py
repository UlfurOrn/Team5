from main.services.db_api import DBapi
from main.services.abc_table import AbcTable
import psycopg2
from psycopg2 import extras
import pytest

import requests
from unittest.mock import patch

from tests.endpoints.test_base import TestBase

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)

@patch("main.services.db_api.DBapi.users")
class TestUserEndpoint(TestBase):
    def test_get_single_user(self, mock_db):
        test_user = {
            'name': "testuser",
            'email': "testuser@email.com",
            'dob': "2020-04-25",
            'gender': "m",
            'weight': "85",
            'height': "180"
        }

        mock_db.return_value = [test_user]

        response = self.app.get("type/1")
        data = response.json

        assert data == test_user
        assert mock_db.called_once_with('GET', '1')


    def test_get_user_list(self, mock_db):
        test_user_list = [
            {
                'name': "testuser",
                'email': "test@email.com",
                'dob': "2020-04-25",
                'gender': "m",
                'weight': "85",
                'height': "180"
            },
            {
                'name': "testuser2",
                'email': "test2@email.com",
                'dob': "2000-01-25",
                'gender': "f",
                'weight': "60",
                'height': "170"
            }
        ]

        mock_db.return_value = test_user_list

        response = self.app.get("/user")
        data = response.json

        assert data == {
            "users": test_user_list
        }
        assert mock_db.called_once_with('GET')

    def test_post_user(self):
        pass

    def test_put_user(self):
        pass

    def test_delete_user(self):
        pass

    def test_exceptions_user(self):
        pass