from main.services.db_api import DBapi
from tests.database.test_base import TestBase

class TestPasswordDB(TestBase):
    def test_correct_password(self):
        assert DBapi.checkpassword("scowdroy0", "yV3wwHgvnQWe")[0][0]

    def test_incorrect_password(self):
        assert not DBapi.checkpassword("TEST", "INCORRECT")[0][0]
