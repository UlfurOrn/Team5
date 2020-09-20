from unittest.mock import patch

from main.util.mappers.user import User
from tests.endpoints.test_base import TestBase


@patch("main.controller.user_controller.DBapi.checkpassword")
class TestAuthenticationEndpoint(TestBase):
    def setUp(self):
        super(TestAuthenticationEndpoint, self).setUp()

        self.test_user_mapper = User(1, "testuser", "testuser@email.com", 'testuser', 'testpassword', "2020-04-25T00:00:00", "m", 85, 180)

    def test_login_working(self, mock_db):
        mock_db.return_value = [[True]]

        login_credentails = {'username': self.test_user_mapper.username, 'password': self.test_user_mapper.password}

        response = self.app.post("/auth/login", headers=self.valid_header, json=login_credentails)
        data = response.json

        assert data == "successfully logged in"
        assert response.status_code == 200
        mock_db.assert_called_once()

    def test_login_failing(self, mock_db):
        mock_db.return_value = [[False]]

        login_credentails = {'username': self.test_user_mapper.username, 'password': self.test_user_mapper.password}

        response = self.app.post("/auth/login", headers=self.valid_header, json=login_credentails)
        data = response.json

        assert data == "couldn't log in"
        assert response.status_code == 404
        mock_db.assert_called_once()
