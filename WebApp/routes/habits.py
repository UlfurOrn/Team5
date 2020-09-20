import functools

from .auth import login_required

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits, get_user_records

bp = Blueprint('habit', __name__, url_prefix='/habit')

# User habits view
@bp.route('/', methods=('GET','POST'))
def userhabits():
    #user_id = session.get('user_id')
    user_id = 1
    habitdict = get_user_habits(current_app.config['API_URL'],user_id)
    if request.method == 'GET':
        somestatement = True
    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        measurement = request.form['measurement']

        
        habit = {
            'name': name,
            'description': description,
            'measurement': measurement,
            'userid' : user_id
        }

        resp = create_habit(current_app.config["API_URL"], habit)
    return render_template('habits/habits.html', habits=habitdict['habits'])


@bp.route('/records', methods=('GET','POST'))
def userrecords():
    #user_id = session.get('user_id')
    user_id = 1
    recorddict = get_user_records(current_app.config['API_URL'], user_id)
    if request.method == 'GET':
        somestatement = True

    return render_template('habits/records.html', records=recorddict['records'])
