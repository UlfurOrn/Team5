import pytest
import psycopg2
from psycopg2 import extras

from main.services.db_api import DBapi
from main.repositories.abc_table import AbcTable
from main.util.mappers.habit import Habit

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest2 user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_habit():
    assert len(DBapi.habits("GET", 1)) == 1


def test_get_habit_list():
    assert len(DBapi.habits("GET")) == 4


def test_post_habit():
    AbcTable._cur.execute("BEGIN;")
    new_habit = Habit(userid=1, name="Test habit", description="My test habit", measurementid=4)
    DBapi.habits("POST", data=new_habit)
    assert len(DBapi.habits("GET")) == 5
    AbcTable._cur.execute("ROLLBACK;")


def test_put_habit():
    AbcTable._cur.execute("BEGIN;")
    updated_habit = Habit(name="TEST")
    DBapi.habits("PUT", 1, updated_habit)
    assert DBapi.habits("GET", 1)[0].name == "TEST"
    AbcTable._cur.execute("ROLLBACK;")


def test_delete_habit():
    AbcTable._cur.execute("BEGIN;")
    DBapi.habits("DELETE", 2)
    assert len(DBapi.habits("GET")) == 3
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
