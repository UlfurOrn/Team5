from main.services.db_api import DBapi
from main.repositories.abc_table import AbcTable
from main.util.mappers.record import Record
import psycopg2
from psycopg2 import extras
import pytest

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest2 user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_record():
    assert len(DBapi.records("GET", 1)) == 1


def test_get_record_list():
    assert len(DBapi.records("GET")) == 4


def test_post_record():
    AbcTable._cur.execute("BEGIN;")
    new_record = Record(userid=1, habitid=1, amount=10, rdate='2020-06-06', rtime='10:10:10')
    DBapi.records("POST", data=new_record)
    assert len(DBapi.records("GET")) == 5
    AbcTable._cur.execute("ROLLBACK;")


def test_put_record():
    AbcTable._cur.execute("BEGIN;")
    updated_record = Record(amount = 10)
    DBapi.records("PUT", 1, updated_record)
    assert DBapi.records("GET", 1)[0].amount == 10
    AbcTable._cur.execute("ROLLBACK;")


def test_delete_record():
    AbcTable._cur.execute("BEGIN;")
    DBapi.records("DELETE", 1)
    assert len(DBapi.records("GET")) == 3
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
