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

    return r.json()

def get_user_records(api_url, user_id=None, habit_id=None):
    session = requests.Session()

    if habit_id:
        r = session.get(api_url+"habit/"+str(habit_id)+'/record')
    elif user_id:
        r = session.get(api_url+"user/"+str(user_id)+'/record')
    else:
        print('Need to provide user_id or habit_id')
        return None

    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None

    return r.json()

def post_item(api_url, item, type):
    session = requests.Session()

    r = session.post(api_url + type, json=item)

    if r.status_code != 200:
        return f'Failed post request, code:{r.status_code}'

def put_item(api_url, item, itemid, type):
    session = requests.Session()

    r = session.put(api_url + type + '/' + str(itemid), json=item)

    if r.status_code != 201:
        return f'Failed put request, code:{r.status_code}'

def delete_item(api_url, itemid, type):
    session = requests.Session()

    r = session.delete(api_url + type + '/' + str(itemid))

    if r.status_code != 200:
        return f'Failed delete request, code:{r.status_code}'

def get_measurements(api_url):
    session = requests.Session()

    r = session.get(api_url+'measurement')

    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None

    return r.json()