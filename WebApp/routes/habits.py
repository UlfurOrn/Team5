import functools

from .auth import login_required

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits, save_new_habit

bp = Blueprint('habit', __name__, url_prefix='/habit')

# User habits view
@bp.route('/', methods=('GET','POST'))
def userhabits():
    user_id = session.get('user_id')
    if request.method == 'GET':
        habitdict = get_user_habits(current_app.config['API_URL'],user_id)
    
    return render_template('habits/habits.html', habits=habitdict['habits'])

@bp.route('/add', methods=('GET','POST'))
def add_habit():
    if request.method == 'POST':
        habit = {
            'userid': session.get('user_id'),
            'name': request.form['name'],
            'description': request.form['description']
        }
        save_new_habit(current_app.config["API_URL"], habit)

    return render_template('habits/add_habit.html')