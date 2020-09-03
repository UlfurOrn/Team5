import psycopg2
from psycopg2 import extras
from abc import ABC, abstractclassmethod

class Abctable(ABC):
    __conn = psycopg2.connect("dbname=habittracker user=habitapi password=habitapi123&  host=gudjoniv.com")
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