import pytest

from main.services.db_api import DBapi
from main.services.pg_api import PGapi
from main.util.mappers.habit import Habit
from tests.database.test_base import TestBase

DBapi = DBapi(PGapi)

class TestHabitDB(TestBase):
    def test_get_single_habit(self):
        assert len(DBapi.habits("GET", 1)) == 1

    def test_get_habit_list(self):
        assert len(DBapi.habits("GET")) == 4

    def test_post_habit(self):
        self.begin()
        new_habit = Habit(userid=1, name="Test habit", description="My test habit", measurementid=4)
        DBapi.habits("POST", data=new_habit)
        assert len(DBapi.habits("GET")) == 5
        self.rollback()

    def test_put_habit(self):
        self.begin()
        updated_habit = Habit(name="TEST")
        DBapi.habits("PUT", 1, updated_habit)
        assert DBapi.habits("GET", 1)[0].name == "TEST"
        self.rollback()

    def test_delete_habit(self):
        self.begin()
        DBapi.habits("DELETE", 2)
        assert len(DBapi.habits("GET")) == 3
        self.rollback()

    def test_exceptions_type(self):
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
