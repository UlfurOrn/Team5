import functools
import datetime
from ast import literal_eval

from .auth import login_required

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits, get_user_records, post_item, delete_item, put_item, get_measurements
from .auth import login_required

bp = Blueprint('habit', __name__, url_prefix='/habit')

# User habits view


@bp.route('/', methods=('GET', 'POST'))
@login_required
def userhabits():
    habitdict = get_user_habits(
        current_app.config['API_URL'], user_id=session.get('user_id'))

    return render_template('habits/habits.html', habits=habitdict['habits'])


@bp.route('/<habit>', methods=('GET', 'POST'))
@login_required
def single_habit(habit):
    habit = literal_eval(habit)
    linked_records = get_user_records(
        current_app.config['API_URL'], habit_id=habit['habitid'])

    return render_template('/habits/single_habit.html', habit=habit, records=linked_records['records'])


@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add_habit():
    measurements = get_measurements(current_app.config['API_URL'])[
        'measurements']
    if request.method == 'POST':
        userid = int(session.get('user_id'))
        name = request.form['name']
        description = request.form['description']
        measurement_id = int(request.form['measurement'])

        error = None

        habit = {
            'userid': userid,
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
@login_required
def update_habit(habit):
    measurements = get_measurements(current_app.config['API_URL'])[
        'measurements']
    habit = literal_eval(habit)
    if request.method == 'POST':
        habitid = habit['habitid']
        userid = int(session.get('user_id'))
        name = request.form['name']
        description = request.form['description']
        measurement_id = int(request.form['measurement'])

        error = None

        habit = {
            'userid': userid,
            'name': name,
            'description': description,
            'measurementid': measurement_id
        }

        error = put_item(
            current_app.config["API_URL"], habit, habitid, 'habit')

        if error is None:
            habit['habitid'] = habitid
            return redirect(url_for('habit.single_habit', habit=habit))

        flash(error)

    return render_template('/habits/update_habit.html', habit=habit, measurements=measurements)


@bp.route('/<habit>/delete', methods=('GET', 'POST'))
@login_required
def delete_habit(habit):
    delete_item(current_app.config["API_URL"],
                literal_eval(habit)['habitid'], 'habit')
    return redirect(url_for('habit.userhabits'))


@bp.route('/records', methods=('GET', 'POST'))
@login_required
def userrecords():
    recorddict = get_user_records(
        current_app.config['API_URL'], session.get('user_id'))
    if request.method == 'POST':
        start_datetime = datetime.datetime.strptime(request.form['start_date'] + 'T' + request.form['start_time'], '%Y-%m-%dT%H:%M')
        end_datetime = datetime.datetime.strptime(request.form['end_date'] + 'T' + request.form['end_time'], '%Y-%m-%dT%H:%M')
        recorddict = record_daterange((start_datetime, end_datetime), recorddict['records'])

    return render_template('habits/records.html', records=recorddict['records'])

def record_daterange(daterange, records):
    '''Finds records withing a certain daterange

    Args:
        daterange (tuple): Tuple of datetime objects (start date, end date)
        records (list): List of recoords

    Returns:
        ret_dict (dict): The records that fit in the daterange
    '''

    ret_dict = {'records': []}
    for record in records:
        if daterange[0] <= datetime.datetime.strptime(record['rdate'], '%Y-%m-%dT%H:%M:%S') <= daterange[1]:
            ret_dict['records'].append(record)
    
    return ret_dict


@bp.route('/records/<record>', methods=('GET', 'POST'))
@login_required
def single_record(record):
    return render_template('/habits/single_record.html', record=literal_eval(record))


@bp.route('/record/add', methods=('GET', 'POST'))
@login_required
def add_record():
    habits = get_user_habits(
        current_app.config['API_URL'], session.get('user_id'))['habits']

    if request.method == 'POST':
        userid = int(session.get('user_id'))
        rdate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        amount = int(request.form['amount'])
        habitid = int(request.form['habit_id'])

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

    return render_template('habits/add_record.html', habits=habits)


@bp.route('/records/<record>/update', methods=('GET', 'POST'))
@login_required
def update_record(record):
    habits = get_user_habits(
        current_app.config['API_URL'], session.get('user_id'))['habits']
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

        error = put_item(
            current_app.config["API_URL"], record, recordid, 'record')

        if error is None:
            return redirect(url_for('habit.single_record', record=record))

        flash(error)

    return render_template('/habits/update_record.html', record=record, habits=habits)


@bp.route('/records/<record>/delete', methods=('GET', 'POST'))
@login_required
def delete_record(record):
    delete_item(current_app.config["API_URL"],
                literal_eval(record)['recordid'], 'record')
    return redirect(url_for('habit.userrecords'))
