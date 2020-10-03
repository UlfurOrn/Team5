from main.services.db_api import DBapi
from main.services.pg_api import PGapi
from tests.database.test_base import TestBase

DBapi = DBapi(PGapi)

class TestCategoryDB(TestBase):
    def test_get_single_mcategory(self):
        assert len(DBapi.mcategories(1)) == 1

    def test_get_mcategories_list(self):
        assert len(DBapi.mcategories()) == 4
