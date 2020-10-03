import pytest

from main.services.db_api import DBapi
from main.services.pg_api import PGapi
from main.util.mappers.record import RecordMapper
from tests.database.test_base import TestBase

DBapi = DBapi(PGapi)

class TestRecordDB(TestBase):
    def test_get_single_record(self):
        assert len(DBapi.records("GET", 1)) == 1

    def test_get_record_list(self):
        assert len(DBapi.records("GET")) == 4

    def test_post_record(self):
        self.begin()
        new_record = RecordMapper(userid=1, habitid=1, amount=10, rdate='2020-06-06', rtime='10:10:10')
        DBapi.records("POST", data=new_record)
        assert len(DBapi.records("GET")) == 5
        self.rollback()

    def test_put_record(self):
        self.begin()
        updated_record = RecordMapper(amount=10)
        DBapi.records("PUT", 1, updated_record)
        assert DBapi.records("GET", 1)[0].amount == 10
        self.rollback()

    def test_delete_record(self):
        self.begin()
        DBapi.records("DELETE", 1)
        assert len(DBapi.records("GET")) == 3
        self.rollback()

    def test_exceptions_record(self):
        with pytest.raises(Exception, match="Missing data"):
            DBapi.records("POST")
        with pytest.raises(Exception, match="Missing data"):
            DBapi.records("PUT", [1])
        with pytest.raises(Exception, match="Missing id"):
            DBapi.records("PUT")
        with pytest.raises(Exception, match="Missing id"):
            DBapi.records("DELETE")
        with pytest.raises(Exception, match="Method not in list of approved methods: GET, POST, PUT, DELETE"):
            DBapi.records("test")
