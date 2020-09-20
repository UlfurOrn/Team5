import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
from werkzeug.security import check_password_hash, generate_password_hash

from ..services.api_calls import save_user, get_user, get_user_id, user_login

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register view
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        date_of_birth = request.form['dateOfBirth']
        gender = request.form['gender']
        weight = request.form['weight']
        height = request.form['height']

        error = None

        print(type(date_of_birth))

        if not username:
            error = 'Username required'
        elif not password:
            error = 'Password required'

        if error is None:
            user = {
                'name': name,
                'email': email,
                'dob': date_of_birth + 'T00:00:00',
                'username': username,
                'password': password,
                'gender': gender,
                'weight': int(weight),
                'height': int(height)
            }

            resp = save_user(current_app.config["API_URL"], user)

            if resp is None:
                return redirect(url_for('auth.login'))
            else:
                error = resp

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        print(f'Getting user {username} from api: {current_app.config["API_URL"]}')

        resp = user_login(current_app.config["API_URL"], username, password)

        if not resp:
            error = 'failed to login'
        
        if error is None:
            session.clear()
            session['user_ud'] = 1
            return redirect(url_for('habit.userhabits'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@bp.before_app_first_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if  user_id is None:
        g.user = None
    else:
        # Get the user from the database
        g.user = get_user_id(current_app.config['API_URL'], user_id)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
    

