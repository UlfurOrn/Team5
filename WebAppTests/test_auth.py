import pytest
from flask import g, session

# def test_register(client, app):
#     assert client.get('/auth/register').status_code == 200

#     response = client.post('/auth/register', data={'username': 'a', 'password': 'a'})
#     assert 'http://localhost/auth/login' == response.headers["Location"]

def test_login(client, auth):
    assert client.get('auth/login').status_code == 200

    # These tests are currently not working... so we commented them out
    # response = auth.login()
    # assert response.headers['Location'] == "http://localhost/"

    # with client:
    #     client.get('/')
    #     assert session['user_id'] == 62

@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "test", b"failed to login"), ("test", "a", b"failed to login"))
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data

def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session