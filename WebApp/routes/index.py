import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

bp = Blueprint('index', __name__, url_prefix='/')

# Index view
@bp.route('/')
def index():
    return redirect(url_for('auth.login'))