import requests


def user_login(api_url, username, password):
    session = requests.Session()
    user_login_form = {'username': username, 'password': password}

    r = session.post(api_url + "auth/login", json=user_login_form)

    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return False

    return True

def get_user(api_url, username):
    session = requests.Session()

    r = session.get(api_url + 'user')
    
    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None
    
    users = r.json()["users"]

    for user in users:
        if user['username'] == username:
            return user

    print('Cannot find user')
    return None

def get_user_id(api_url, user_id):
    session = requests.Session()

    r = session.get(api_url + 'user/' + str(user_id))
    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None

    return r.json()

def save_user(api_url, user):
    session = requests.Session()
    
    r = session.post(api_url + 'user', json=user)
    
    if r.status_code != 200:
        return f'Cannot connect to API {r.status_code}'

def save_edited_user(api_url, user_id,user):
    session = requests.Session()

    r = session.put(api_url + 'user/'+str(user_id), json=user)
    
    if r.status_code != 200:
        return f'Cannot connect to API {r.status_code}'

def get_user_habits(api_url, user_id):
    session = requests.Session()
    
    r = session.get(api_url+'user/'+str(user_id)+'/habit')
    
    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None

    habits = r.json()
    return habits

def get_user_records(api_url, user_id):
    session = requests.Session()

    r = session.get(api_url+"user/"+str(user_id)+'/record')

    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None

    return r.json()

def post_habit(api_url, habit):
    session = requests.Session()

    r = session.post(api_url+'habit', json=habit)

    if r.status_code != 200:
        print(r.status_code)
        return f'Failed posting habit, code:{r.status_code}'

def post_record(api_url, record):
    session = requests.Session()

    r = session.post(api_url+'record', json=record)

    if r.status_code != 200:
        print(r.status_code)
        return f'Failed posting record, code:{r.status_code}'

def put_habit(api_url, habit, habitid):
    session = requests.Session()

    r = session.put(api_url+'habit/'+str(habitid), json=habit)

    if r.status_code != 200:
        return f'Failed put habit, code:{r.status_code}'

def put_record(api_url, record, recordid):
    session = requests.Session()

    r = session.put(api_url+'record/'+str(recordid), json=record)

    if r.status_code != 200:
        return f'Failed put record, code:{r.status_code}'

def delete_item(api_url, itemid, type):
    session = requests.Session()

    r = session.delete(api_url + type + '/' + str(itemid))

    if r.status_code != 200:
        return f'Failed to delete item, code:{r.status_code}'