from main.services.db_api import DBapi
from tests.database.test_base import TestBase


class TestMeasurementDB(TestBase):
    def test_get_single_measurement(self):
        assert len(DBapi.measurements(1)) == 1

    def test_get_measurements_list(self):
        assert len(DBapi.measurements()) == 5
