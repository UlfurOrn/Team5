import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
from werkzeug.security import check_password_hash, generate_password_hash

from ..services.api_calls import save_user, get_user, get_user_id

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register view
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username required'
        elif not password:
            error = 'Password required'

        if error is None:
            print(f'Adding user {username} to api: {current_app.config["API_URL"]}')
            user = {
                'username': username,
                'password_hash': generate_password_hash(password)
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
        user = get_user(current_app.config["API_URL"], username)

        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'
        
        if error is None:
            session.clear()
            session['user_ud'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

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
    

