from unittest.mock import patch

from main.util.mappers.usermapper import UserMapper
from tests.endpoints.test_base import TestBase


@patch("main.controller.auth_controller.DBapi.users.checkpassword")
class TestAuthenticationEndpoint(TestBase):

    def get_login(self, username, password):
        return {
            "username": username,
            "password": password
        }

    def test_valid_authentication(self, mock_db):
        mock_db.return_value = [[True]]

        username = "Valid Username"
        password = "Valid Password"
        login_credentials = self.get_login(username, password)

        response = self.app.post("/auth/login", headers=self.valid_header, json=login_credentials)
        data = response.json

        assert data == "Login Successful"
        assert response.status_code == 200
        mock_db.assert_called_once_with(username, password)

    def test_login_forbidden(self, mock_db):
        mock_db.return_value = [[False]]

        username = "Invalid Username"
        password = "Invalid Password"
        login_credentials = self.get_login(username, password)

        response = self.app.post("/auth/login", headers=self.valid_header, json=login_credentials)
        data = response.json

        assert data["message"] == "Invalid username or password"
        assert response.status_code == 403
        mock_db.assert_called_once_with(username, password)

    def test_login_unauthorized(self, mock_db):
        login_credentials = self.get_login("", "")

        response = self.app.post("/auth/login", headers=self.valid_header, json=login_credentials)
        data = response.json

        assert data["message"] == "Missing username and password"
        assert response.status_code == 401
        mock_db.assert_not_called()
