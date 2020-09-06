import requests
from unittest.mock import patch

URL = "http://127.0.0.1:5000/"


@patch("main.services.db_api.DBapi.types")
def test_get_single_type(mock_db):
    test_type = {
        'name': "TestType",
        'description': "Testing Test Type",
        'measurement': 1234.5678
    }

    mock_db.return_value = test_type

    data = requests.get(URL + "/get/1")
    data = data.json

    assert data == test_type

def test_get_type_list():
    pass


def test_post_type():
    pass


def test_put_type():
    pass


def test_delete_type():
    pass
