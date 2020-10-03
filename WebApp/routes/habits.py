import functools
import datetime

from .auth import login_required

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits, get_user_records, post_habit, post_record

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


@bp.route('/record/add', methods=('GET', 'POST'))
def add_record():
    if request.method == 'POST':
        userid = int(session.get('user_id'))
        habitid = int(request.form['habit_id'])
        rdate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        amount = int(request.form['amount'])

        error = None

        record = {
            'userid': userid,
            'habitid': habitid,
            'rdate': rdate,
            'amount': amount
        }

        error = post_record(current_app.config["API_URL"], record)

        if error is None:
            return redirect(url_for('habit.userrecords'))
        
        flash(error)

    return render_template('habits/add_record.html')