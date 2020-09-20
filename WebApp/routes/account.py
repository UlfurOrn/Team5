import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
from ..services.api_calls import get_user_id

bp = Blueprint('account', __name__, url_prefix='/account')

# User account view
@bp.route('/', methods=('GET','POST'))
def viewAccount():
    user_id = 2
    if request.method == 'GET':
        details = get_user_id(current_app.config['API_URL'], user_id)
    return render_template('account/viewAccount.html', account=details)
