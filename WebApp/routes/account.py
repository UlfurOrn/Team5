import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
from ..services.api_calls import get_user_id

bp = Blueprint('account', __name__, url_prefix='/account')

# User account view
@bp.route('/viewaccount', methods=('GET'))
def viewAccount():
    user_id = session.get('user_id')
    if request.method == 'GET':
        accountDetails = get_user_id(current_app.config['API_URL'].user_id)
    return render_template('viewAccount.html', account=accountDetails)

