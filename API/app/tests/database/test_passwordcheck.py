from main.services.db_api import DBapi
from main.services.pg_api import PGapi
from tests.database.test_base import TestBase

DBapi = DBapi(PGapi)

class TestPasswordDB(TestBase):
    def test_correct_password(self):
        assert DBapi.checkpassword("scowdroy0", "yV3wwHgvnQWe")[0][0]

    def test_incorrect_password(self):
        assert not DBapi.checkpassword("TEST", "INCORRECT")[0][0]
