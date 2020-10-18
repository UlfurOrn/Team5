from unittest.mock import patch

from main.util.mappers.habitmapper import HabitMapper
from tests.endpoints.test_base import TestBase


class TestHabitEndpoint(TestBase):

    def setUp(self):
        super(TestHabitEndpoint, self).setUp()

        self.test_habit_mapper = HabitMapper(1, 1, "TestHabit", "Testing Test Habit", 1)
        self.test_habit_dict = {
            "habitid": 1, "userid": 1, "name": "TestHabit", "description": "Testing Test Habit", "measurementid": 1
        }

    @patch("main.controller.habit_controller.check_id")
    @patch("main.controller.habit_controller.DBapi.habits.get")
    def test_get_single_habit(self, mock_db, mock_check):
        mock_db.return_value = [self.test_habit_mapper]  # DB returns habit in a list

        response = self.app.get("habit/1", headers=self.valid_header)
        data = response.json

        assert data == self.test_habit_dict
        mock_check.assert_called_once_with(1)
        mock_db.assert_called_once_with(1)

    @patch("main.controller.habit_controller.DBapi.habits.get")
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
        mock_db.assert_called_once()

    @patch("main.controller.habit_controller.DBapi.habits.post")
    def test_post_habit(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/habit", headers=self.valid_header, json=self.test_habit_dict)
        data = response.json

        assert data is None
        mock_db.assert_called_once()

    @patch("main.controller.habit_controller.check_id")
    @patch("main.controller.habit_controller.DBapi.habits.get")
    @patch("main.controller.habit_controller.DBapi.habits.put")
    def test_put_habit(self, mock_db, mock_get, mock_check):
        mock_get.return_value = [self.test_habit_mapper]

        response = self.app.put("/habit/1", headers=self.valid_header, json=self.test_habit_dict)
        data = response.json

        assert data == self.test_habit_dict
        assert response.status_code == 201

        mock_check.assert_called_once_with(1)
        mock_get.assert_called_once_with(1)
        mock_db.assert_called_once()

    @patch("main.controller.habit_controller.check_id")
    @patch("main.controller.habit_controller.DBapi.habits.delete")
    def test_delete_habit(self, mock_db, mock_check):
        response = self.app.delete("/habit/1", headers=self.valid_header)
        data = response.json

        assert data == ""
        assert response.status_code == 200
        mock_check.assert_called_once_with(1)
        mock_db.assert_called_once_with(1)

    def test_bad_request_exception(self):
        response_list = [
            self.app.get("habit/0", headers=self.valid_header),
            self.app.put("habit/0", headers=self.valid_header, json=self.test_habit_dict),
            self.app.delete("habit/0", headers=self.valid_header)
        ]

        for response in response_list:
            assert response.json["message"] == "Habit id must be higher than 0"
            assert response.status_code == 400

    @patch("main.controller.habit_controller.DBapi.habits.get")
    def test_not_found_exception(self, mock_get):
        mock_get.return_value = False
        response_list = [
            self.app.get("habit/1", headers=self.valid_header),
            self.app.put("habit/1", headers=self.valid_header, json=self.test_habit_dict),
            self.app.delete("habit/1", headers=self.valid_header)
        ]

        for response in response_list:
            assert response.json["message"] == "Habit with id 1 not found"
            assert response.status_code == 404
