from unittest.mock import patch

from tests.endpoints.test_base import TestBase


@patch("main.controller.user_controller.DBapi.users")
class TestUserEndpoint(TestBase):
    def setUp(self):
        super(TestUserEndpoint, self).setUp()

        self.test_user = {
            'name': "testuser",
            'email': "testuser@email.com",
            'dob': "2020-04-25T00:00:00",
            'gender': "m",
            'weight': 85,
            'height': 180
        }

    def test_get_single_user(self, mock_db):
        mock_db.return_value = [self.test_user]

        response = self.app.get("user/1")
        data = response.json

        assert data == self.test_user
        mock_db.assert_called_once_with('GET', '1')

    def test_get_user_list(self, mock_db):
        test_user_list = [
            {
                'name': "testuser",
                'email': "test@email.com",
                'dob': "2020-04-25T00:00:00",
                'gender': "m",
                'weight': 85,
                'height': 180
            },
            {
                'name': "testuser2",
                'email': "test2@email.com",
                'dob': "2020-05-25T00:00:00",
                'gender': "f",
                'weight': 60,
                'height': 170
            }
        ]

        mock_db.return_value = test_user_list

        response = self.app.get("/user")
        data = response.json

        assert data == {
            "users": test_user_list
        }
        mock_db.assert_called_once_with('GET')

    def test_post_user(self, mock_db):
        mock_db.return_value = None

        response = self.app.post("/user", headers=self.valid_header, json=self.test_user)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("POST", data=self.test_user)

    def test_put_user(self, mock_db):
        mock_db.return_value = None

        response = self.app.put("/user/1", headers=self.valid_header, json=self.test_user)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("PUT", "1", data=self.test_user)

    def test_delete_user(self, mock_db):
        mock_db.return_value = None

        response = self.app.delete("/user/1", headers=self.valid_header)
        data = response.json

        assert data is None
        mock_db.assert_called_once_with("DELETE", "1")
