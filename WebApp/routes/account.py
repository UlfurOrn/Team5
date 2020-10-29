import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from ..services.api_calls import post_item, get_user, get_user_id, save_edited_user

bp = Blueprint('account', __name__, url_prefix='/account')

# User account view
@bp.route('/', methods=('GET','POST'))
def viewAccount():
    user_id = session.get('user_id')
    if request.method == 'GET':
        details = get_user_id(current_app.config['API_URL'], user_id)
    return render_template('account/viewAccount.html', account=details)

@bp.route('/edit', methods=('GET','POST'))
def editAccount():
    user_id = session.get('user_id')
    if request.method == 'GET':
        details = get_user_id(current_app.config['API_URL'], user_id)
    elif request.method == 'POST':
        details = get_user_id(current_app.config['API_URL'], user_id)

        print(details)

        if (request.form['fullname'] == ""):
            name = details['name']
        else:
            name = request.form['fullname']

        if (request.form['email'] == ""):
            email= details['email']
        else:
            email = request.form['email']

        if (request.form['dateOfBirth']==''):
            dob = details['dob']
        else:
            dob = request.form['dateOfBirth']

        if (request.form['weight'] == ''):
            weight = details['weight']
        else:
            weight = request.form['weight']

        if (request.form['height']==''):
            height = details['height']
        else:
            height = request.form['height']

        #try:
        #    if (request.form['gender']==None):
        #        gender = details['gender']
        #    else:
        #        gender = request.form['gender']
        #except:
         #   gender = request.form['gender']

        
        error = None
        if error is None:
            print(f'Changing name to api: {current_app.config["API_URL"]}')
            user = {
                'name': name,
                'email':email,
                'dob':dob,
                'weight':weight,
                'height':height
                #'gender':gender
            }
            resp = save_edited_user(current_app.config["API_URL"], user_id,user)
            if resp is None:
                error = resp
            else:
                error = resp
        flash(error)

    return render_template('account/editAccount.html', account=details)

@bp.route('/editpassword', methods=('GET','POST'))
def editPassword():
    user_id = session.get('user_id')
    if request.method == 'GET':
        details = get_user_id(current_app.config['API_URL'], user_id)
    elif request.method == 'POST':
        details = get_user_id(current_app.config['API_URL'], user_id)

        print(details)
        error = None
        if (request.form['password1']==''):
            password = details['password']
        else:
            if(request.form['password1']!=request.form['password2']):
                error = "Passwords dont match"
                password = details['password']
            else:       
                password = request.form['password1']
            
        if error is None:
            print(f'Changing name to api: {current_app.config["API_URL"]}')
            user = {
                'password':password
            }
            resp = save_edited_user(current_app.config["API_URL"], user_id,user)
            if resp is None:
                error = resp
            else:
                error = resp
            flash('Password successfully changed')
        else:
            flash(error)


      

        
    return render_template('account/editPassword.html', account=details)