import pytest

def test_index(client, auth):
    auth.login()
    response = client.get("/habit/")
    assert b'User Habits' in response.data

@pytest.mark.parametrize('path', (
    '/habit/',
    '/habit/1',
    '/habit/1/update',
    '/habit/1/delete',
    '/habit/add'
))
def test_login_required(client, auth, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'

def test_add_habit(client, auth):
    auth.login()
    response = client.get('/habit/add')
    assert b'Add Habit' in response.data

    response = client.post('/habit/add', data={'name': 'test', 'description': 'test habit', 'measurement': '1'})
    assert response.status_code == 302


# These tests need to be reconfigured...
# def test_single_habit(client, auth):
#     auth.login()
#     response = client.get('/habit/%7B%27habitid%27:%2047%2C%20%27userid%27:%2062%2C%20%27name%27:%20%27test%27%2C%20%27description%27:%20%27test%20habit%27%2C%20%27measurementid%27:%201%7D')
    
#     assert response.status_code == 302

# def test_delete_habit(client, auth):
#     auth.login()
#     response = client.get('/habit/%7B%27habitid%27:%2047%2C%20%27userid%27:%2062%2C%20%27name%27:%20%27test%27%2C%20%27description%27:%20%27test%20habit%27%2C%20%27measurementid%27:%201%7D/delete')

#     assert response.status_code == 302