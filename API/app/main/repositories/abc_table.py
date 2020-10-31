import psycopg2
from psycopg2 import extras
from psycopg2.extensions import AsIs
from abc import ABC, abstractclassmethod


class AbcTable(ABC):
    """
        An abstract class that provides 3 concrete class methods and 1 abstract class method. It also
        provides a connection and a cursor to a postgresql database. The concrete class methods are
        post, put and delete which work on the table of cls.table with id cls.table_key. These are 
        class functions that need to be designated in the subclass for these 3 functions to work.
    """
    _conn = psycopg2.connect("dbname=habittracker2 user=habitapi password=habitapi123&  host=gudjoniv.com")
    _conn.autocommit = True
    _cur = _conn.cursor(cursor_factory=extras.DictCursor)
    table = ""
    table_key = ""

    @abstractclassmethod
    def get(cls, id):
        pass

    @classmethod
    def post(cls, data):
        """ Insert a new data (Mapper) into table of cls.table in the database """
        cls.test_connection()
        data_tuple = data.to_sql_insert()
        cls._cur.execute("INSERT INTO %s %s VALUES %s;", (AsIs(cls.table), AsIs(data_tuple[0]), AsIs(data_tuple[1])))

    @classmethod
    def put(cls, id, data):
        """ Update record with id, in table cls.table with key cls.table_key and update to new data of data Mapper """
        cls.test_connection()
        data_str = data.to_sql_update()
        cls._cur.execute("UPDATE %s SET %s WHERE %s = %s", (AsIs(cls.table), AsIs(data_str), AsIs(cls.table_key), id))

    @classmethod
    def delete(cls, id):
        """ Delete record from table cls.table with id of cls.table_key """
        cls.test_connection()
        cls._cur.execute("DELETE FROM %s WHERE %s = %s;", (AsIs(cls.table), AsIs(cls.table_key), id))
    
    @classmethod
    def test_connection(cls):
        """ A method that checks if connection to the database is still intact, if not opens connection/cursor again """
        try:
            cls._cur.execute("SELECT;")
        except psycopg2.InterfaceError:
            cls._conn = psycopg2.connect("dbname=habittracker2 user=habitapi password=habitapi123&  host=gudjoniv.com")
            cls._conn.autocommit = True
            cls._cur = cls._conn.cursor(cursor_factory=extras.DictCursor)