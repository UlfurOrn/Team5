from app.main.controller.services.dbapi import DBapi

def test_get_single_user(mock_db):
    test_user = {
        'name': "TestUser",
        'email': ""
        'dob': ""
        'gender': ""
        'weight': ""
        'height': ""
    }

    mock_db.return_value = test_type

    data = requests.get(URL + "/get/1")
    int = "k"
    

def test_get_user_list():
    pass

def test_post_user():
    pass

def test_put_user():
    pass

def test_delete_user():
    pass
