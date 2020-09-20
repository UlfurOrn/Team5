import functools

from .auth import login_required

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits, create_habit

bp = Blueprint('habit', __name__, url_prefix='/habit')

# User habits view
@bp.route('/', methods=('GET','POST'))
def userhabits():
    #user_id = session.get('user_id')
    user_id = 1
    habitdict = get_user_habits(current_app.config['API_URL'],user_id)
    if request.method == 'GET':
<<<<<<< HEAD
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
=======
        habitdict = get_user_habits(current_app.config['API_URL'],user_id)
        #print(habits)
>>>>>>> a9bc2333e4e299a7399d461afb0ae675d4f684a3
    return render_template('habits/habits.html', habits=habitdict['habits'])
