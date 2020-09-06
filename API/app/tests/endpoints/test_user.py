from main.services.db_api import DBapi
from main.services.abc_table import AbcTable
import psycopg2
from psycopg2 import extras
import pytest

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_user():    
    test_user = {
        'name': "TestUser",
        'email': "",
        'dob': "",
        'gender': "",
        'weight': "",
        'height': ""
    }

    mock_db.return_value = test_type

    data = requests.get(URL + "/get/1")
    data = data.json

    assert data == test_type

def test_get_user_list():
    pass

def test_post_user():
    pass

def test_put_user():
    pass

def test_delete_user():
    pass

def test_exceptions_user():
    pass