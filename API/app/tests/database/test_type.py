from main.services.db_api import DBapi
from main.services.abc_table import AbcTable
import psycopg2
from psycopg2 import extras
import pytest

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_type():
    assert len(DBapi.types("GET", 1)) == 1

def test_get_type_list():
    assert len(DBapi.types("GET")) == 3

def test_post_type():
    AbcTable._cur.execute("BEGIN;")
    DBapi.types("POST", data={"name": "testType", "description": "A test type", "measurement": "Coverage"})
    assert len(DBapi.types("GET")) == 4
    AbcTable._cur.execute("ROLLBACK;")

def test_put_type():
    AbcTable._cur.execute("BEGIN;")
    DBapi.types("PUT", 1, {"name": "Vatn", "description": "Drykkur"})
    assert str(DBapi.types("GET", 1)) == "[[1, 'Vatn', 'Drykkur', 'mL']]"
    AbcTable._cur.execute("ROLLBACK;")

def test_delete_type():
    AbcTable._cur.execute("BEGIN;")
    DBapi.types("DELETE", 2)
    assert len(DBapi.types("GET")) == 2
    AbcTable._cur.execute("ROLLBACK;")

def test_exceptions_type():
    pass
