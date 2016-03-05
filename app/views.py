from __future__ import print_function

from app import app, db
from models import User
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
import logging

import os
import json
import requests
from flask import request, jsonify, session, redirect
from flask import render_template, send_from_directory
from functools import wraps

# TODO: This shouldn't be here.
AUTH0_CLIENT_ID = "DjhO1VyfUgOozHXlBkwOxI07e31xwmeX"
AUTH0_CLIENT_SECRET = "vglZfTY2xXOXGjH02DOtzXewzd2mAW_gU7Bf-ThWrOXFR4HLhSS7GFxrfvxKoKYO"
#AUTH0_CALLBACK_URI = "http://192.168.99.100:5000/user"
AUTH0_CALLBACK_URI = "http://127.0.0.1:8000/user"

def check_session(f):
    """Decorator function for sign-in hook"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' in session:
            # Redirect to Login page
            return redirect('/user')
        return f(*args, **kwargs)

    return decorated

@app.route('/')
@app.route('/index')
@app.route('/signin')
@check_session
def index():
    """Sign In controller"""

    return render_template('signin.html')

@app.route('/callback')
def callback_handling():
    """Callback controller for Auth0 service"""
    env = os.environ
    code = request.args.get('code')

    json_header = {'content-type': 'application/json'}

    token_url = "https://{domain}/oauth/token".format(domain='golfr-io.auth0.com')

    token_payload = {
        'client_id':     AUTH0_CLIENT_ID,
        'client_secret': AUTH0_CLIENT_SECRET,
        'redirect_uri':  AUTH0_CALLBACK_URI,
        'code':          code,
        'grant_type':    'authorization_code'
    }

    token_info = requests.post(token_url, data=json.dumps(token_payload), headers=json_header).json()

    user_url = "https://{domain}/userinfo?access_token={access_token}".format(domain='golfr-io.auth0.com', access_token=token_info['access_token'])

    user_info = requests.get(user_url).json()

    # Save all user information into the session
    session['profile'] = user_info

    # Redirect to the user's page
    return redirect('/user')

def requires_auth(f):
    """Decorator function for sign-in hook"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            # Redirect to Login page
            return redirect('/')
        return f(*args, **kwargs)

    return decorated

def save_user_hook(f):

    @wraps(f)
    
    def decorated(*args, **kwargs):
        
        if 'profile' in session:
            username = session['profile']['nickname']
            user_email = session['profile']['email']
            
            if User.query.filter_by(username=username) is  None:
                try:
                    user = User(username, user_email)
                    db.session.add(user)
                    db.session.commit()
                except:
                    # TODO: redirect to 500 page
                    pass

        return f(*args, **kwargs)

    return decorated

@app.route('/user')
@requires_auth
@save_user_hook
def user():
    """User's logged in landing page"""
    return render_template('user.html', user=session['profile'])

@app.route('/logout')
def logout():
    if session['profile']:
        session.clear()

    return redirect('/')
