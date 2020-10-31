import pytest

def test_account(client, auth):
    response = client.get("/account")
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get("/account")
    assert b"User Habits" in response.data
    assert b"Log Out" in response.data
    assert b"View Account" in response.data
    assert b"habits" in response.data
    assert b"records" in response.data