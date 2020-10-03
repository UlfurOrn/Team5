from unittest.mock import patch

from main.util.mappers.habit import HabitMapper
from tests.endpoints.test_base import TestBase


@patch("main.controller.habit_controller.DBapi.habits")
class TestHabitEndpoint(TestBase):

    def setUp(self):
        super(TestHabitEndpoint, self).setUp()

        self.test_habit_mapper = HabitMapper(1, 1, "TestHabit", "Testing Test Habit", 1)
        self.test_habit_dict = {
            "habitid": 1, "userid": 1, "name": "TestHabit", "description": "Testing Test Habit", "measurementid": 1
        }

    def test_get_single_habit(self, mock_db):
        mock_db.return_value = [self.test_habit_mapper]  # DB returns habit in a list

        response = self.app.get("habit/1", headers=self.valid_header)
        data = response.json

        assert data == self.test_habit_dict
        mock_db.assert_called_once_with('GET', "1")

    def test_get_habit_list(self, mock_db):
        test_habit_list_insert = [
            HabitMapper(1, 1, "TestHabit1", "Testing Habit 1", 1),
            HabitMapper(2, 1, "TestHabit2", "Testing Habit 2", 2),
            HabitMapper(3, 1, "TestHabit3", "Testing Habit 3", 3)
        ]
        test_habit_list = [
            {"habitid": 1, "userid": 1, "name": "TestHabit1", "description": "Testing Habit 1", "measurementid": 1},
            {"habitid": 2, "userid": 1, "name": "TestHabit2", "description": "Testing Habit 2", "measurementid": 2},
            {"habitid": 3, "userid": 1, "name": "TestHabit3", "description": "Testing Habit 3", "measurementid": 3}
        ]

        mock_db.return_value = test_habit_list_insert

        response = self.app.get("/habit", headers=self.valid_header)
        data = response.json

        assert data == {
            "habits": test_habit_list
        }
        mock_db.assert_called_once_with("GET")

    def test_post_habit(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/habit", headers=self.valid_header, json=self.test_habit_dict)
        data = response.json

        assert data is None
        mock_db.assert_called_once()

    def test_put_habit(self, mock_db):
        mock_db.return_value = None

        response = self.app.put("/habit/1", headers=self.valid_header, json=self.test_habit_dict)
        data = response.json

        assert data is None
        mock_db.assert_called_once()

    def test_delete_habit(self, mock_db):
        mock_db.return_value = None

        response = self.app.delete("/habit/1", headers=self.valid_header)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("DELETE", "1")
