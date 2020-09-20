from unittest.mock import patch

from main.util.mappers.user import User
from tests.endpoints.test_base import TestBase


@patch("main.controller.user_controller.DBapi.users")
class TestAuthenticationEndpoint(TestBase):
    def setUp(self):
        super(TestAuthenticationEndpoint, self).setUp()

        self.test_user_mapper = User(1, "testuser", "testuser@email.com", 'testuser', 'testpassword', "2020-04-25T00:00:00", "m", 85, 180)

    def test_login(self, mock_db):
        mock_db.return_value = [self.test_user_mapper]

        login_credentails = {'username': self.test_user_mapper.username, 'password': self.test_user_mapper.password}
        print(login_credentails)

        response = self.app.post("/auth/login", headers=self.valid_header, json=login_credentails)
        data = response.json

        assert data == "successfully logged in"
        mock_db.assert_called_once()
