import pytest

def test_account(client, auth):
    auth.login()
    response = client.get("/account")
    assert response.headers['Location'] == 'http://localhost/account/'
    response = client.get("/account/edit")
    assert b'Edit Account' in response.data
    response = client.get("/account/editpassword")
    assert b'Edit Password' in response.data

@pytest.mark.parametrize('path', (
    '/account/',
    '/account/edit',
    '/habit/editpassword'
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'

# def test_edit_account(client, auth):
#     auth.login()
#     response = client.post("/account/edit", data={"email"})

# def test_edit_password(client, auth):
#     auth.login()
#     response = client.post("/account/editpassword", data={'password1': '123', 'password2': '123'})
    
#     assert b'password successfully changed' in response.data
#     response = client.post("/account/editpassword", data={'password1': 'test', 'password2': 'test'})