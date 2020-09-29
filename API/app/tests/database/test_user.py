import pytest
import psycopg2
from psycopg2 import extras

from main.services.db_api import DBapi
from main.repositories.abc_table import AbcTable
from main.util.mappers.user import User

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest2 user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_user():
    assert len(DBapi.users("GET", 1)) == 1


def test_get_user_list():
    assert len(DBapi.users("GET")) == 5


def test_post_user():
    AbcTable._cur.execute("BEGIN;")
    new_user = User(name="testuser", email="testemail", username="testusername", password="PASSWORD")
    DBapi.users("POST", data=new_user)
    assert len(DBapi.users("GET")) == 6
    AbcTable._cur.execute("ROLLBACK;")


def test_put_user():
    AbcTable._cur.execute("BEGIN;")
    updated_user = User(name="TESTNAME")
    DBapi.users("PUT", 1, updated_user)
    assert DBapi.users("GET", 1)[0].name == "TESTNAME"
    AbcTable._cur.execute("ROLLBACK;")


def test_delete_user():
    AbcTable._cur.execute("BEGIN;")
    assert len(DBapi.users("GET")) == 5
    DBapi.users("DELETE", 3)
    assert len(DBapi.users("GET")) == 4
    AbcTable._cur.execute("ROLLBACK;")


def test_exceptions_user():
    with pytest.raises(Exception, match="Missing data"):
        DBapi.users("POST")
    with pytest.raises(Exception, match="Missing data"):
        DBapi.users("PUT", 1)
    with pytest.raises(Exception, match="Missing id"):
        DBapi.users("PUT")
    with pytest.raises(Exception, match="Missing id"):
        DBapi.users("DELETE")
    with pytest.raises(Exception, match="Method not in list of approved methods: GET, POST, PUT, DELETE"):
        DBapi.users("test")
