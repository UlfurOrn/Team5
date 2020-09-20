import requests
from unittest.mock import patch

from tests.endpoints.test_base import TestBase


@patch("main.controller.habit_controller.DBapi.habits")
class TestHabitEndpoint(TestBase):

    def setUp(self):
        super(TestHabitEndpoint, self).setUp()

        self.test_habit = {
            'name': "TestHabit",
            'description': "Testing Test Habit",
            'measurement': "1234.5678"
        }

    def test_get_single_habit(self, mock_db):
        mock_db.return_value = [self.test_habit]  # DB returns habit in a list

        response = self.app.get("habit/1", headers=self.valid_header)
        data = response.json

        assert data == self.test_habit
        mock_db.assert_called_once_with('GET', "1")

    def test_get_habit_list(self, mock_db):
        test_habit_list = [
            {
                'name': "TestHabit1",
                'description': "Testing Test Habit 1",
                'measurement': "1234.5678"
            },
            {
                'name': "TestHabit2",
                'description': "Testing Test Habit 2",
                'measurement': "8765.4321"
            },
            {
                'name': "TestHabit3",
                'description': "Testing Test Habit 3",
                'measurement': "1234"
            }
        ]

        mock_db.return_value = test_habit_list

        response = self.app.get("/habit", headers=self.valid_header)
        data = response.json

        assert data == {
            "habits": test_habit_list
        }
        mock_db.assert_called_once_with("GET")

    def test_post_habit(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/habit", headers=self.valid_header, json=self.test_habit)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("POST", data=self.test_habit)

    def test_put_habit(self, mock_db):
        mock_db.return_value = None

        response = self.app.put("/habit/1", headers=self.valid_header, json=self.test_habit)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("PUT", "1", data=self.test_habit)

    def test_delete_habit(self, mock_db):
        mock_db.return_value = None

        response = self.app.delete("/habit/1", headers=self.valid_header)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("DELETE", "1")
