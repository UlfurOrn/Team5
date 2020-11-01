import pytest

def test_index(client, auth):
    auth.login()
    response = client.get("/habit/records")
    assert b'User Records' in response.data

@pytest.mark.parametrize('path', (
    '/habit/records',
    '/habit/records/1',
    '/habit/records/1/update',
    '/habit/records/1/delete'
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'