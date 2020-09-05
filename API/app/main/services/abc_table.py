import psycopg2
from psycopg2 import extras
from abc import ABC, abstractclassmethod


class AbcTable(ABC):
    """
        An abstract class that provides unfilled class methods for all 4 CRUD operations on a table in the Habit tracker database.
        Has connection objects to the database and a cursor that can be called with super()._cur.
    """
    __conn = psycopg2.connect("dbname=habittracker user=habitapi password=habitapi123&  host=gudjoniv.com")
    __conn.autocommit = True
    _cur = __conn.cursor(cursor_factory=extras.DictCursor)

    @abstractclassmethod
    def get(cls, id):
        pass

    @abstractclassmethod
    def post(cls, data):
        pass

    @abstractclassmethod
    def put(cls, id, data):
        pass

    @abstractclassmethod
    def delete(cls, id):
        pass