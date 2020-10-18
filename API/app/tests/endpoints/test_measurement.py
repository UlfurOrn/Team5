from unittest.mock import patch

from main.util.mappers.measurementmapper import MeasurementMapper
from tests.endpoints.test_base import TestBase


class TestMeasurementEndpoint(TestBase):
    def setUp(self):
        super(TestMeasurementEndpoint, self).setUp()

    @patch("main.controller.measurement_controller.check_id")
    @patch("main.controller.measurement_controller.DBapi.measurements.get")
    def test_get_single_measurement(self, mock_db, mock_check):
        test_measurement = {
            "measurementid": 1,
            "name": "Kilometers",
            "abreviation": "km",
            "mcategoryid": 1
        }
        test_measurement_mapper = MeasurementMapper(**test_measurement)

        mock_db.return_value = [test_measurement_mapper]

        response = self.app.get("measurement/1")
        data = response.json

        assert data == test_measurement
        mock_check.assert_called_once_with(1)
        mock_db.assert_called_once_with(1)

    @patch("main.controller.measurement_controller.DBapi.measurements.get")
    def test_get_measurement_list(self, mock_db):
        test_measurement_list = [
            {
                "measurementid": 1,
                "name": "Kilometers",
                "abreviation": "km",
                "mcategoryid": 1
            },
            {
                "measurementid": 2,
                "name": "Meters",
                "abreviation": "m",
                "mcategoryid": 1
            }
        ]

        test_measurement_mapper_list = [
            MeasurementMapper(**measurement_dict)
            for measurement_dict in test_measurement_list
        ]

        mock_db.return_value = test_measurement_mapper_list

        response = self.app.get("/measurement")
        data = response.json

        assert data == {
            "measurements": test_measurement_list
        }
        mock_db.assert_called_once()
