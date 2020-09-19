from main.services.db_api import DBapi
from main.services.abc_table import AbcTable
import psycopg2
from psycopg2 import extras
import pytest

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest2 user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_mcategory():
    assert len(DBapi.mcategories("GET", 1)) == 1

def test_get_mcategories_list():
    assert len(DBapi.mcategories("GET")) == 4