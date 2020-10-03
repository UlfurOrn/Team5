import functools

from .auth import login_required

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits, get_user_records, post_habit

bp = Blueprint('habit', __name__, url_prefix='/habit')

# User habits view
@bp.route('/', methods=('GET','POST'))
def userhabits():
    habitdict = get_user_habits(current_app.config['API_URL'], session.get('user_id'))

    return render_template('habits/habits.html', habits=habitdict['habits'])

@bp.route('/add', methods=('GET', 'POST'))
def add_habit():
    if request.method == 'POST':
        userid = int(session.get('user_id'))
        name = request.form['name']
        description = request.form['description']
        measurement_id = int(request.form['measurement_id'])

        error = None

        habit = {
            'userid' : userid,
            'name': name,
            'description': description,
            'measurementid': measurement_id
        }
        print(habit)

        error = post_habit(current_app.config["API_URL"], habit)
        
        if error is None:
            return redirect(url_for('habit.userhabits'))
        
        flash(error)

    return render_template('habits/add_habit.html')

@bp.route('/records', methods=('GET','POST'))
def userrecords():
    recorddict = get_user_records(current_app.config['API_URL'], session.get('user_id'))
    if request.method == 'GET':
        somestatement = True

    return render_template('habits/records.html', records=recorddict['records'])
