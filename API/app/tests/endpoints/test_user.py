from unittest.mock import patch

from main.util.mappers.usermapper import UserMapper
from tests.endpoints.test_base import TestBase


@patch("main.controller.user_controller.DBapi.users")
class TestUserEndpoint(TestBase):
    def setUp(self):
        super(TestUserEndpoint, self).setUp()

        self.test_user_mapper = UserMapper(
            1, "testuser", "testuser@email.com", 'testuser', 'testpassword', "2020-04-25T00:00:00", "m", 85, 180
        )
        self.test_user_dict = {
            'userid': 1,
            'name': "testuser",
            'email': "testuser@email.com",
            'dob': "2020-04-25",
            'username': 'testuser',
            'password': 'testpassword',
            'gender': "m",
            'weight': 85,
            'height': 180
        }

    def test_get_single_user(self, mock_db):
        mock_db.return_value = [self.test_user_mapper]

        response = self.app.get("user/1")
        data = response.json

        assert data == self.test_user_dict
        mock_db.assert_called_once_with('GET', '1')

    def test_get_user_list(self, mock_db):
        test_user_list_insert = [
            UserMapper(1, "testuser", "test@email.com", 'testuser', 'testpassword', "2020-04-25T00:00:00", "m", 85, 180),
            UserMapper(2, "testuser2", "test2@email.com", 'testuser2', 'testpassword2', "2020-05-25T00:00:00", "f", 60, 170)
        ]

        test_user_list = [
            {
                'userid': 1,
                'name': "testuser",
                'email': "test@email.com",
                'dob': "2020-04-25",
                'username': 'testuser',
                'password': 'testpassword',
                'gender': "m",
                'weight': 85,
                'height': 180
            },
            {
                'userid': 2,
                'name': "testuser2",
                'email': "test2@email.com",
                'dob': "2020-05-25",
                'username': 'testuser2',
                'password': 'testpassword2',
                'gender': "f",
                'weight': 60,
                'height': 170
            }
        ]

        mock_db.return_value = test_user_list_insert

        response = self.app.get("/user")
        data = response.json

        assert data == {
            "users": test_user_list
        }
        mock_db.assert_called_once_with('GET')

    def test_post_user(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/user", headers=self.valid_header, json=self.test_user_dict)
        data = response.json

        assert data is None
        mock_db.assert_called_once()

    def test_put_user(self, mock_db):
        mock_db.return_value = None

        response = self.app.put("/user/1", headers=self.valid_header, json=self.test_user_dict)
        data = response.json

        assert data is None
        mock_db.assert_called_once()

    def test_delete_user(self, mock_db):
        mock_db.return_value = None

        response = self.app.delete("/user/1", headers=self.valid_header)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("DELETE", "1")
