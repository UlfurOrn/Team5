import pytest

from main.services.db_api import DBapi
from main.services.pg_api import PGapi
from main.util.mappers.user import UserMapper
from tests.database.test_base import TestBase

DBapi = DBapi(PGapi)

class TestUserDB(TestBase):
    def test_get_single_user(self):
        assert len(DBapi.users("GET", 1)) == 1

    def test_get_user_list(self):
        assert len(DBapi.users("GET")) == 5

    def test_post_user(self):
        self.begin()
        new_user = UserMapper(name="testuser", email="testemail", username="testusername", password="PASSWORD")
        DBapi.users("POST", data=new_user)
        assert len(DBapi.users("GET")) == 6
        self.rollback()

    def test_put_user(self):
        self.begin()
        updated_user = UserMapper(name="TESTNAME")
        DBapi.users("PUT", 1, updated_user)
        assert DBapi.users("GET", 1)[0].name == "TESTNAME"
        self.rollback()

    def test_delete_user(self):
        self.begin()
        assert len(DBapi.users("GET")) == 5
        DBapi.users("DELETE", 3)
        assert len(DBapi.users("GET")) == 4
        self.rollback()

    def test_exceptions_user(self):
        with pytest.raises(Exception, match="Missing data"):
            DBapi.users("POST")
        with pytest.raises(Exception, match="Missing data"):
            DBapi.users("PUT", 1)
        with pytest.raises(Exception, match="Missing id"):
            DBapi.users("PUT")
        with pytest.raises(Exception, match="Missing id"):
            DBapi.users("DELETE")
        with pytest.raises(Exception, match="Method not in list of approved methods: GET, POST, PUT, DELETE"):
            DBapi.users("test")
