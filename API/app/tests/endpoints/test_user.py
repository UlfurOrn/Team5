from main.services.db_api import DBapi
from main.services.abc_table import AbcTable
from unittest.mock import patch
import psycopg2
from psycopg2 import extras

# This connects the AbcTable to another designated test database
AbcTable._conn = psycopg2.connect("dbname=habittest user=habittester password=tester123  host=gudjoniv.com")
AbcTable._conn.autocommit = True
AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)


def test_get_single_user():
    assert len(DBapi.users("GET", 1)) == 1

def test_get_user_list():
    assert len(DBapi.users("GET")) == 3

def test_post_user():
    AbcTable._cur.execute("BEGIN;")
    DBapi.users("POST", data={"name": "test",
                              "email": "test", 
                              "dob": "2000-10-02", 
                              "gender": "f", 
                              "weight": 50, 
                              "height": 160})
    assert len(DBapi.users("GET")) == 4
    AbcTable._cur.execute("ROLLBACK;")

def test_put_user():
    AbcTable._cur.execute("BEGIN;")
    DBapi.users("PUT", 1, {"name": "puttest", "gender": "f"})
    assert str(DBapi.users("GET", 1)) == "[[1, 'puttest', 'test@email.com', datetime.date(2020, 4, 25), 'f', 85, 180]]"
    AbcTable._cur.execute("ROLLBACK;")

def test_delete_user():
    AbcTable._cur.execute("BEGIN;")
    assert len(DBapi.users("GET")) == 3
    DBapi.users("DELETE", 3)
    assert len(DBapi.users("GET")) == 2
    AbcTable._cur.execute("ROLLBACK;")
