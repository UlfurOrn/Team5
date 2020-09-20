import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import save_user, get_user, get_user_id, save_edited_user

bp = Blueprint('account', __name__, url_prefix='/account')

# User account view
@bp.route('/', methods=('GET','POST'))
def viewAccount():
    user_id = session.get('user_id')
    if request.method == 'GET':
        details = get_user_id(current_app.config['API_URL'], user_id)
    return render_template('account/viewAccount.html', account=details)

@bp.route('/edit', methods=('GET','POST'))
def editAccount():
    user_id = 2
    if request.method == 'GET':
        details = get_user_id(current_app.config['API_URL'], user_id)
    elif request.method == 'POST':
        details = get_user_id(current_app.config['API_URL'], user_id)
        name = request.form['fullname']
        error = None
        if error is None:
            print(f'Changing name to api: {current_app.config["API_URL"]}')
            user = {
                'name': name,
            }
            resp = save_edited_user(current_app.config["API_URL"], user_id,user)
            if resp is None:
                error = resp
            else:
                error = resp
        flash(error)

    return render_template('account/editAccount.html', account=details)