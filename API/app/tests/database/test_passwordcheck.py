from main.services.db_api import DBapi
from main.repositories.abc_table import AbcTable
import psycopg2
from psycopg2 import extras
import pytest

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest2 user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_correct_password():
    assert DBapi.checkpassword("scowdroy0", "yV3wwHgvnQWe")[0][0]


def test_incorrect_password():
    assert not DBapi.checkpassword("TEST", "INCORRECT")[0][0]
