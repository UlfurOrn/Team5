import requests

url = 'http://127.0.0.1:5000/'

def test_user_route():
    session = requests.Session()

    r = session.get(url + 'user')

    assert r.status_code == 200

def test_record_route():
    session = requests.Session()

    r = session.get(url + 'record')

    assert r.status_code == 200

def test_type_route():
    session = requests.Session()

    r = session.get(url + 'record')

    assert r.status_code == 200