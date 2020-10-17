import functools
import datetime
from ast import literal_eval

from .auth import login_required

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits, get_user_records, post_item, delete_item, put_item, get_measurements

bp = Blueprint('habit', __name__, url_prefix='/habit')

# User habits view
@bp.route('/', methods=('GET','POST'))
def userhabits():
    habitdict = get_user_habits(current_app.config['API_URL'], user_id=session.get('user_id'))

    return render_template('habits/habits.html', habits=habitdict['habits'])

@bp.route('/<habit>', methods=('GET', 'POST'))
def single_habit(habit):
    habit = literal_eval(habit)
    linked_records = get_user_records(current_app.config['API_URL'], habit_id=habit['habitid'])
    print(linked_records)
    return render_template('/habits/single_habit.html', habit=habit, records=linked_records['records'])

@bp.route('/add', methods=('GET', 'POST'))
def add_habit():
    measurements = get_measurements(current_app.config['API_URL'])['measurements']
    if request.method == 'POST':
        userid = int(session.get('user_id'))
        name = request.form['name']
        description = request.form['description']
        measurement_id = int(request.form['measurement'])

        error = None

        habit = {
            'userid' : userid,
            'name': name,
            'description': description,
            'measurementid': measurement_id
        }

        error = post_item(current_app.config["API_URL"], habit, 'habit')
        
        if error is None:
            return redirect(url_for('habit.userhabits'))
        
        flash(error)

    return render_template('habits/add_habit.html', measurements=measurements)

@bp.route('/<habit>/update', methods=('GET', 'POST'))
def update_habit(habit):
    habit = literal_eval(habit)
    if request.method == 'POST':
        habitid = habit['habitid']
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

        error = put_itemm(current_app.config["API_URL"], habit, habitid, 'habit')

        if error is None:
            return redirect(url_for('habit.single_habit', habit=habit))

        flash(error)

    return render_template('/habits/update_habit.html', habit=habit)

@bp.route('/<habit>/delete', methods=('GET','POST'))
def delete_habit(habit):
    delete_item(current_app.config["API_URL"], literal_eval(habit)['habitid'], 'habit')
    return redirect(url_for('habit.userhabits'))

@bp.route('/records', methods=('GET','POST'))
def userrecords():
    recorddict = get_user_records(current_app.config['API_URL'], session.get('user_id'))
    if request.method == 'GET':
        somestatement = True

    return render_template('habits/records.html', records=recorddict['records'])

@bp.route('/records/<record>', methods=('GET', 'POST'))
def single_record(record):
    return render_template('/habits/single_record.html', record=literal_eval(record))

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

        error = post_item(current_app.config["API_URL"], record, 'record')

        if error is None:
            return redirect(url_for('habit.userrecords'))
        
        flash(error)

    return render_template('habits/add_record.html')

@bp.route('/records/<record>/update', methods=('GET', 'POST'))
def update_record(record):
    record = literal_eval(record)
    if request.method == 'POST':
        recordid = record['recordid']
        userid = int(session.get('user_id'))
        habitid = int(request.form['habitid'])
        rdate = request.form['date']
        amount = int(request.form['amount'])

        error = None

        record = {
            'userid': userid,
            'habitid': habitid,
            'rdate': rdate,
            'amount': amount
        }

        error = put_itemm(current_app.config["API_URL"], record, recordid, 'record')

        if error is None:
            return redirect(url_for('habit.single_record', record=record))

        flash(error)

    return render_template('/habits/update_record.html', record=record)

@bp.route('/records/<record>/delete', methods=('GET', 'POST'))
def delete_record(record):
    delete_item(current_app.config["API_URL"], literal_eval(record)['recordid'], 'record')
    return redirect(url_for('habit.userrecords'))