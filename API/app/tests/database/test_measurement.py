from main.services.db_api import DBapi
from main.services.pg_api import PGapi
from tests.database.test_base import TestBase

DBapi = DBapi(PGapi)

class TestMeasurementDB(TestBase):
    def test_get_single_measurement(self):
        assert len(DBapi.measurements(1)) == 1

    def test_get_measurements_list(self):
        assert len(DBapi.measurements()) == 5
