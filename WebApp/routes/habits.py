import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import get_user_habits

bp = Blueprint('habit', __name__, url_prefix='/habit')

# User habits view
@bp.route('/', methods=('GET','POST'))
def userhabits():
    #user_id = session.get('user_id')
    user_id = 1
    if request.method == 'GET':
        habitdict = get_user_habits(current_app.config['API_URL'],user_id)
        #print(habits)
    return render_template('habits/habits.html', habits=habitdict['habits'])
        

