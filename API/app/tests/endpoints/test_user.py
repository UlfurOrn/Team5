from unittest.mock import patch

from main.util.mappers.usermapper import UserMapper
from tests.endpoints.test_base import TestBase


class TestUserEndpoint(TestBase):
    def setUp(self):
        super(TestUserEndpoint, self).setUp()

        self.test_user_mapper = UserMapper(
            1, "testuser", "testuser@email.com", 'testuser', 'testpassword', "2020-04-25", "m", 85, 180
        )
        self.test_user_dict = {
            'userid': 1,
            'name': "testuser",
            'email': "testuser@email.com",
            'username': 'testuser',
            'password': 'testpassword',
            'dob': "2020-04-25",
            'gender': "m",
            'weight': 85,
            'height': 180
        }

    @patch("main.controller.user_controller.check_id")
    @patch("main.controller.user_controller.DBapi.users.get")
    def test_get_single_user(self, mock_db, mock_check):
        mock_db.return_value = [self.test_user_mapper]

        response = self.app.get("user/1")
        data = response.json

        assert data == self.test_user_dict
        mock_check.assert_called_once_with(1)
        mock_db.assert_called_once_with(1)

    @patch("main.controller.user_controller.DBapi.users.get")
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
        mock_db.assert_called_once()

    @patch("main.controller.user_controller.DBapi.users.post")
    def test_post_user(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/user", headers=self.valid_header, json=self.test_user_dict)
        data = response.json

        assert data is None
        mock_db.assert_called_once()

    @patch("main.controller.user_controller.check_id")
    @patch("main.controller.user_controller.DBapi.users.get")
    @patch("main.controller.user_controller.DBapi.users.put")
    def test_put_user(self, mock_db, mock_get, mock_check):
        mock_get.return_value = [self.test_user_mapper]

        response = self.app.put("/user/1", headers=self.valid_header, json=self.test_user_dict)
        data = response.json

        assert data == self.test_user_dict
        assert response.status_code == 201

        mock_check.assert_called_once_with(1)
        mock_get.assert_called_once_with(1)
        mock_db.assert_called_once()

    @patch("main.controller.user_controller.check_id")
    @patch("main.controller.user_controller.DBapi.users.delete")
    def test_delete_user(self, mock_db, mock_check):
        response = self.app.delete("/user/1", headers=self.valid_header)
        data = response.json

        assert data == ""
        assert response.status_code == 200
        mock_check.assert_called_once_with(1)
        mock_db.assert_called_once_with(1)

    def test_bad_request_exception(self):
        response_list = [
            self.app.get("user/0", headers=self.valid_header),
            self.app.put("user/0", headers=self.valid_header, json=self.test_user_dict),
            self.app.delete("user/0", headers=self.valid_header),
            self.app.get("user/0/habit", headers=self.valid_header),
            self.app.get("user/0/record", headers=self.valid_header)
        ]

        for response in response_list:
            assert response.json["message"] == "User id must be higher than 0"
            assert response.status_code == 400

    @patch("main.controller.user_controller.DBapi.users.get")
    def test_not_found_exception(self, mock_get):
        mock_get.return_value = False
        response_list = [
            self.app.get("user/1", headers=self.valid_header),
            self.app.put("user/1", headers=self.valid_header, json=self.test_user_dict),
            self.app.delete("user/1", headers=self.valid_header),
            self.app.get("user/1/habit", headers=self.valid_header),
            self.app.get("user/1/record", headers=self.valid_header)
        ]

        for response in response_list:
            assert response.json["message"] == "User with id 1 not found"
            assert response.status_code == 404
