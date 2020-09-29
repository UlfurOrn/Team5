import unittest
import psycopg2
from psycopg2 import extras

from main.repositories.abc_table import AbcTable


class TestBase(unittest.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()

        AbcTable._conn = psycopg2.connect(
            "dbname=habittest2 user=habittester password=tester123  host=gudjoniv.com"
        )
        AbcTable._conn.autocommit = True
        AbcTable._cur = AbcTable._conn.cursor(cursor_factory=extras.DictCursor)

    def begin(self):
        AbcTable._cur.execute("BEGIN;")

    def rollback(self):
        AbcTable._cur.execute("ROLLBACK;")
