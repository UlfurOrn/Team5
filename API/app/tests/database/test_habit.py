from main.services.db_api import DBapi
from main.services.abc_table import AbcTable
import psycopg2
from psycopg2 import extras
import pytest

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest2 user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_type():
    assert len(DBapi.habits("GET", 1)) == 1

def test_get_type_list():
    assert len(DBapi.habits("GET")) == 3

"""def test_post_type():
    AbcTable._cur.execute("BEGIN;")
    DBapi.habits("POST", data={"name": "testType", "description": "A test type", "measurement": "Coverage"})
    assert len(DBapi.habits("GET")) == 4
    AbcTable._cur.execute("ROLLBACK;")

def test_put_type():
    AbcTable._cur.execute("BEGIN;")
    DBapi.habits("PUT", 1, {"name": "Vatn", "description": "Drykkur"})
    assert str(DBapi.habits("GET", 1)) == "[[1, 'Vatn', 'Drykkur', 'mL']]"
    AbcTable._cur.execute("ROLLBACK;")"""

def test_delete_type():
    AbcTable._cur.execute("BEGIN;")
    DBapi.habits("DELETE", 2)
    assert len(DBapi.habits("GET")) == 2
    AbcTable._cur.execute("ROLLBACK;")

def test_exceptions_type():
    with pytest.raises(Exception, match="Missing data"):
        DBapi.habits("POST")
    with pytest.raises(Exception, match="Missing data"):
        DBapi.habits("PUT", 1)
    with pytest.raises(Exception, match="Missing id"):
        DBapi.habits("PUT")
    with pytest.raises(Exception, match="Missing id"):
        DBapi.habits("DELETE")
    with pytest.raises(Exception, match="Method not in list of approved methods: GET, POST, PUT, DELETE"):
        DBapi.habits("test")