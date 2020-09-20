import requests

def get_user(api_url, username):
    session = requests.Session()

    r = session.get(api_url + 'user/')
    
    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None
    
    users = r.json()

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
    account = r.json()
    return account

def save_user(api_url, user):
    session = requests.Session()

    r = session.post(api_url + 'user', data=user)
    
    if r.status_code != 200:
        print(r.json)
        return f'Cannot connect to API {r.status_code}'

def get_user_habits(api_url,user_id):
    session = requests.Session()
    
    r = session.get(api_url+'habit/'+str(user_id))
    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None
    print("Status Code: \n")
    habits = r.json()
    return habits