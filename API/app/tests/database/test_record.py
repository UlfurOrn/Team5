from main.services.db_api import DBapi
from main.services.abc_table import AbcTable
import psycopg2
from psycopg2 import extras
import pytest

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_record():
    assert len(DBapi.records("GET", [1, 1, "2020-09-03 10:05:26"])) == 1

def test_get_record_list():
    assert len(DBapi.records("GET")) == 3

def test_post_record():
    AbcTable._cur.execute("BEGIN;")
    DBapi.records("POST", data={"userid": 1, "typeid": 2, "rdatetime": "1990-09-03 10:25:10", "amount": 10})
    assert len(DBapi.records("GET")) == 4
    AbcTable._cur.execute("ROLLBACK;")

def test_put_record():
    AbcTable._cur.execute("BEGIN;")
    DBapi.records("PUT", [1, 1, "2020-09-03 10:05:26"], {"Amount": 1500})
    assert str(DBapi.records("GET", [1, 1, "2020-09-03 10:05:26"])) == "[[1, 1, datetime.datetime(2020, 9, 3, 10, 5, 26), 1500.0]]"
    AbcTable._cur.execute("ROLLBACK;")

def test_delete_record():
    AbcTable._cur.execute("BEGIN;")
    DBapi.records("DELETE", [1, 1, "2020-09-03 10:05:26"])
    assert len(DBapi.records("GET")) == 2
    AbcTable._cur.execute("ROLLBACK;")

def test_exceptions_record():
    with pytest.raises(Exception, match="Missing data"):
        DBapi.records("POST")
    with pytest.raises(Exception, match="Missing data"):
        DBapi.records("PUT", [1])
    with pytest.raises(Exception, match="Missing id"):
        DBapi.records("PUT")
    with pytest.raises(Exception, match="Missing id"):
        DBapi.records("DELETE")
    with pytest.raises(Exception, match="Method not in list of approved methods: GET, POST, PUT, DELETE"):
        DBapi.records("test")
